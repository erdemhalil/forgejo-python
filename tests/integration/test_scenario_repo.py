"""Repository lifecycle and the pinned Spec/runtime mismatches around it."""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

import pyfj

if TYPE_CHECKING:
    from harness import Seed

pytestmark = pytest.mark.integration


def test_repository_lifecycle(admin_client: pyfj.Forgejo, seed: Seed) -> None:
    name = seed.name("repo", "scenario-lifecycle")
    created = admin_client.orgs.repos.create(seed.org, name=name, auto_init=True, description="created by a scenario")
    try:
        assert created.full_name == f"{seed.org}/{name}"
        assert created.default_branch == "main"
        assert created.empty is False
        assert created.owner is not None
        assert created.owner.login == seed.org

        fetched = admin_client.repos.get(seed.org, name)
        assert fetched.id == created.id

        edited = admin_client.repos.update(seed.org, name, description="edited by a scenario")
        assert edited.description == "edited by a scenario"

        results = admin_client.repos.search(q=name)
        assert results.data
        assert any(repo.full_name == f"{seed.org}/{name}" for repo in results.data)

        languages = admin_client.repos.languages(seed.org, name)
        assert isinstance(languages, dict)
    finally:
        admin_client.repos.delete(seed.org, name)

    with pytest.raises(pyfj.NotFoundError):
        admin_client.repos.get(seed.org, name)


def test_file_lifecycle(admin_client: pyfj.Forgejo, seed: Seed) -> None:
    repo = seed.repo_for("scenario-files")
    admin_client.repos.contents.create(
        repo.owner,
        repo.name,
        "scenario.txt",
        content="b25l",  # "one"
        message="add scenario file",
    )

    contents = admin_client.repos.contents.get(repo.owner, repo.name, "scenario.txt")
    assert contents.name == "scenario.txt"
    assert contents.sha is not None

    listing = admin_client.repos.contents.list(repo.owner, repo.name)
    assert any(entry.name == "scenario.txt" for entry in listing)

    updated = admin_client.repos.contents.update(
        repo.owner,
        repo.name,
        "scenario.txt",
        content="dHdv",  # "two"
        sha=contents.sha,
        message="update scenario file",
    )
    assert updated.content is not None

    raw = admin_client.repos.raw.get(repo.owner, repo.name, "scenario.txt")
    assert raw == b"two"


def test_private_repository_is_hidden_from_anonymous(
    admin_client: pyfj.Forgejo,
    anonymous_client: pyfj.Forgejo,
    seed: Seed,
) -> None:
    private = seed.repo_for("scenario-private", private=True)
    with pytest.raises(pyfj.NotFoundError):
        anonymous_client.repos.get(private.owner, private.name)
    assert admin_client.repos.get(private.owner, private.name).private is True


def test_empty_issue_template_list_decodes_as_null(admin_client: pyfj.Forgejo, seed: Seed) -> None:
    """Pin the Forgejo 16 mismatch: the Spec says array, the instance sends null.

    ``repoGetIssueTemplates`` on a repository without templates must therefore
    raise ``DecodeError`` until the Spec is corrected server-side.
    """
    repo = seed.repo_for("scenario-templates-empty")
    with pytest.raises(pyfj.DecodeError):
        admin_client.repos.issue_templates(repo.owner, repo.name)


def test_empty_issue_reaction_list_decodes_as_null(admin_client: pyfj.Forgejo, seed: Seed) -> None:
    """Pin the Forgejo 16 mismatch for issue reactions without any reaction."""
    repo = seed.repo_for("scenario-reactions-empty")
    issue = seed.issue(repo, "reactions")
    with pytest.raises(pyfj.DecodeError):
        admin_client.repos.issues.reactions.list(repo.owner, repo.name, issue.index)


def test_empty_runner_jobs_list_decodes_as_null(admin_client: pyfj.Forgejo, seed: Seed) -> None:
    """Pin the Forgejo 16 mismatch for an empty repository jobs list."""
    repo = seed.repo_for("scenario-jobs-empty")
    with pytest.raises(pyfj.DecodeError):
        admin_client.repos.actions.runners.jobs(repo.owner, repo.name)


def test_empty_user_jobs_list_decodes_as_null(admin_client: pyfj.Forgejo) -> None:
    """Pin the Forgejo 16 mismatch for an empty user-scope jobs list."""
    with pytest.raises(pyfj.DecodeError):
        admin_client.user.actions.runners.jobs()


def test_user_transfer_completes_immediately(
    admin_client: pyfj.Forgejo,
    user_client: pyfj.Forgejo,
    seed: Seed,
) -> None:
    """Pin Forgejo 16 behaviour: transferring to a user needs no acceptance.

    ``acceptRepoTransfer`` and ``rejectRepoTransfer`` are skipped because this
    instance never leaves a pending transfer for them to act on.
    """
    repo = seed.repo_for("scenario-transfer")
    transferred = admin_client.repos.transfer(repo.owner, repo.name, new_owner=seed.user)
    assert transferred.owner is not None
    assert transferred.owner.login == seed.user
    # pyfj does not follow redirects, so the old path surfaces the move as a 301.
    with pytest.raises(pyfj.APIError) as caught:
        admin_client.repos.get(repo.owner, repo.name)
    assert caught.value.status_code == 301
    moved = user_client.repos.get(seed.user, repo.name)
    assert moved.full_name == f"{seed.user}/{repo.name}"
    user_client.repos.delete(seed.user, repo.name)
