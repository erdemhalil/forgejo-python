"""Integration harness: container boot, readiness, CLI seeding, and the seed model.

The harness owns everything the integration suite needs from the outside world:
a session-scoped Forgejo container, readiness polling, admin/token seeding via
the ``forgejo admin`` CLI, and a lazily-seeded :class:`Seed` used by the smoke
registry and the scenario suite.

Forgejo 16 runtime notes discovered by this suite:

- Empty list responses are sometimes JSON ``null`` instead of ``[]``
  (issue/comment reactions, issue templates, some Actions job lists); pyfj
  decodes per Spec and raises ``DecodeError``. Scenario tests pin the cases
  that matter.
- ``ActivityPub``'s ``@context`` was observed as a JSON array while the Spec
  types it as a string; federation is disabled in this harness, so the suite
  does not currently re-verify that observation.
- Body-less POST/PUT requests (``createFork``, ``addCollaborator``, ...) are
  rejected with ``422 Empty Content-Type`` unless a body field is sent.
- User-directed repository transfers complete immediately; ``accept`` and
  ``reject`` have no pending transfer to act on.
- Actions secret and variable names must match ``[A-Za-z_][A-Za-z0-9_]*``.
- Token-management endpoints reject token authentication and require Basic
  auth.
- Wiki page titles containing dashes cannot be fetched or deleted by name.
- ``releases/latest`` ignores tags that do not parse as versions.
- Git hook endpoints need ``DISABLE_GIT_HOOKS=false`` and (for non-admins)
  ``allow_git_hook``.

This module imports the library under test only through its public surface.
"""

from __future__ import annotations

import base64
import contextlib
import os
import re
import secrets
import time
from dataclasses import dataclass
from functools import cached_property
from typing import TYPE_CHECKING, Literal, TypeVar, cast

import httpx2
from testcontainers.core.container import DockerContainer, ExecConfig
from testcontainers.core.docker_client import DockerClient

import pyfj

if TYPE_CHECKING:
    from collections.abc import Callable, Sequence

    from testcontainers.core.container import BytesExecResult

T = TypeVar("T")

DEFAULT_IMAGE = "codeberg.org/forgejo/forgejo:16"
MIRROR_IMAGE = "data.forgejo.org/forgejo/forgejo:16"
CONTAINER_PORT = 3000
READY_TIMEOUT_SECONDS = 240.0
READY_POLL_INTERVAL = 0.25
#: Test-client request timeout; longer than the library default so shared CI
#: runners absorb slow container I/O without spurious TransportError flakes.
CLIENT_TIMEOUT = 60.0
CLI_USER = "1000"  # the unprivileged ``git`` user the CLI must run as

ADMIN_USERNAME = "pyfj-admin"
ADMIN_PASSWORD = "pyfj-admin-pass-1234"
ADMIN_EMAIL = "pyfj-admin@pyfj.test"
USER_USERNAME = "pyfj-user"
USER_PASSWORD = "pyfj-user-pass-1234"
USER_EMAIL = "pyfj-user@pyfj.test"
TOKEN_NAME = "pyfj-integration"

# Distinct, static ed25519 public keys: Forgejo rejects duplicate key material,
# and the private halves are intentionally not kept (the API only needs the
# public key).
SSH_PUBLIC_KEYS = (
    "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIF39AOTH9svH1qlVp/0ha3xDNAiH8mBUD1nLdjYfn0ck pyfj-key-1",
    "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIJawK9m6//Sz9YIbfK0OQbN//piPPWXLGPAmuzB4ERtC pyfj-key-2",
    "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIML3bXA2mvmgv25ZC4CZQEdX+rGXU/GBXHDPLJOAnLPK pyfj-key-3",
    "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIFHtvunOYASgmQX7DWATp7BfrXbyctTGdqZ4hr/7fcHY pyfj-key-4",
    "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIBTFhfmlytdmizWMypg6LFrG0royTl7cp2mqZAUCs7JY pyfj-pool-1",
    "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIIMELtgG2g5N2WdiMcNAmaD+kxpbK4l5rQ1rcOEnjs0Y pyfj-pool-2",
    "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIIoWK7Eb7cCq3nLoEhmLxNf05WZ5CfFuUdSYgid5yswR pyfj-pool-3",
    "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAILPiXjbnlGkc3nstDGqb2KTKpOlRXtRNQ6cBKJP2pc1y pyfj-pool-4",
    "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIE2XJQhARDJb6acbHQWjnE0mNovwcZy676b7IPITo+Sh pyfj-pool-5",
    "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIOWhBiQYbM/rRscy6wA+vY0WcXnFFbgotJo1K8h0ccH1 pyfj-pool-6",
    "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIGcFMCkm+y2896eGRpc8NaUu8VxsYEPsWMns1UhKJK2w pyfj-pool-7",
    "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIJtc+PmeoE564Y7ZBd6IHiBzlp1UxoW+Rkes2XvJPA53 pyfj-pool-8",
)

#: A 1x1 transparent PNG, for avatar endpoints.
TINY_PNG_BASE64 = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNk+M9QDwADhgGAWjR9awAAAABJRU5ErkJggg=="

_OPERATION_ID = re.compile(r"Operation ID: (\S+)")


class DockerUnavailableError(RuntimeError):
    """Raised when the Docker daemon cannot be reached."""


def docker_available() -> bool:
    """Return whether the Docker daemon answers; never raises."""
    try:
        return bool(DockerClient().client.ping())
    except Exception:  # noqa: BLE001 - any client failure means "not available"
        return False


@dataclass
class ForgejoServer:
    """A booted Forgejo container with seeded admin/regular-user tokens."""

    container: DockerContainer
    base_url: str
    run_id: str
    admin_token: str
    user_token: str

    def cli(self, *args: str) -> str:
        """Run a ``forgejo`` CLI command in the container as the ``git`` user."""
        result: BytesExecResult = self.container.exec(ExecConfig(command=["forgejo", *args], user=CLI_USER))
        output = result.output.decode("utf-8", errors="replace")
        if result.exit_code != 0:
            joined = " ".join(args)
            message = f"forgejo {joined} failed with exit code {result.exit_code}: {output.strip()}"
            raise RuntimeError(message)
        return output.strip()

    def stop(self) -> None:
        """Stop and remove the container; never raises."""
        with contextlib.suppress(Exception):
            self.container.stop(force=True)

    def logs(self) -> str:
        """Return the container logs (stdout + stderr) for failure reports."""
        try:
            stdout, stderr = self.container.get_logs()
        except Exception as exc:  # noqa: BLE001 - best-effort diagnostics
            return f"<could not read container logs: {exc}>"
        return (stdout + b"\n" + stderr).decode("utf-8", errors="replace")


def _container(image: str) -> DockerContainer:
    """Create the container with the harness's explicit configuration overrides.

    Every override is deliberate; defaults that would hide coverage are turned
    on, and features that destabilise the shared instance are turned off:

    - ``security DISABLE_GIT_HOOKS``: off so the git-hook operations are usable.
    - ``quota ENABLED``: on so the quota surface exists (tests keep the seeded
      users out of restrictive groups).
    - ``repository ENABLE_FLAGS``: on so the (non-default) repo-flags surface
      exists.
    - ``migrations ALLOW_LOCALNETWORKS``: on so the migrate/mirror operations
      can clone from the instance's own localhost address inside the container.
    - ``actions ENABLED``: on so runner/secret/variable operations exist.
    - ``service DISABLE_REGISTRATION`` / ``webhook ALLOWED_HOST_LIST``: classic
      harness conveniences (CLI users and unreachable test webhook URLs).
    - ``federation``: left at its default (off); with it on, starring a
      repository fails with a Forgejo 500 and the ActivityPub routes demand
      HTTP signatures.
    - ``mailer/cron``: off to keep logs quiet and the container deterministic.
    """
    return (
        DockerContainer(image)
        .with_exposed_ports(CONTAINER_PORT)
        .with_env("FORGEJO__database__DB_TYPE", "sqlite3")
        .with_env("FORGEJO__security__INSTALL_LOCK", "true")
        .with_env("FORGEJO__security__DISABLE_GIT_HOOKS", "false")
        .with_env("FORGEJO__server__DOMAIN", "localhost")
        .with_env("FORGEJO__server__HTTP_PORT", str(CONTAINER_PORT))
        .with_env("FORGEJO__server__ROOT_URL", f"http://localhost:{CONTAINER_PORT}/")
        .with_env("FORGEJO__actions__ENABLED", "true")
        .with_env("FORGEJO__quota__ENABLED", "true")
        .with_env("FORGEJO__repository__ENABLE_FLAGS", "true")
        .with_env("FORGEJO__migrations__ALLOW_LOCALNETWORKS", "true")
        .with_env("FORGEJO__service__DISABLE_REGISTRATION", "false")
        .with_env("FORGEJO__webhook__ALLOWED_HOST_LIST", "*")
        .with_env("FORGEJO__attachment__ENABLED", "true")
        .with_env("FORGEJO__lfs__START_SERVER", "true")
        .with_env("FORGEJO__mailer__ENABLED", "false")
        .with_env("FORGEJO__cron__ENABLED", "false")
        .with_env("FORGEJO__log__LEVEL", "Warn")
        .with_env("FORGEJO__repository__DEFAULT_BRANCH", "main")
    )


def _wait_for_version(client: httpx2.Client, base_url: str, *, server: ForgejoServer) -> None:
    """Poll ``/api/v1/version`` until the instance answers or the deadline passes."""
    url = f"{base_url}/api/v1/version"
    deadline = time.monotonic() + READY_TIMEOUT_SECONDS
    last_error: Exception | None = None
    while time.monotonic() < deadline:
        try:
            response = client.get(url)
            if response.status_code == httpx2.codes.OK:
                return
            last_error = RuntimeError(f"GET {url} returned HTTP {response.status_code}: {response.text[:200]}")
        except httpx2.HTTPError as exc:
            last_error = exc
        time.sleep(READY_POLL_INTERVAL)
    container_logs = server.logs()
    message = f"Forgejo did not become ready at {url} within {READY_TIMEOUT_SECONDS:.0f}s: {last_error}"
    message = f"{message}\n--- container logs ---\n{container_logs[-4000:]}"
    raise TimeoutError(message) from last_error


def _last_line(output: str) -> str:
    lines = [line.strip() for line in output.splitlines() if line.strip()]
    if not lines:
        message = "expected the forgejo CLI to print a value, got no output"
        raise RuntimeError(message)
    return lines[-1]


def start_forgejo() -> ForgejoServer:
    """Boot the container, wait for readiness, and seed users and tokens."""
    override = os.environ.get("PYFJ_TEST_IMAGE")
    candidates = [override] if override else [DEFAULT_IMAGE, MIRROR_IMAGE]
    errors: list[str] = []
    for image in candidates:
        container = _container(image)
        try:
            container.start()
        except Exception as exc:  # noqa: BLE001 - try the next candidate (mirror)
            errors.append(f"{image}: {exc}")
            with contextlib.suppress(Exception):
                container.stop(force=True)
            continue
        port = container.get_exposed_port(CONTAINER_PORT)
        base_url = f"http://127.0.0.1:{port}"
        server = ForgejoServer(
            container=container,
            base_url=base_url,
            run_id=secrets.token_hex(3),
            admin_token="",
            user_token="",
        )
        try:
            with httpx2.Client(timeout=5.0) as client:
                _wait_for_version(client, base_url, server=server)
            _seed_users(server)
            with pyfj.Forgejo(base_url, token=server.admin_token, timeout=CLIENT_TIMEOUT) as admin:
                admin.admin.users.update(ADMIN_USERNAME, allow_git_hook=True)
        except Exception:
            server.stop()
            raise
        return server
    joined = "\n".join(errors)
    message = f"could not start a Forgejo container; tried:\n{joined}"
    raise DockerUnavailableError(message)


def _seed_users(server: ForgejoServer) -> None:
    """Create the admin and regular users and generate their API tokens."""
    server.admin_token = _create_user_and_token(
        server,
        ADMIN_USERNAME,
        ADMIN_PASSWORD,
        ADMIN_EMAIL,
        admin=True,
    )
    server.user_token = _create_user_and_token(
        server,
        USER_USERNAME,
        USER_PASSWORD,
        USER_EMAIL,
    )


def _create_user_and_token(
    server: ForgejoServer,
    username: str,
    password: str,
    email: str,
    *,
    admin: bool = False,
) -> str:
    """Create one CLI user and return an API token with all scopes.

    ``--scopes all`` is a deliberate harness choice: the suite exercises both
    the user and admin surfaces with one token per seeded user.
    """
    create = [
        "admin",
        "user",
        "create",
        "--username",
        username,
        "--password",
        password,
        "--email",
        email,
        "--must-change-password=false",
    ]
    if admin:
        create.append("--admin")
    server.cli(*create)
    return _last_line(
        server.cli(
            "admin",
            "user",
            "generate-access-token",
            "--username",
            username,
            "--token-name",
            TOKEN_NAME,
            "--scopes",
            "all",
            "--raw",
        )
    )


_MISSING = object()


def _safe_getattr(obj: object, name: str) -> object:
    """Return ``obj.name`` or a sentinel when the attribute raises."""
    try:
        return getattr(obj, name)
    except Exception:  # noqa: BLE001 - a raising namespace property must not break binding
        return _MISSING


def build_method_index(client: pyfj.Forgejo) -> dict[str, Callable[..., object]]:
    """Map every ``Operation ID`` docstring on ``client`` to its bound method.

    Namespaces are walked recursively; the client itself and private attributes
    are skipped. Duplicate operation ids cannot occur in a valid generated
    surface, so the first match wins.
    """
    index: dict[str, Callable[..., object]] = {}
    seen: set[int] = set()

    def walk(obj: object) -> None:
        if id(obj) in seen:
            return
        seen.add(id(obj))
        for name in dir(obj):
            if name.startswith("_"):
                continue
            attribute = _safe_getattr(obj, name)
            if attribute is _MISSING:
                continue
            if callable(attribute):
                match = _OPERATION_ID.search(attribute.__doc__ or "")
                if match is not None:
                    index.setdefault(match.group(1), attribute)
            elif not isinstance(attribute, (str, bytes, int, float, bool, type(None))):
                walk(attribute)

    walk(client)
    return index


@dataclass(frozen=True, slots=True)
class RepoRef:
    """An ``(owner, name)`` repository reference with its path-argument tuple."""

    owner: str
    name: str

    @property
    def args(self) -> tuple[str, str]:
        return (self.owner, self.name)

    @property
    def full_name(self) -> str:
        return f"{self.owner}/{self.name}"


@dataclass(frozen=True, slots=True)
class IssueRef:
    """An issue (or pull request) reference in a repository."""

    repo: RepoRef
    index: int

    @property
    def args(self) -> tuple[str, str, int]:
        return (self.repo.owner, self.repo.name, self.index)


class Seed:
    """Session-scoped, lazily-created resources shared by smoke and scenarios.

    Every ``<thing>_for(key)`` helper caches its resource so repeated smoke
    entries reuse one object; destructive operations get their own ``key`` so
    they never delete a baseline resource another test still needs.
    """

    def __init__(self, server: ForgejoServer, admin: pyfj.Forgejo) -> None:
        self.server = server
        self.admin = admin
        self.user_client = pyfj.Forgejo(server.base_url, token=server.user_token, timeout=CLIENT_TIMEOUT)
        self.run_id = server.run_id

    def close(self) -> None:
        """Close the cached clients this seed owns."""
        self.user_client.close()
        for name in ("basic_client", "basic_user_client"):
            client = self.__dict__.get(name)
            if client is not None:
                cast("pyfj.Forgejo", client).close()

    @cached_property
    def basic_client(self) -> pyfj.Forgejo:
        """A Basic-auth client for the admin user."""
        return pyfj.Forgejo(self.server.base_url, auth=(ADMIN_USERNAME, ADMIN_PASSWORD), timeout=CLIENT_TIMEOUT)

    @cached_property
    def basic_user_client(self) -> pyfj.Forgejo:
        """A Basic-auth client for the regular user."""
        return pyfj.Forgejo(self.server.base_url, auth=(USER_USERNAME, USER_PASSWORD), timeout=CLIENT_TIMEOUT)

    def ensure_release(self) -> None:
        """Create the baseline release if no test has done so yet."""
        _ = self.release_id

    # -- names ---------------------------------------------------------------

    def name(self, kind: str, key: str = "default") -> str:
        """Return a container-unique name for ``kind``/``key``."""
        return f"{self.run_id}-{kind}-{key}"

    def secret_name(self, key: str = "default") -> str:
        """Return a container-unique name legal for an Actions secret."""
        cleaned = re.sub(r"[^A-Za-z0-9_]", "_", key.upper())
        return f"PYFJ_SECRET_{cleaned}_{self.run_id.upper()}"

    def variable_name(self, key: str = "default") -> str:
        """Return a container-unique name legal for an Actions variable."""
        cleaned = re.sub(r"[^A-Za-z0-9_]", "_", key.upper())
        return f"PYFJ_VARIABLE_{cleaned}_{self.run_id.upper()}"

    # -- repositories --------------------------------------------------------

    def repo_for(
        self,
        key: str = "default",
        *,
        owner: str | None = None,
        private: bool = False,
        auto_init: bool = True,
        template: bool = False,
        description: str | None = None,
    ) -> RepoRef:
        """Create (once) and return an org repository for smoke use."""
        return self._repo(
            owner or self.org, key, private=private, auto_init=auto_init, template=template, description=description
        )

    def user_repo_for(self, key: str = "default", *, private: bool = False, auto_init: bool = True) -> RepoRef:
        """Create (once) and return a repository owned by the regular user."""
        cache_key = f"repo:{USER_USERNAME}:{key}"
        cached = self._cache_get(cache_key)
        if cached is not None:
            return cast("RepoRef", cached)
        name = self.name("repo", key)
        try:
            repo = self.admin.admin.users.create_repo(
                USER_USERNAME,
                name=name,
                private=private,
                auto_init=auto_init,
                default_branch="main" if auto_init else None,
            )
        except pyfj.APIError as exc:
            if exc.status_code != httpx2.codes.CONFLICT:
                raise
            return self._cache_put(cache_key, RepoRef(owner=USER_USERNAME, name=name))
        ref = RepoRef(
            owner=repo.owner.login if repo.owner and repo.owner.login else USER_USERNAME,
            name=repo.name or name,
        )
        return self._cache_put(cache_key, ref)

    def _repo(
        self,
        owner: str,
        key: str,
        *,
        private: bool,
        auto_init: bool,
        template: bool = False,
        description: str | None = None,
    ) -> RepoRef:
        cache_key = f"repo:{owner}:{key}"
        cached = self._cache_get(cache_key)
        if cached is not None:
            return cast("RepoRef", cached)
        name = self.name("repo", key)
        try:
            repo = self.admin.orgs.repos.create(
                owner,
                name=name,
                private=private,
                auto_init=auto_init,
                template=template,
                description=description,
                default_branch="main" if auto_init else None,
            )
        except pyfj.APIError as exc:
            if exc.status_code != httpx2.codes.CONFLICT:
                raise
            return self._cache_put(cache_key, RepoRef(owner=owner, name=name))
        ref = RepoRef(
            owner=repo.owner.login if repo.owner and repo.owner.login else owner,
            name=repo.name or name,
        )
        return self._cache_put(cache_key, ref)

    # -- baseline resources --------------------------------------------------

    @cached_property
    def org(self) -> str:
        """The baseline organization."""
        try:
            organization = self.admin.orgs.create(username=self.name("org"), full_name="pyfj integration org")
        except pyfj.APIError as exc:
            if exc.status_code != httpx2.codes.CONFLICT:
                raise
            return self.name("org")
        return organization.username or self.name("org")

    @cached_property
    def repo(self) -> RepoRef:
        """The baseline public repository, initialized with README and main branch."""
        return self.repo_for("base")

    @cached_property
    def private_repo(self) -> RepoRef:
        """The baseline private repository."""
        return self.repo_for("private", private=True)

    @cached_property
    def template_repo(self) -> RepoRef:
        """A repository marked as a template, for ``repos.generate``."""
        return self.repo_for("template", template=True)

    @cached_property
    def empty_repo(self) -> RepoRef:
        """A repository without an initial commit, for empty-state checks."""
        return self.repo_for("empty", auto_init=False)

    @cached_property
    def fork(self) -> RepoRef:
        """A fork of the baseline repository owned by the regular user."""
        cache_key = "fork"
        cached = self._cache_get(cache_key)
        if cached is not None:
            return cast("RepoRef", cached)
        forked = self.user_client.repos.forks.create(
            self.repo.owner,
            self.repo.name,
            name=self.name("repo", "fork"),
        )
        ref = RepoRef(
            owner=forked.owner.login if forked.owner and forked.owner.login else USER_USERNAME,
            name=forked.name or self.name("repo", "fork"),
        )
        return self._cache_put(cache_key, ref)

    @cached_property
    def team_id(self) -> int:
        """The baseline team inside the baseline organization, with the user as member."""
        return self.team_for("base", members=[USER_USERNAME])

    @cached_property
    def main_sha(self) -> str:
        """The SHA of the first commit on the baseline repository's main branch."""
        commits = self.admin.repos.commits.list(self.repo.owner, self.repo.name)
        first = next(iter(commits))
        assert first.sha is not None
        return first.sha

    @cached_property
    def branch(self) -> str:
        """The baseline feature branch, created with one file commit."""
        self.admin.repos.contents.create(
            self.repo.owner,
            self.repo.name,
            "pyfj-change.txt",
            content="cHlmalBjaGFuZ2UK",
            message="add feature file",
            new_branch="pyfj-feature",
        )
        return "pyfj-feature"

    @cached_property
    def issue_index(self) -> int:
        """The baseline open issue."""
        issue = self.admin.repos.issues.create(
            self.repo.owner,
            self.repo.name,
            title=self.name("issue"),
            body="baseline issue body",
        )
        assert issue.number is not None
        return issue.number

    @cached_property
    def issue_second_index(self) -> int:
        """A second open issue, for dependency and blocking exercises."""
        issue = self.admin.repos.issues.create(
            self.repo.owner,
            self.repo.name,
            title=self.name("issue", "second"),
            body="second issue body",
        )
        assert issue.number is not None
        return issue.number

    @cached_property
    def comment_id(self) -> int:
        """The baseline comment on the baseline issue."""
        comment = self.admin.repos.issues.comments.create(
            self.repo.owner,
            self.repo.name,
            self.issue_index,
            body="baseline comment",
        )
        assert comment.id is not None
        return comment.id

    @cached_property
    def label_id(self) -> int:
        """The baseline label on the baseline repository."""
        label = self.admin.repos.labels.create(
            self.repo.owner,
            self.repo.name,
            name=self.name("label"),
            color="#00aa66",
        )
        assert label.id is not None
        return label.id

    @cached_property
    def milestone_id(self) -> int:
        """The baseline milestone on the baseline repository."""
        milestone = self.admin.repos.milestones.create(self.repo.owner, self.repo.name, title=self.name("milestone"))
        assert milestone.id is not None
        return milestone.id

    @cached_property
    def release_id(self) -> int:
        """The baseline release, created from the main branch HEAD.

        The tag is a real version (``v0.1.0``) because ``releases/latest``
        ignores releases whose tags do not parse as versions.
        """
        release = self.admin.repos.releases.create(
            self.repo.owner,
            self.repo.name,
            tag_name=self.release_tag,
            name="baseline release",
            target_commitish="main",
            body="baseline release notes",
        )
        assert release.id is not None
        return release.id

    @cached_property
    def release_tag(self) -> str:
        """The version tag of the baseline release."""
        return "v0.1.0"

    @cached_property
    def pull_index(self) -> int:
        """The baseline pull request (head: :attr:`branch`, base: main)."""
        pull = self.admin.repos.pulls.create(
            self.repo.owner,
            self.repo.name,
            title=self.name("pull"),
            head=self.branch,
            base="main",
            body="baseline pull body",
        )
        assert pull.number is not None
        return pull.number

    @cached_property
    def tracked_time_id(self) -> int:
        """The baseline tracked time entry on the baseline issue."""
        entry = self.admin.repos.issues.times.add(
            self.repo.owner,
            self.repo.name,
            self.issue_index,
            time=60,
        )
        assert entry.id is not None
        return entry.id

    @cached_property
    def issue_attachment_id(self) -> int:
        """The baseline attachment on the baseline issue."""
        attachment = self.admin.repos.issues.assets.create(
            self.repo.owner,
            self.repo.name,
            self.issue_index,
            attachment=("attachment.txt", b"pyfj attachment", "text/plain"),
        )
        assert attachment.id is not None
        return attachment.id

    @cached_property
    def comment_attachment_id(self) -> int:
        """The baseline attachment on the baseline issue comment."""
        attachment = self.admin.repos.issues.comments.assets.create(
            self.repo.owner,
            self.repo.name,
            self.comment_id,
            attachment=("comment-attachment.txt", b"pyfj comment attachment", "text/plain"),
        )
        assert attachment.id is not None
        return attachment.id

    @cached_property
    def release_attachment_id(self) -> int:
        """The baseline attachment on the baseline release."""
        attachment = self.admin.repos.releases.assets.create(
            self.repo.owner,
            self.repo.name,
            self.release_id,
            name="release-attachment.txt",
            attachment=("release-attachment.txt", b"pyfj release attachment", "text/plain"),
        )
        assert attachment.id is not None
        return attachment.id

    @cached_property
    def deploy_key_id(self) -> int:
        """The baseline deploy key on the baseline repository."""
        key = self.admin.repos.keys.create(
            self.repo.owner,
            self.repo.name,
            title=self.name("deploy-key"),
            key=self.ssh_key_for("deploy:base"),
        )
        assert key.id is not None
        return key.id

    @cached_property
    def user_key_id(self) -> int:
        """The baseline public key on the regular user."""
        key = self.user_client.user.keys.create(title=self.name("user-key"), key=self.ssh_key_for("user:base"))
        assert key.id is not None
        return key.id

    @cached_property
    def repo_hook_id(self) -> int:
        """The baseline repository webhook."""
        hook = self.admin.repos.hooks.create(
            self.repo.owner,
            self.repo.name,
            type=pyfj.CreateHookOptionType.FORGEJO,
            config=pyfj.CreateHookOptionConfig(url="http://127.0.0.1:1/pyfj-hook", content_type="json"),
            events=["push"],
        )
        assert hook.id is not None
        return hook.id

    @cached_property
    def org_hook_id(self) -> int:
        """The baseline organization webhook."""
        hook = self.admin.orgs.hooks.create(
            self.org,
            type=pyfj.CreateHookOptionType.FORGEJO,
            config=pyfj.CreateHookOptionConfig(url="http://127.0.0.1:1/pyfj-org-hook", content_type="json"),
            events=["push"],
        )
        assert hook.id is not None
        return hook.id

    @cached_property
    def user_hook_id(self) -> int:
        """The baseline user webhook."""
        hook = self.admin.user.hooks.create(
            type=pyfj.CreateHookOptionType.FORGEJO,
            config=pyfj.CreateHookOptionConfig(url="http://127.0.0.1:1/pyfj-user-hook", content_type="json"),
            events=["push"],
        )
        assert hook.id is not None
        return hook.id

    @cached_property
    def admin_hook_id(self) -> int:
        """The baseline system webhook."""
        hook = self.admin.admin.hooks.create(
            type=pyfj.CreateHookOptionType.FORGEJO,
            config=pyfj.CreateHookOptionConfig(url="http://127.0.0.1:1/pyfj-admin-hook", content_type="json"),
            events=["push"],
        )
        assert hook.id is not None
        return hook.id

    @cached_property
    def wiki_page_name(self) -> str:
        """The baseline wiki page name."""
        self.admin.repos.wiki.create(self.repo.owner, self.repo.name, title="Home", content_base64="cHlmalB3aWtp")
        return "Home"

    # -- reusable resources --------------------------------------------------

    def org_for(self, key: str = "default") -> str:
        """Create (once) and return an organization name."""
        cache_key = f"org:{key}"
        cached = self._cache_get(cache_key)
        if cached is not None:
            return cast("str", cached)
        name = self.name("org", key)
        try:
            self.admin.orgs.create(username=name, full_name=f"pyfj {key} org")
        except pyfj.APIError as exc:
            if exc.status_code != httpx2.codes.CONFLICT:
                raise
        return self._cache_put(cache_key, name)

    def team_for(
        self,
        key: str = "default",
        *,
        org: str | None = None,
        members: Sequence[str] = (),
        repos: Sequence[RepoRef] = (),
    ) -> int:
        """Create (once) a team, optionally with members and repositories."""
        org = org or self.org
        cache_key = f"team:{org}:{key}"
        cached = self._cache_get(cache_key)
        if cached is not None:
            return cast("int", cached)
        team = self.admin.orgs.teams.create(
            org,
            name=self.name("team", key),
            units=["repo.code", "repo.issues"],
        )
        assert team.id is not None
        for member in members:
            self.admin.teams.members.add(team.id, member)
        for repo in repos:
            self.admin.teams.repos.add(team.id, repo.owner, repo.name)
        return self._cache_put(cache_key, team.id)

    def team_name_for(
        self,
        key: str = "default",
        *,
        org: str | None = None,
        members: Sequence[str] = (),
        repos: Sequence[RepoRef] = (),
    ) -> str:
        """Create (once) a team and return its name (the repo-team API key)."""
        self.team_for(key, org=org, members=members, repos=repos)
        return self.name("team", key)

    def runner_for(
        self,
        key: str = "default",
        *,
        scope: Literal["admin", "org", "repo", "user"] = "admin",
        owner: str | None = None,
        repo: RepoRef | None = None,
    ) -> int:
        """Register (once) an Actions runner at the requested scope."""
        cache_key = f"runner:{scope}:{owner or ''}:{repo.full_name if repo else ''}:{key}"
        cached = self._cache_get(cache_key)
        if cached is not None:
            return cast("int", cached)
        name = self.name("runner", key)
        response: pyfj.RegisterRunnerResponse
        if scope == "admin":
            response = self.admin.admin.actions.runners.register(name=name, description="pyfj smoke runner")
        elif scope == "org":
            response = self.admin.orgs.actions.runners.register(owner or self.org, name=name, description="pyfj smoke")
        elif scope == "repo":
            assert repo is not None
            response = self.admin.repos.actions.runners.register(
                repo.owner, repo.name, name=name, description="pyfj smoke"
            )
        else:
            response = self.admin.user.actions.runners.register(name=name, description="pyfj smoke")
        assert response.id is not None
        return self._cache_put(cache_key, response.id)

    def user_for(self, key: str = "default") -> str:
        """Create (once) a throwaway user through the admin API."""
        cache_key = f"user:{key}"
        cached = self._cache_get(cache_key)
        if cached is not None:
            return cast("str", cached)
        username = self.name("user", key)
        self.admin.admin.users.create(
            username=username,
            password="pyfj-scratch-pass-1234",
            email=f"{username}@pyfj.test",
            must_change_password=False,
        )
        return self._cache_put(cache_key, username)

    def email_for(self, key: str = "default") -> str:
        """Create (once) a throwaway e-mail on the regular user and return it."""
        cache_key = f"email:{key}"
        cached = self._cache_get(cache_key)
        if cached is not None:
            return cast("str", cached)
        address = f"{self.run_id}-{key}@pyfj.test"
        self.user_client.user.emails.add(emails=[address])
        return self._cache_put(cache_key, address)

    def access_token_for(self, username: str, key: str = "default") -> str:
        """Create (once) an access token and return its name (for deletion)."""
        cache_key = f"token:{username}:{key}"
        cached = self._cache_get(cache_key)
        if cached is not None:
            return cast("str", cached)
        name = self.name("token", key)
        self.admin.admin.users.tokens.create(username, name=name, scopes=["write:repository"])
        return self._cache_put(cache_key, name)

    def quota_group_for(
        self,
        key: str = "default",
        *,
        rules: Sequence[str] = (),
        users: Sequence[str] = (),
    ) -> str:
        """Create (once) a quota group with optional rules and users."""
        cache_key = f"quota-group:{key}"
        cached = self._cache_get(cache_key)
        if cached is not None:
            return cast("str", cached)
        name = self.name("quota-group", key)
        self.admin.admin.quota.groups.create(name=name)
        for rule in rules:
            self.admin.admin.quota.groups.rules.add(name, rule)
        for username in users:
            self.admin.admin.quota.groups.users.add(name, username)
        return self._cache_put(cache_key, name)

    def quota_rule_for(self, key: str = "default") -> str:
        """Create (once) a quota rule and return its name."""
        cache_key = f"quota-rule:{key}"
        cached = self._cache_get(cache_key)
        if cached is not None:
            return cast("str", cached)
        name = self.name("quota-rule", key)
        self.admin.admin.quota.rules.create(name=name, limit=100)
        return self._cache_put(cache_key, name)

    def hook_for(self, key: str = "default", *, repo: RepoRef | None = None, org: str | None = None) -> int:
        """Create (once) a webhook on a repository, an organization, or the user."""
        scope = "repo" if repo is not None else ("org" if org is not None else "user")
        cache_key = f"hook:{scope}:{key}"
        cached = self._cache_get(cache_key)
        if cached is not None:
            return cast("int", cached)
        config = pyfj.CreateHookOptionConfig(
            url=f"http://127.0.0.1:1/{self.name('hook', key)}",
            content_type="json",
        )
        hook_type = pyfj.CreateHookOptionType.FORGEJO
        if repo is not None:
            hook = self.admin.repos.hooks.create(
                repo.owner,
                repo.name,
                type=hook_type,
                config=config,
                events=["push"],
            )
        elif org is not None:
            hook = self.admin.orgs.hooks.create(org, type=hook_type, config=config, events=["push"])
        else:
            hook = self.admin.user.hooks.create(type=hook_type, config=config, events=["push"])
        assert hook.id is not None
        return self._cache_put(cache_key, hook.id)

    def label_for(self, repo: RepoRef, key: str = "default") -> int:
        """Create (once) a label in ``repo`` and return its id."""
        cache_key = f"label:{repo.full_name}:{key}"
        cached = self._cache_get(cache_key)
        if cached is not None:
            return cast("int", cached)
        label = self.admin.repos.labels.create(repo.owner, repo.name, name=self.name("label", key), color="#3366cc")
        assert label.id is not None
        return self._cache_put(cache_key, label.id)

    def milestone_for(self, repo: RepoRef, key: str = "default") -> int:
        """Create (once) a milestone in ``repo`` and return its id."""
        cache_key = f"milestone:{repo.full_name}:{key}"
        cached = self._cache_get(cache_key)
        if cached is not None:
            return cast("int", cached)
        milestone = self.admin.repos.milestones.create(repo.owner, repo.name, title=self.name("milestone", key))
        assert milestone.id is not None
        return self._cache_put(cache_key, milestone.id)

    def release_for(self, repo: RepoRef, key: str = "default") -> int:
        """Create (once) a release in ``repo`` and return its id."""
        cache_key = f"release:{repo.full_name}:{key}"
        cached = self._cache_get(cache_key)
        if cached is not None:
            return cast("int", cached)
        release = self.admin.repos.releases.create(
            repo.owner,
            repo.name,
            tag_name=self.name("tag", key),
            name=f"release {key}",
            target_commitish="main",
        )
        assert release.id is not None
        return self._cache_put(cache_key, release.id)

    def deploy_key_for(self, repo: RepoRef, key: str = "default") -> int:
        """Create (once) a deploy key in ``repo`` and return its id."""
        cache_key = f"deploy-key:{repo.full_name}:{key}"
        cached = self._cache_get(cache_key)
        if cached is not None:
            return cast("int", cached)
        deploy_key = self.admin.repos.keys.create(
            repo.owner,
            repo.name,
            title=self.name("deploy-key", key),
            key=self.ssh_key_for(f"deploy:{repo.full_name}:{key}"),
        )
        assert deploy_key.id is not None
        return self._cache_put(cache_key, deploy_key.id)

    def user_key_for(self, key: str = "default") -> int:
        """Create (once) a public key on the regular user and return its id."""
        cache_key = f"user-key:{key}"
        cached = self._cache_get(cache_key)
        if cached is not None:
            return cast("int", cached)
        key_model = self.user_client.user.keys.create(
            title=self.name("user-key", key), key=self.ssh_key_for(f"user:{key}")
        )
        assert key_model.id is not None
        return self._cache_put(cache_key, key_model.id)

    def oauth_app_for(self, key: str = "default") -> int:
        """Create (once) an OAuth2 application and return its id."""
        cache_key = f"oauth:{key}"
        cached = self._cache_get(cache_key)
        if cached is not None:
            return cast("int", cached)
        application = self.admin.user.applications.oauth2.create(
            name=self.name("oauth", key),
            redirect_uris=["http://127.0.0.1:1/callback"],
            confidential_client=True,
        )
        assert application.id is not None
        return self._cache_put(cache_key, application.id)

    def wiki_for(self, repo: RepoRef, key: str = "default") -> str:
        """Create (once) a wiki page and return its title.

        Wiki page titles must not contain dashes: Forgejo maps web paths to
        git paths by restoring dashes to spaces, so a dashed title can never
        be fetched or deleted again by name.
        """
        cache_key = f"wiki:{repo.full_name}:{key}"
        cached = self._cache_get(cache_key)
        if cached is not None:
            return cast("str", cached)
        title = f"{self.run_id}wiki{key.replace('-', '')}"
        self.admin.repos.wiki.create(repo.owner, repo.name, title=title, content_base64="cHlmalB3aWtp")
        return self._cache_put(cache_key, title)

    def branch_protection_for(self, repo: RepoRef, key: str = "default") -> str:
        """Create (once) a branch protection and return its branch name."""
        cache_key = f"branch-protection:{repo.full_name}:{key}"
        cached = self._cache_get(cache_key)
        if cached is not None:
            return cast("str", cached)
        name = f"pyfj-{key}"
        self.admin.repos.branch_protections.create(repo.owner, repo.name, branch_name=name, enable_push=False)
        return self._cache_put(cache_key, name)

    def tag_protection_for(self, repo: RepoRef, key: str = "default") -> int:
        """Create (once) a tag protection and return its id."""
        cache_key = f"tag-protection:{repo.full_name}:{key}"
        cached = self._cache_get(cache_key)
        if cached is not None:
            return cast("int", cached)
        protection = self.admin.repos.tag_protections.create(
            repo.owner,
            repo.name,
            name_pattern=f"{self.run_id}-{key}-*",
            whitelist_usernames=[USER_USERNAME],
        )
        assert protection.id is not None
        return self._cache_put(cache_key, protection.id)

    def ssh_key_for(self, key: str = "default") -> str:
        """Return a distinct static SSH public key for ``key`` (pool is finite)."""
        cache_key = f"ssh:{key}"
        cached = self._cache_get(cache_key)
        if cached is not None:
            return cast("str", cached)
        used = len([name for name in self.__dict__ if name.startswith("_seed_ssh:")])
        if used >= len(SSH_PUBLIC_KEYS):
            message = "the static SSH key pool is exhausted; add more keys to harness.SSH_PUBLIC_KEYS"
            raise RuntimeError(message)
        return self._cache_put(cache_key, SSH_PUBLIC_KEYS[used])

    def admin_user_key_for(self, key: str = "default") -> tuple[str, int]:
        """Create (once) a throwaway user with one public key; return ``(user, key id)``."""
        cache_key = f"admin-user-key:{key}"
        cached = self._cache_get(cache_key)
        if cached is not None:
            return cast("tuple[str, int]", cached)
        username = self.user_for(f"key-{key}")
        key_model = self.admin.admin.users.keys.create(
            username,
            title=self.name("admin-user-key", key),
            key=self.ssh_key_for(f"admin-user:{key}"),
            read_only=True,
        )
        assert key_model.id is not None
        return self._cache_put(cache_key, (username, key_model.id))

    def admin_hook_for(self, key: str = "default") -> int:
        """Create (once) a system webhook and return its id."""
        cache_key = f"admin-hook:{key}"
        cached = self._cache_get(cache_key)
        if cached is not None:
            return cast("int", cached)
        hook = self.admin.admin.hooks.create(
            type=pyfj.CreateHookOptionType.FORGEJO,
            config=pyfj.CreateHookOptionConfig(
                url=f"http://127.0.0.1:1/{self.name('admin-hook', key)}",
                content_type="json",
            ),
            events=["push"],
        )
        assert hook.id is not None
        return self._cache_put(cache_key, hook.id)

    def org_label_for(self, key: str = "default") -> int:
        """Create (once) an organization label and return its id."""
        cache_key = f"org-label:{key}"
        cached = self._cache_get(cache_key)
        if cached is not None:
            return cast("int", cached)
        label = self.admin.orgs.labels.create(self.org, name=self.name("label", key), color="#8844cc")
        assert label.id is not None
        return self._cache_put(cache_key, label.id)

    def org_secret_for(self, key: str = "default") -> str:
        """Create (once) an organization Actions secret and return its name."""
        cache_key = f"org-secret:{key}"
        cached = self._cache_get(cache_key)
        if cached is not None:
            return cast("str", cached)
        name = self.secret_name(key)
        self.admin.orgs.actions.secrets.update(self.org, name, data="dmFsdWU=")
        return self._cache_put(cache_key, name)

    def repo_secret_for(self, repo: RepoRef, key: str = "default") -> str:
        """Create (once) a repository Actions secret and return its name."""
        cache_key = f"repo-secret:{repo.full_name}:{key}"
        cached = self._cache_get(cache_key)
        if cached is not None:
            return cast("str", cached)
        name = self.secret_name(key)
        self.admin.repos.actions.secrets.update(repo.owner, repo.name, name, data="dmFsdWU=")
        return self._cache_put(cache_key, name)

    def user_secret_for(self, key: str = "default") -> str:
        """Create (once) a user Actions secret and return its name."""
        cache_key = f"user-secret:{key}"
        cached = self._cache_get(cache_key)
        if cached is not None:
            return cast("str", cached)
        name = self.secret_name(key)
        self.admin.user.actions.secrets.update(name, data="dmFsdWU=")
        return self._cache_put(cache_key, name)

    def org_variable_for(self, key: str = "default") -> str:
        """Create (once) an organization Actions variable and return its name."""
        cache_key = f"org-variable:{key}"
        cached = self._cache_get(cache_key)
        if cached is not None:
            return cast("str", cached)
        name = self.variable_name(key)
        self.admin.orgs.actions.variables.create(self.org, name, value="one")
        return self._cache_put(cache_key, name)

    def repo_variable_for(self, repo: RepoRef, key: str = "default") -> str:
        """Create (once) a repository Actions variable and return its name."""
        cache_key = f"repo-variable:{repo.full_name}:{key}"
        cached = self._cache_get(cache_key)
        if cached is not None:
            return cast("str", cached)
        name = self.variable_name(key)
        self.admin.repos.actions.variables.create(repo.owner, repo.name, name, value="one")
        return self._cache_put(cache_key, name)

    def user_variable_for(self, key: str = "default") -> str:
        """Create (once) a user Actions variable and return its name."""
        cache_key = f"user-variable:{key}"
        cached = self._cache_get(cache_key)
        if cached is not None:
            return cast("str", cached)
        name = self.variable_name(key)
        self.admin.user.actions.variables.create(name, value="one")
        return self._cache_put(cache_key, name)

    def commit_sha(self, repo: RepoRef) -> str:
        """The SHA of the first commit in ``repo``."""
        cache_key = f"commit:{repo.full_name}"
        cached = self._cache_get(cache_key)
        if cached is not None:
            return cast("str", cached)
        commits = self.admin.repos.commits.list(repo.owner, repo.name)
        first = next(iter(commits))
        assert first.sha is not None
        return self._cache_put(cache_key, first.sha)

    def pending_review(self, pull: IssueRef) -> int:
        """Create (once) a pending review by the admin on ``pull`` and return its id."""
        cache_key = f"pending-review:{pull.repo.full_name}:{pull.index}"
        cached = self._cache_get(cache_key)
        if cached is not None:
            return cast("int", cached)
        review = self.admin.repos.pulls.reviews.create(
            pull.repo.owner,
            pull.repo.name,
            pull.index,
            body="pyfj pending review",
            commit_id=self.pull_head_sha(pull),
        )
        assert review.id is not None
        return self._cache_put(cache_key, review.id)

    def pull_head_sha(self, pull: IssueRef) -> str:
        """The head commit SHA of ``pull``."""
        model = self.admin.repos.pulls.get(pull.repo.owner, pull.repo.name, pull.index)
        assert model.head is not None
        assert model.head.sha is not None
        return model.head.sha

    def user_review(self, pull: IssueRef, *, event: str) -> int:
        """Create (once) a submitted review by the regular user and return its id."""
        cache_key = f"user-review:{pull.repo.full_name}:{pull.index}"
        cached = self._cache_get(cache_key)
        if cached is not None:
            return cast("int", cached)
        self.admin.repos.collaborators.add(
            pull.repo.owner,
            pull.repo.name,
            USER_USERNAME,
            permission=pyfj.AddCollaboratorOptionPermission.WRITE,
        )
        review = self.user_client.repos.pulls.reviews.create(
            pull.repo.owner,
            pull.repo.name,
            pull.index,
            body="pyfj user review",
            commit_id=self.pull_head_sha(pull),
            event=event,
        )
        assert review.id is not None
        return self._cache_put(cache_key, review.id)

    def scratch_repo_with_file(self, key: str, filepath: str, content: str) -> RepoRef:
        """Create (once) a repository initialized with one extra file.

        ``content`` is raw text; the contents API speaks base64.
        """
        cache_key = f"repo-file:{key}"
        cached = self._cache_get(cache_key)
        if cached is not None:
            return cast("RepoRef", cached)
        repo = self.repo_for(f"file-{key}")
        self.admin.repos.contents.create(
            repo.owner,
            repo.name,
            filepath,
            content=base64.b64encode(content.encode()).decode(),
            message=f"add {filepath}",
        )
        return self._cache_put(cache_key, repo)

    def _clone_address(self, repo: RepoRef) -> str:
        """The HTTP clone address reachable from inside the container."""
        return f"http://localhost:{CONTAINER_PORT}/{repo.full_name}.git"

    def mirrored_repo_for(self, key: str = "default") -> RepoRef:
        """Migrate (once) a throwaway repository as a pull mirror and return it."""
        cache_key = f"mirror:{key}"
        cached = self._cache_get(cache_key)
        if cached is not None:
            return cast("RepoRef", cached)
        source = self.scratch_repo_with_file(f"mirror-source-{key}", "mirror.txt", "mirrored")
        name = self.name("repo", f"mirror-{key}")
        migrated = self.admin.repos.migrate(
            clone_addr=self._clone_address(source),
            repo_name=name,
            repo_owner=self.org,
            service=pyfj.MigrateRepoOptionsService.GIT,
            mirror=True,
            auth_username=ADMIN_USERNAME,
            auth_password=ADMIN_PASSWORD,
        )
        owner = migrated.owner.login if migrated.owner and migrated.owner.login else self.org
        ref = RepoRef(owner=owner, name=migrated.name or name)
        return self._cache_put(cache_key, ref)

    def push_mirror_for(self, key: str = "default") -> tuple[RepoRef, str]:
        """Create (once) a push mirror from a throwaway repo; return ``(source, remote_name)``."""
        cache_key = f"push-mirror:{key}"
        cached = self._cache_get(cache_key)
        if cached is not None:
            return cast("tuple[RepoRef, str]", cached)
        source = self.scratch_repo_with_file(f"push-source-{key}", "push.txt", "pushed")
        target = self.repo_for(f"push-target-{key}")
        mirror = self.admin.repos.push_mirrors.create(
            source.owner,
            source.name,
            remote_address=self._clone_address(target),
            remote_username=ADMIN_USERNAME,
            remote_password=ADMIN_PASSWORD,
            sync_on_commit=False,
            interval="8h",
        )
        assert mirror.remote_name is not None
        return self._cache_put(cache_key, (source, mirror.remote_name))

    # -- scalar fixtures -----------------------------------------------------

    @property
    def user(self) -> str:
        """The seeded regular user's username."""
        return USER_USERNAME

    @cached_property
    def repo_id(self) -> int:
        """The numeric id of the baseline repository."""
        repo = self.admin.repos.get(self.repo.owner, self.repo.name)
        assert repo.id is not None
        return repo.id

    @cached_property
    def user_id(self) -> int:
        """The numeric id of the seeded regular user."""
        user = self.admin.users.get(USER_USERNAME)
        assert user.id is not None
        return user.id

    @cached_property
    def org_id(self) -> int:
        """The numeric id of the baseline organization."""
        organization = self.admin.orgs.get(self.org)
        assert organization.id is not None
        return organization.id

    @cached_property
    def gitignore_template(self) -> str:
        """The name of a served gitignore template."""
        names = self.admin.misc.gitignore.templates.list()
        assert names
        return names[0]

    @cached_property
    def label_template(self) -> str:
        """The name of a served label template."""
        names = self.admin.misc.label.templates.list()
        assert names
        return names[0]

    @cached_property
    def license_template(self) -> str:
        """The name of a served license template."""
        entries = self.admin.misc.licenses.list()
        assert entries
        name = entries[0].name
        assert name is not None
        return name

    @cached_property
    def cron_task(self) -> str:
        """The name of a safe-to-run admin cron task."""
        tasks = list(self.admin.admin.cron.list())
        assert tasks
        first = tasks[0]
        assert first.name is not None
        return first.name

    @cached_property
    def notification_id(self) -> int:
        """A notification thread id, created by mentioning the admin on a watched repo."""
        self.admin.repos.subscription.update(self.repo.owner, self.repo.name)
        self.user_client.repos.issues.comments.create(
            self.repo.owner,
            self.repo.name,
            self.issue_index,
            body=f"notification trigger for @{ADMIN_USERNAME}",
        )
        deadline = time.monotonic() + 15.0
        while True:
            for thread in self.admin.notifications.list(all=True):
                if thread.id is not None:
                    return thread.id
            if time.monotonic() >= deadline:
                message = "no notification appeared for the mention within 15s"
                raise TimeoutError(message)
            time.sleep(0.25)

    @cached_property
    def admin_runner_id(self) -> int:
        """A registered admin-scope Actions runner."""
        return self.runner_for("base", scope="admin")

    @cached_property
    def base_pull(self) -> IssueRef:
        """The baseline pull request reference."""
        return IssueRef(repo=self.repo, index=self.pull_index)

    @cached_property
    def file_sha(self) -> str:
        """The blob SHA of the baseline repository's README."""
        contents = self.admin.repos.contents.get(self.repo.owner, self.repo.name, "README.md")
        assert contents.sha is not None
        return contents.sha

    @cached_property
    def annotated_tag_sha(self) -> str:
        """The tag-object SHA of a fresh annotated tag on the baseline repository."""
        tag_name = self.name("tag", "annotated")
        tag = self.admin.repos.tags.create(
            self.repo.owner,
            self.repo.name,
            tag_name=tag_name,
            target=self.main_sha,
            message="pyfj annotated tag",
        )
        references = self.admin.repos.git.refs.get(self.repo.owner, self.repo.name, f"tags/{tag.name}")
        assert references
        assert references[0].object is not None
        assert references[0].object.sha is not None
        return references[0].object.sha

    @cached_property
    def editorconfig_repo(self) -> RepoRef:
        """A repository carrying an ``.editorconfig`` file."""
        return self.scratch_repo_with_file("editorconfig", ".editorconfig", "root = true\n")

    @cached_property
    def issue_template_repo(self) -> RepoRef:
        """A repository carrying one valid issue template."""
        repo = self.repo_for("issue-template")
        template = (
            "name: Bug\n"
            "about: Something is broken\n"
            "body:\n"
            "  - type: input\n"
            "    id: description\n"
            "    attributes:\n"
            "      label: Description\n"
        )
        self.admin.repos.contents.create(
            repo.owner,
            repo.name,
            ".forgejo/ISSUE_TEMPLATE/bug.yml",
            content=base64.b64encode(template.encode()).decode(),
            message="add issue template",
        )
        return repo

    @cached_property
    def merged_pull_commit(self) -> tuple[RepoRef, str]:
        """A merged pull request's repository and its merge commit SHA."""
        repo = self.repo_for("merged-commit")
        pull = self.pull(repo, "merged-commit")
        self.admin.repos.pulls.merge(
            repo.owner,
            repo.name,
            pull.index,
            do=pyfj.MergePullRequestOptionDo.MERGE,
        )
        merged = self.admin.repos.pulls.get(repo.owner, repo.name, pull.index)
        assert merged.merge_commit_sha is not None
        return (repo, merged.merge_commit_sha)

    @cached_property
    def team_with_repo(self) -> int:
        """A team that already contains the baseline repository."""
        return self.team_for("repo", repos=[self.repo])

    # -- helpers -------------------------------------------------------------

    def issue(self, repo: RepoRef, key: str = "default", *, title: str | None = None) -> IssueRef:
        """Create (once) and return an issue in ``repo``."""
        cache_key = f"issue:{repo.full_name}:{key}"
        cached = self._cache_get(cache_key)
        if cached is not None:
            return cast("IssueRef", cached)
        issue = self.admin.repos.issues.create(repo.owner, repo.name, title=title or self.name("issue", key))
        assert issue.number is not None
        return self._cache_put(cache_key, IssueRef(repo=repo, index=issue.number))

    def pull(self, repo: RepoRef, key: str = "default", *, title: str | None = None) -> IssueRef:
        """Create (once) and return a pull request in ``repo``.

        The head branch is created through the contents API first, like the
        baseline pull request.
        """
        cache_key = f"pull:{repo.full_name}:{key}"
        cached = self._cache_get(cache_key)
        if cached is not None:
            return cast("IssueRef", cached)
        self.admin.repos.contents.create(
            repo.owner,
            repo.name,
            f"pyfj-{key}.txt",
            content="cHlmalBwdWxsCg==",
            message=f"add {key} pull file",
            new_branch=f"pyfj-{key}",
        )
        pull = self.admin.repos.pulls.create(
            repo.owner,
            repo.name,
            title=title or self.name("pull", key),
            head=f"pyfj-{key}",
            base="main",
        )
        assert pull.number is not None
        return self._cache_put(cache_key, IssueRef(repo=repo, index=pull.number))

    def _cache_get(self, key: str) -> object | None:
        return self.__dict__.get(f"_seed_{key}")

    def _cache_put(self, key: str, value: T) -> T:
        self.__dict__[f"_seed_{key}"] = value
        return value
