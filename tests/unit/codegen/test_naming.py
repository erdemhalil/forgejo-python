"""Naming-algorithm tests: verbs, nesting, collisions, and overrides."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any

import pytest

from codegen.ir import build_ir
from codegen.naming import (
    MethodOverride,
    NamespaceOverride,
    Overrides,
    Registry,
    assign_names,
    load_mapping,
    load_registry,
    operation_verb,
)
from codegen.spec import SpecError, load_spec

if TYPE_CHECKING:
    from pathlib import Path

    from codegen.ir import IR
    from codegen.naming import Naming


def _load(tmp_path: Path, data: object) -> IR:
    path = tmp_path / "spec.json"
    path.write_text(json.dumps(data), encoding="utf-8")
    return build_ir(load_spec(path))


def _spec(*operations: tuple[str, str, str]) -> dict[str, Any]:
    """Build a minimal Spec from ``(method, path, operationId)`` triples."""
    paths: dict[str, dict[str, Any]] = {}
    for method, path, operation_id in operations:
        paths.setdefault(path, {})[method.lower()] = {
            "operationId": operation_id,
            "responses": {"200": {"description": "ok"}},
        }
    return {
        "swagger": "2.0",
        "info": {"title": "Tiny", "version": "0.0.1"},
        "paths": paths,
    }


@pytest.mark.parametrize(
    ("operation_id", "verb"),
    [
        ("repoMergePullRequest", "merge"),
        ("adminCronRun", "run"),
        ("userGetRunnerRegistrationToken", "get"),
        ("renderMarkdownRaw", "render"),
        ("activitypubPersonInbox", None),
    ],
)
def test_operation_verb_extraction(operation_id: str, verb: str | None) -> None:
    assert operation_verb(operation_id) == verb


def test_collection_and_item_verbs(tmp_path: Path) -> None:
    ir = _load(
        tmp_path,
        _spec(
            ("GET", "/repos/{owner}/{repo}/issues", "issueListIssues"),
            ("GET", "/repos/{owner}/{repo}/issues/{index}", "issueGetIssue"),
            ("POST", "/repos/{owner}/{repo}/issues", "issueCreateIssue"),
            ("PATCH", "/repos/{owner}/{repo}/issues/{index}", "issueEditIssue"),
            ("DELETE", "/repos/{owner}/{repo}/issues/{index}", "issueDelete"),
        ),
    )
    naming = assign_names(ir)
    calls = {(endpoint.namespace, endpoint.method) for endpoint in naming.endpoints}
    assert (("repos", "issues"), "list") in calls
    assert (("repos", "issues"), "get") in calls
    assert (("repos", "issues"), "create") in calls
    assert (("repos", "issues"), "update") in calls
    assert (("repos", "issues"), "delete") in calls


def test_nesting_and_parameter_segments(tmp_path: Path) -> None:
    ir = _load(
        tmp_path,
        _spec(
            ("GET", "/repos/{owner}/{repo}/issues/{index}/comments", "issueListComments"),
            ("POST", "/repos/{owner}/{repo}/issues/{index}/comments", "issueCreateComment"),
            ("GET", "/repos/{owner}/{repo}/issues/{index}/comments/{id}", "issueGetComment"),
        ),
    )
    naming = assign_names(ir)
    by_id = {endpoint.operation.operation_id: endpoint for endpoint in naming.endpoints}
    assert by_id["issueListComments"].namespace == ("repos", "issues", "comments")
    assert by_id["issueListComments"].method == "list"
    assert by_id["issueGetComment"].namespace == ("repos", "issues", "comments")
    assert by_id["issueGetComment"].method == "get"


def test_trailing_action_segment_names_the_method(tmp_path: Path) -> None:
    ir = _load(
        tmp_path,
        _spec(
            ("POST", "/repos/{owner}/{repo}/pulls/{index}/merge", "repoMergePullRequest"),
            ("GET", "/repos/{owner}/{repo}/pulls/{index}/merge", "repoPullRequestIsMerged"),
        ),
    )
    naming = assign_names(
        ir,
        Overrides(
            namespaces={"/repos/{owner}/{repo}/pulls/{index}/merge": NamespaceOverride(skip=True)},
            methods={
                "repoMergePullRequest": MethodOverride(name="merge"),
                "repoPullRequestIsMerged": MethodOverride(name="is_merged"),
            },
        ),
    )
    by_id = {endpoint.operation.operation_id: endpoint for endpoint in naming.endpoints}
    # `merge` is flattened into a method; both operations share the namespace.
    assert by_id["repoMergePullRequest"].namespace == ("repos", "pulls")
    assert by_id["repoMergePullRequest"].method == "merge"
    assert by_id["repoPullRequestIsMerged"].method == "is_merged"


def test_action_style_post_uses_the_operation_verb(tmp_path: Path) -> None:
    ir = _load(
        tmp_path,
        _spec(
            ("GET", "/admin/cron", "adminCronList"),
            ("POST", "/admin/cron/{task}", "adminCronRun"),
            ("POST", "/repos/{owner}/{repo}/pulls/{index}/reviews/{id}", "repoSubmitPullReview"),
        ),
    )
    naming = assign_names(ir)
    by_id = {endpoint.operation.operation_id: endpoint for endpoint in naming.endpoints}
    assert by_id["adminCronRun"].method == "run"
    assert by_id["repoSubmitPullReview"].method == "submit"


def test_standalone_paths_route_to_misc(tmp_path: Path) -> None:
    ir = _load(
        tmp_path,
        _spec(
            ("GET", "/version", "getVersion"),
            ("GET", "/licenses/{name}", "getLicenseTemplateInfo"),
            ("GET", "/licenses", "listLicenseTemplates"),
        ),
    )
    naming = assign_names(ir)
    by_id = {endpoint.operation.operation_id: endpoint for endpoint in naming.endpoints}
    assert by_id["getVersion"].namespace == ("misc",)
    assert by_id["getVersion"].method == "version"
    assert by_id["listLicenseTemplates"].namespace == ("misc", "licenses")
    assert by_id["getLicenseTemplateInfo"].namespace == ("misc", "licenses")


def test_known_top_level_groups_keep_their_names(tmp_path: Path) -> None:
    ir = _load(
        tmp_path,
        _spec(
            ("GET", "/user", "userGetCurrent"),
            ("GET", "/user/emails", "userListEmails"),
            ("GET", "/users/{username}", "userGet"),
            ("GET", "/repos/{owner}/{repo}", "repoGet"),
        ),
    )
    naming = assign_names(ir)
    modules = {endpoint.operation.operation_id: endpoint.namespace[0] for endpoint in naming.endpoints}
    assert modules == {"userGetCurrent": "user", "userListEmails": "user", "userGet": "users", "repoGet": "repos"}


def test_method_collisions_fail_loudly(tmp_path: Path) -> None:
    ir = _load(
        tmp_path,
        _spec(
            ("GET", "/widgets/{id}", "widgetGet"),
            ("GET", "/widgets/{id}.{format}", "widgetDownload"),
        ),
    )
    with pytest.raises(SpecError, match="unresolved method collision"):
        assign_names(ir)


def test_attribute_collisions_fail_loudly(tmp_path: Path) -> None:
    ir = _load(
        tmp_path,
        _spec(
            ("PATCH", "/repos/{owner}/{repo}/issues/{index}", "issueEditIssue"),
            ("GET", "/repos/{owner}/{repo}/issues/{index}/subscriptions", "issueSubscriptions"),
            ("GET", "/repos/{owner}/{repo}/issues/{index}/subscriptions/check", "issueCheckSubscription"),
        ),
    )
    # A method override may not reuse a sibling child namespace's attribute name.
    overrides = Overrides(methods={"issueEditIssue": MethodOverride(name="subscriptions")})
    with pytest.raises(SpecError, match="unresolved attribute collision"):
        assign_names(ir, overrides)


def test_method_override_resolves_collisions(tmp_path: Path) -> None:
    ir = _load(
        tmp_path,
        _spec(
            ("GET", "/widgets/{id}", "widgetGet"),
            ("GET", "/widgets/{id}.{format}", "widgetDownload"),
        ),
    )
    naming = assign_names(ir, Overrides(methods={"widgetDownload": MethodOverride(name="download")}))
    methods = {endpoint.operation.operation_id: endpoint.method for endpoint in naming.endpoints}
    assert methods == {"widgetGet": "get", "widgetDownload": "download"}


def test_namespace_override_renames_and_skips(tmp_path: Path) -> None:
    ir = _load(
        tmp_path,
        _spec(
            ("GET", "/gitignore/templates", "listGitignoresTemplates"),
            ("GET", "/gitignore/templates/{name}", "getGitignoreTemplateInfo"),
            ("POST", "/repos/{owner}/{repo}/transfer", "repoTransfer"),
            ("POST", "/repos/{owner}/{repo}/transfer/accept", "acceptRepoTransfer"),
        ),
    )
    overrides = Overrides(
        namespaces={
            "/gitignore/templates": NamespaceOverride(name="ignores"),
            "/repos/{owner}/{repo}/transfer": NamespaceOverride(skip=True),
        },
    )
    naming = assign_names(ir, overrides)
    by_id = {endpoint.operation.operation_id: endpoint for endpoint in naming.endpoints}
    assert by_id["listGitignoresTemplates"].namespace == ("misc", "gitignore", "ignores")
    assert by_id["getGitignoreTemplateInfo"].namespace == ("misc", "gitignore", "ignores")
    assert by_id["acceptRepoTransfer"].namespace == ("repos",)
    assert by_id["acceptRepoTransfer"].method == "accept"
    assert by_id["repoTransfer"].namespace == ("repos",)


def test_deprecated_flag_and_override(tmp_path: Path) -> None:
    data = _spec(("GET", "/widgets/{id}", "widgetGet"))
    data["paths"]["/widgets/{id}"]["get"]["deprecated"] = True
    ir = _load(tmp_path, data)
    naming = assign_names(ir, Overrides(methods={"widgetGet": MethodOverride(deprecated=False)}))
    assert naming.endpoints[0].deprecated is False


def test_unknown_override_keys_fail(tmp_path: Path) -> None:
    ir = _load(tmp_path, _spec(("GET", "/widgets", "widgetList")))
    with pytest.raises(SpecError, match="unknown operations"):
        assign_names(ir, Overrides(methods={"missing": MethodOverride(name="x")}))
    with pytest.raises(SpecError, match="unknown path prefixes"):
        assign_names(ir, Overrides(namespaces={"/nope": NamespaceOverride(name="x")}))


def test_registry_exclusions_are_applied_and_validated(tmp_path: Path) -> None:
    ir = _load(tmp_path, _spec(("GET", "/widgets", "widgetList"), ("GET", "/widgets/{id}", "widgetGet")))
    naming = assign_names(ir, registry=Registry(exclusions={"widgetGet": "cannot work"}))
    assert [endpoint.operation.operation_id for endpoint in naming.endpoints] == ["widgetList"]
    assert naming.exclusions[0][1] == "cannot work"
    with pytest.raises(SpecError, match="exclusions for unknown operations"):
        assign_names(ir, registry=Registry(exclusions={"missing": "no"}))


def test_invalid_override_identifiers_fail(tmp_path: Path) -> None:
    ir = _load(tmp_path, _spec(("GET", "/widgets", "widgetList")))
    with pytest.raises(SpecError, match="not a valid identifier"):
        assign_names(ir, Overrides(methods={"widgetList": MethodOverride(name="not-valid")}))


def test_load_mapping_and_registry(tmp_path: Path) -> None:
    mapping_path = tmp_path / "mapping.toml"
    mapping_path.write_text(
        '[namespaces."/user"]\nname = "user"\n\n[methods.widgetGet]\nname = "fetch"\ndeprecated = true\n',
        encoding="utf-8",
    )
    mapping = load_mapping(mapping_path)
    assert mapping.namespaces["/user"].name == "user"
    assert mapping.methods["widgetGet"].name == "fetch"
    assert mapping.methods["widgetGet"].deprecated is True
    assert load_mapping(tmp_path / "missing.toml").methods == {}

    registry_path = tmp_path / "registry.toml"
    registry_path.write_text('[[exclusions]]\noperation = "widgetGet"\nreason = "nope"\n', encoding="utf-8")
    assert load_registry(registry_path).exclusions == {"widgetGet": "nope"}
    assert load_registry(tmp_path / "missing.toml").exclusions == {}


def test_real_spec_top_level_counts(real_naming: Naming) -> None:
    counts: dict[str, int] = {}
    for endpoint in real_naming.endpoints:
        counts[endpoint.namespace[0]] = counts.get(endpoint.namespace[0], 0) + 1
    assert counts == {
        "repos": 264,
        "user": 66,
        "users": 17,
        "orgs": 53,
        "teams": 12,
        "admin": 51,
        "notifications": 5,
        "packages": 6,
        "settings": 4,
        "activitypub": 11,
        "misc": 16,
    }
    assert len(real_naming.endpoints) == 505
    assert len(real_naming.exclusions) == 1
    assert len(real_naming.endpoints) + len(real_naming.exclusions) == 506


def test_real_spec_worked_examples(real_naming: Naming) -> None:
    by_id = {endpoint.operation.operation_id: endpoint for endpoint in real_naming.endpoints}
    assert (by_id["repoGet"].namespace, by_id["repoGet"].method) == (("repos",), "get")
    assert (by_id["issueCreateIssue"].namespace, by_id["issueCreateIssue"].method) == (
        ("repos", "issues"),
        "create",
    )
    assert (by_id["issueGetComments"].namespace, by_id["issueGetComments"].method) == (
        ("repos", "issues", "comments"),
        "list",
    )
    assert (by_id["repoMergePullRequest"].namespace, by_id["repoMergePullRequest"].method) == (
        ("repos", "pulls"),
        "merge",
    )


def test_reviewed_renames(real_naming: Naming) -> None:
    calls = {
        endpoint.operation.operation_id: ".".join((*endpoint.namespace, endpoint.method))
        for endpoint in real_naming.endpoints
    }
    assert calls["orgPublicizeMember"] == "orgs.public_members.publicize"
    assert calls["orgConcealMember"] == "orgs.public_members.conceal"
    assert calls["createOrgRepoDeprecated"] == "misc.org.create_repo"
    assert calls["activitypubRepository"] == "activitypub.repository.get"
    assert calls["activitypubRepositoryInbox"] == "activitypub.repository.inbox"
    assert calls["activitypubPerson"] == "activitypub.person.get"
    assert calls["activitypubPersonInbox"] == "activitypub.person.inbox"
    assert calls["repoDeleteTopic"] == "repos.topics.remove"
    assert calls["repoDeleteFlag"] == "repos.flags.remove"
    assert calls["repoAddPushMirror"] == "repos.push_mirrors.create"
    assert calls["repoDeletePushMirror"] == "repos.push_mirrors.delete"
    assert calls["repoChangeFiles"] == "repos.contents.change_files"
    assert calls["repoGetCommitPullRequest"] == "repos.commits.pull_request"
    assert calls["notifyNewAvailable"] == "notifications.new_count"
