"""Declarative smoke registry, keyed by generated ``operationId``.

Every entry invokes exactly one generated operation with minimal valid inputs
against the seeded container. The first argument is the bound generated method
(located through its ``Operation ID: <id>`` docstring by
:func:`harness.build_method_index`); the second is the lazily-seeded
:class:`harness.Seed`. Entries never call private helpers on the client; where
an operation needs compound setup, a module-level helper does the setup with
the public surface and then invokes the bound method. The only exceptions are
the token-management operations, whose server rejects token auth: those
helpers bind the same docstring method on a Basic-auth client instead.

Operations that cannot run against this harness (external services, published
packages, GPG material, ...) live in ``skips.toml`` instead; the completeness
test proves the two sets plus ``codegen/registry.toml`` cover the Spec.
"""

from __future__ import annotations

from datetime import UTC, datetime
from typing import TYPE_CHECKING

from harness import ADMIN_PASSWORD, ADMIN_USERNAME, TINY_PNG_BASE64, USER_USERNAME, build_method_index

import pyfj

if TYPE_CHECKING:
    from collections.abc import Callable

    from harness import Seed

    SmokeCall = Callable[[Callable[..., object], Seed], object]


#: Return categories derived from ``codegen/naming-report.md`` (generated
#: from the Spec). The smoke test uses them to assert the documented outcome
#: of every exercised operation rather than only that the call did not raise.
RETURNS_NONE = frozenset(
    {  # 147
        "activitypubInstanceActorInbox",
        "activitypubRepositoryInbox",
        "activitypubPersonInbox",
        "deleteAdminRunner",
        "adminCronRun",
        "adminDeleteHook",
        "adminDeleteQuotaGroup",
        "adminAddRuleToQuotaGroup",
        "adminRemoveRuleFromQuotaGroup",
        "adminAddUserToQuotaGroup",
        "adminRemoveUserFromQuotaGroup",
        "adminDeleteQuotaRule",
        "adminAdoptRepository",
        "adminDeleteUnadoptedRepository",
        "adminDeleteUser",
        "adminDeleteUserEmails",
        "adminDeleteUserPublicKey",
        "adminSetUserQuotaGroups",
        "adminRenameUser",
        "adminDeleteUserAccessToken",
        "notifyReadList",
        "notifyReadThread",
        "orgDelete",
        "deleteOrgRunner",
        "updateOrgSecret",
        "deleteOrgSecret",
        "updateOrgVariable",
        "createOrgVariable",
        "deleteOrgVariable",
        "orgUpdateAvatar",
        "orgDeleteAvatar",
        "orgBlockUser",
        "orgDeleteHook",
        "orgDeleteLabel",
        "orgIsMember",
        "orgDeleteMember",
        "orgIsPublicMember",
        "orgPublicizeMember",
        "orgConcealMember",
        "renameOrg",
        "orgUnblockUser",
        "linkPackage",
        "unlinkPackage",
        "deletePackage",
        "repoDelete",
        "DeleteActionArtifact",
        "deleteRepoRunner",
        "DeleteActionRun",
        "CancelActionRun",
        "updateRepoSecret",
        "deleteRepoSecret",
        "updateRepoVariable",
        "createRepoVariable",
        "deleteRepoVariable",
        "repoUpdateAvatar",
        "repoDeleteAvatar",
        "repoDeleteBranchProtection",
        "repoDeleteBranch",
        "repoUpdateBranch",
        "repoCheckCollaborator",
        "repoAddCollaborator",
        "repoDeleteCollaborator",
        "repoReplaceAllFlags",
        "repoDeleteAllFlags",
        "repoCheckFlag",
        "repoAddFlag",
        "repoDeleteFlag",
        "repoRemoveNote",
        "repoDeleteGitHook",
        "repoDeleteHook",
        "repoTestHook",
        "issueDeleteComment",
        "issueDeleteIssueCommentAttachment",
        "issueDeleteCommentReaction",
        "issueDelete",
        "issueDeleteIssueAttachment",
        "issueDeleteCommentDeprecated",
        "issueClearLabels",
        "issueRemoveLabel",
        "pinIssue",
        "unpinIssue",
        "moveIssuePin",
        "issueDeleteIssueReaction",
        "issueDeleteStopWatch",
        "issueStartStopWatch",
        "issueStopStopWatch",
        "issueAddSubscription",
        "issueDeleteSubscription",
        "issueResetTime",
        "issueDeleteTime",
        "repoDeleteKey",
        "issueDeleteLabel",
        "issueDeleteMilestone",
        "repoMirrorSync",
        "notifyReadRepoList",
        "repoPullRequestIsMerged",
        "repoMergePullRequest",
        "repoCancelScheduledAutoMerge",
        "repoDeletePullReviewRequests",
        "repoDeletePullReview",
        "repoDeletePullReviewComment",
        "repoUpdatePullRequest",
        "repoPushMirrorSync",
        "repoDeletePushMirror",
        "repoDeleteReleaseByTag",
        "repoDeleteRelease",
        "repoDeleteReleaseAttachment",
        "userCurrentDeleteSubscription",
        "repoSyncForkDefault",
        "repoSyncForkBranch",
        "repoDeleteTagProtection",
        "repoDeleteTag",
        "repoAddTeam",
        "repoDeleteTeam",
        "repoUpdateTopics",
        "repoAddTopic",
        "repoDeleteTopic",
        "repoDeleteWikiPage",
        "orgDeleteTeam",
        "orgAddTeamMember",
        "orgRemoveTeamMember",
        "orgAddTeamRepository",
        "orgRemoveTeamRepository",
        "deleteUserRunner",
        "updateUserSecret",
        "deleteUserSecret",
        "updateUserVariable",
        "createUserVariable",
        "deleteUserVariable",
        "userCurrentActivityPubFollow",
        "userDeleteOAuth2Application",
        "userUpdateAvatar",
        "userDeleteAvatar",
        "userBlockUser",
        "userDeleteEmail",
        "userCurrentCheckFollowing",
        "userCurrentPutFollow",
        "userCurrentDeleteFollow",
        "userCurrentDeleteGPGKey",
        "userDeleteHook",
        "userCurrentDeleteKey",
        "userCurrentCheckStarring",
        "userCurrentPutStar",
        "userCurrentDeleteStar",
        "userUnblockUser",
        "userCheckFollowing",
        "userDeleteAccessToken",
    }
)

RETURNS_MAYBE_NONE = frozenset(
    {  # 4
        "DispatchWorkflow",
        "issueGetComment",
        "issueEditComment",
        "issueEditCommentDeprecated",
    }
)

RETURNS_STR = frozenset(
    {  # 10
        "renderMarkdown",
        "renderMarkdownRaw",
        "renderMarkup",
        "repoGetActionJobLogs",
        "repoDownloadCommitDiffOrPatch",
        "repoDownloadPullDiffOrPatch",
        "repoSigningKey",
        "getSigningKey",
        "getSSHSigningKey",
        "getVerificationToken",
    }
)

RETURNS_BYTES = frozenset(
    {  # 5
        "DownloadActionArtifact",
        "repoGetActionRunLogs",
        "repoGetArchive",
        "repoGetRawFileOrLFS",
        "repoGetRawFile",
    }
)

RETURNS_BOOL = frozenset(
    {  # 2
        "orgCheckQuota",
        "userCheckQuota",
    }
)

RETURNS_LIST = frozenset(
    {  # 44
        "adminGetActionRunJobs",
        "adminListQuotaGroups",
        "adminListUsersInQuotaGroup",
        "adminListQuotaRules",
        "adminSearchRunJobs",
        "adminUnadoptedList",
        "adminListUserEmails",
        "listGitignoresTemplates",
        "listLabelTemplates",
        "getLabelTemplateInfo",
        "listLicenseTemplates",
        "orgSearchRunJobs",
        "listPackageFiles",
        "repoSearchRunJobs",
        "ListActionRunJobs",
        "repoGetAssignees",
        "repoListBranchProtection",
        "repoGetContentsList",
        "repoListFlags",
        "GetBlobs",
        "repoListAllGitRefs",
        "repoListGitRefs",
        "repoListGitHooks",
        "repoGetIssueTemplates",
        "issueListIssueCommentAttachments",
        "issueGetCommentReactions",
        "repoListPinnedIssues",
        "issueListIssueAttachments",
        "issueGetComments",
        "issueGetLabels",
        "issueReplaceLabels",
        "issueAddLabel",
        "repoListPinnedPullRequests",
        "repoCreatePullReviewRequests",
        "repoGetPullReviewComments",
        "repoListReleaseAttachments",
        "repoGetReviewers",
        "repoListTagProtection",
        "repoListTeams",
        "userTrackedTimes",
        "userSearchRunJobs",
        "userListEmails",
        "userAddEmail",
        "userGetHeatmapData",
    }
)

RETURNS_DICT = frozenset(
    {  # 2
        "repoGetEditorConfig",
        "repoGetLanguages",
    }
)


# --------------------------------------------------------------------------- helpers


def _block_then_remove(m: Callable[..., object], s: Seed) -> object:
    """Exercise ``issueRemoveIssueBlocking`` on a freshly blocked pair."""
    blocker = s.issue(s.repo_for("blocker"), "source")
    blocked = s.issue(s.repo_for("blocker"), "target")
    s.admin.repos.issues.blocks.create(
        blocker.repo.owner,
        blocker.repo.name,
        blocker.index,
        body_index=blocked.index,
        body_owner=blocked.repo.owner,
        body_repo=blocked.repo.name,
    )
    return m(
        blocker.repo.owner,
        blocker.repo.name,
        blocker.index,
        body_index=blocked.index,
        body_owner=blocked.repo.owner,
        body_repo=blocked.repo.name,
    )


def _dependency_then_remove(m: Callable[..., object], s: Seed) -> object:
    """Exercise ``issueRemoveIssueDependencies`` on a fresh dependency."""
    dependent = s.issue(s.repo_for("dependency"), "dependent")
    dependency = s.issue(s.repo_for("dependency"), "dependency")
    s.admin.repos.issues.dependencies.create(
        dependent.repo.owner,
        dependent.repo.name,
        dependent.index,
        body_index=dependency.index,
        body_owner=dependency.repo.owner,
        body_repo=dependency.repo.name,
    )
    return m(
        dependent.repo.owner,
        dependent.repo.name,
        dependent.index,
        body_index=dependency.index,
        body_owner=dependency.repo.owner,
        body_repo=dependency.repo.name,
    )


def _publicize_then_check(m: Callable[..., object], s: Seed) -> object:
    """Publicize the regular user (as themselves), then exercise the membership check."""
    with s.admin.sudo_as(USER_USERNAME):
        s.admin.orgs.public_members.publicize(s.org, s.user)
    return m(s.org, s.user)


def _check_membership(m: Callable[..., object], s: Seed) -> object:
    """Exercise ``orgIsMember`` for a user known to be a member."""
    return m(s.org, s.user)


def _remove_org_member(m: Callable[..., object], s: Seed) -> object:
    """Exercise ``orgDeleteMember`` on a throwaway member."""
    team = s.team_for("org-member", members=[s.user_for("org-member")])
    assert team > 0
    return m(s.org, s.user_for("org-member"))


def _publicize_member(m: Callable[..., object], s: Seed) -> object:
    """Exercise ``orgPublicizeMember`` as the user (admin client, user context)."""
    with s.admin.sudo_as(USER_USERNAME):
        return m(s.org, s.user)


def _check_org_public_member(m: Callable[..., object], s: Seed) -> object:
    """Exercise ``orgIsPublicMember`` after the user publicizes themselves."""
    with s.admin.sudo_as(USER_USERNAME):
        s.admin.orgs.public_members.publicize(s.org, s.user)
    return m(s.org, s.user)


def _cancel_auto_merge(m: Callable[..., object], s: Seed) -> object:
    """Schedule auto-merge on a fresh pull request, then cancel it."""
    pull = s.pull(s.repo_for("auto-merge"), "cancel")
    s.admin.repos.pulls.merge(
        pull.repo.owner,
        pull.repo.name,
        pull.index,
        do=pyfj.MergePullRequestOptionDo.MERGE,
        merge_when_checks_succeed=True,
    )
    return m(pull.repo.owner, pull.repo.name, pull.index)


def _merge_pull(m: Callable[..., object], s: Seed) -> object:
    """Exercise the merge call on a fresh pull request."""
    pull = s.pull(s.repo_for("merge"), "merge")
    return m(pull.repo.owner, pull.repo.name, pull.index, do=pyfj.MergePullRequestOptionDo.MERGE)


def _is_merged(m: Callable[..., object], s: Seed) -> object:
    """Exercise ``repoPullRequestIsMerged`` on a pull request that is merged."""
    pull = s.pull(s.repo_for("merged"), "merged")
    s.admin.repos.pulls.merge(
        pull.repo.owner,
        pull.repo.name,
        pull.index,
        do=pyfj.MergePullRequestOptionDo.MERGE,
    )
    return m(pull.repo.owner, pull.repo.name, pull.index)


def _note_then_get(m: Callable[..., object], s: Seed) -> object:
    """Exercise ``repoGetNote`` after setting a note on a throwaway commit."""
    repo = s.repo_for("notes")
    sha = s.commit_sha(repo)
    s.admin.repos.git.notes.set(repo.owner, repo.name, sha, message="pyfj note")
    return m(repo.owner, repo.name, sha)


def _note_then_delete(m: Callable[..., object], s: Seed) -> object:
    """Exercise ``repoRemoveNote`` after setting a note on a throwaway commit."""
    repo = s.repo_for("notes-delete")
    sha = s.commit_sha(repo)
    s.admin.repos.git.notes.set(repo.owner, repo.name, sha, message="pyfj note")
    return m(repo.owner, repo.name, sha)


def _review_request_then_delete(m: Callable[..., object], s: Seed) -> object:
    """Exercise ``repoDeletePullReviewRequests`` after requesting a reviewer."""
    pull = s.pull(s.repo_for("review-request"), "delete")
    s.admin.repos.pulls.requested_reviewers.create(
        pull.repo.owner,
        pull.repo.name,
        pull.index,
        reviewers=[USER_USERNAME],
    )
    return m(pull.repo.owner, pull.repo.name, pull.index, reviewers=[USER_USERNAME])


def _update_branch(m: Callable[..., object], s: Seed) -> object:
    """Exercise ``repoUpdatePullRequest`` on a pull request with an outdated head."""
    repo = s.repo_for("update-branch")
    pull = s.pull(repo, "update")
    s.admin.repos.contents.create(
        repo.owner,
        repo.name,
        "base-change.txt",
        content="cHlmalBiYXNl",
        message="advance base",
        branch="main",
    )
    return m(pull.repo.owner, pull.repo.name, pull.index)


def _dispatch_workflow(m: Callable[..., object], s: Seed) -> object:
    """Exercise workflow dispatch on a repository carrying a workflow file."""
    repo = s.scratch_repo_with_file(
        "workflow",
        ".forgejo/workflows/smoke.yml",
        (
            "name: smoke\n"
            "on: workflow_dispatch\n"
            "jobs:\n"
            "  smoke:\n"
            "    runs-on: ubuntu-latest\n"
            "    steps:\n"
            "      - run: echo smoke\n"
        ),
    )
    return m(repo.owner, repo.name, "smoke.yml", ref="main")


def _delete_attached_asset(m: Callable[..., object], s: Seed) -> object:
    """Exercise ``issueDeleteIssueAttachment`` on a freshly attached file."""
    repo = s.repo_for("asset-delete")
    issue = s.issue(repo, "asset")
    attachment = s.admin.repos.issues.assets.create(
        repo.owner,
        repo.name,
        issue.index,
        attachment=("delete-me.txt", b"delete me", "text/plain"),
    )
    assert attachment.id is not None
    return m(repo.owner, repo.name, issue.index, attachment.id)


def _delete_comment_asset(m: Callable[..., object], s: Seed) -> object:
    """Exercise ``issueDeleteIssueCommentAttachment`` on a freshly attached file."""
    repo = s.repo_for("comment-asset-delete")
    issue = s.issue(repo, "comment")
    comment = s.admin.repos.issues.comments.create(repo.owner, repo.name, issue.index, body="asset comment")
    assert comment.id is not None
    attachment = s.admin.repos.issues.comments.assets.create(
        repo.owner,
        repo.name,
        comment.id,
        attachment=("delete-me.txt", b"delete me", "text/plain"),
    )
    assert attachment.id is not None
    return m(repo.owner, repo.name, comment.id, attachment.id)


def _delete_release_asset(m: Callable[..., object], s: Seed) -> object:
    """Exercise ``repoDeleteReleaseAttachment`` on a freshly attached file."""
    repo = s.repo_for("release-asset-delete")
    release = s.release_for(repo, "asset")
    attachment = s.admin.repos.releases.assets.create(
        repo.owner,
        repo.name,
        release,
        name="delete-me.txt",
        attachment=("delete-me.txt", b"delete me", "text/plain"),
    )
    assert attachment.id is not None
    return m(repo.owner, repo.name, release, attachment.id)


def _change_files(m: Callable[..., object], s: Seed) -> object:
    """Exercise ``repoChangeFiles`` with one create and one update operation."""
    repo = s.scratch_repo_with_file("change", "existing.txt", "existing")
    existing = s.admin.repos.contents.get(repo.owner, repo.name, "existing.txt")
    assert existing.sha is not None
    return m(
        repo.owner,
        repo.name,
        branch="main",
        message="pyfj change files",
        files=[
            pyfj.ChangeFileOperation(operation="create", path="created.txt", content="Y3JlYXRlZA=="),
            pyfj.ChangeFileOperation(operation="update", path="existing.txt", content="dXBkYXRlZA==", sha=existing.sha),
        ],
    )


def _apply_diff_patch(m: Callable[..., object], s: Seed) -> object:
    """Exercise ``repoApplyDiffPatch`` with a minimal unified diff."""
    repo = s.repo_for("diffpatch")
    diff = (
        "diff --git a/pyfj-diff.txt b/pyfj-diff.txt\n"
        "new file mode 100644\n"
        "index 0000000..e69de29\n"
        "--- /dev/null\n"
        "+++ b/pyfj-diff.txt\n"
        "@@ -0,0 +1 @@\n"
        "+pyfj diff\n"
    )
    return m(repo.owner, repo.name, content=diff, sha=s.commit_sha(repo), message="apply pyfj diff")


def _delete_file(m: Callable[..., object], s: Seed) -> object:
    """Exercise ``repoDeleteFile`` on a file created for the purpose."""
    repo = s.scratch_repo_with_file("delete-file", "to-delete.txt", "delete me")
    contents = s.admin.repos.contents.get(repo.owner, repo.name, "to-delete.txt")
    assert contents.sha is not None
    return m(repo.owner, repo.name, "to-delete.txt", sha=contents.sha, message="delete file")


def _update_file(m: Callable[..., object], s: Seed) -> object:
    """Exercise ``repoUpdateFile`` on a file created for the purpose."""
    repo = s.scratch_repo_with_file("update-file", "to-update.txt", "update me")
    contents = s.admin.repos.contents.get(repo.owner, repo.name, "to-update.txt")
    assert contents.sha is not None
    return m(
        repo.owner,
        repo.name,
        "to-update.txt",
        content="bmV3IGNvbnRlbnQ=",
        sha=contents.sha,
        message="update file",
    )


def _delete_branch(m: Callable[..., object], s: Seed) -> object:
    """Exercise ``repoDeleteBranch`` on a branch created for the purpose."""
    repo = s.repo_for("branch-delete")
    s.admin.repos.branches.create(repo.owner, repo.name, new_branch_name="pyfj-delete-me")
    return m(repo.owner, repo.name, "pyfj-delete-me")


def _update_branch_name(m: Callable[..., object], s: Seed) -> object:
    """Exercise ``repoUpdateBranch`` on a branch created for the purpose."""
    repo = s.repo_for("branch-update")
    s.admin.repos.branches.create(repo.owner, repo.name, new_branch_name="pyfj-rename-me")
    return m(repo.owner, repo.name, "pyfj-rename-me", name="pyfj-renamed")


def _sync_fork(m: Callable[..., object], s: Seed) -> object:
    """Exercise ``repoSyncForkDefault`` after advancing the forked repository."""
    s.admin.repos.contents.create(
        s.repo.owner,
        s.repo.name,
        "fork-upstream.txt",
        content="dXBzdHJlYW0=",
        message="advance upstream",
        branch="main",
    )
    return m(s.fork.owner, s.fork.name)


def _sync_fork_branch(m: Callable[..., object], s: Seed) -> object:
    """Exercise ``repoSyncForkBranch`` for a non-default branch present in both."""
    fork = s.fork  # fork before the branch exists upstream so the fork starts without it
    branch = "pyfj-sync-branch"
    s.admin.repos.branches.create(
        s.repo.owner,
        s.repo.name,
        new_branch_name=branch,
        old_branch_name="main",
    )
    s.user_client.repos.branches.create(
        fork.owner,
        fork.name,
        new_branch_name=branch,
        old_branch_name="main",
    )
    s.admin.repos.contents.create(
        s.repo.owner,
        s.repo.name,
        "fork-upstream-branch.txt",
        content="dXBzdHJlYW0=",
        message="advance upstream",
        branch=branch,
    )
    return m(fork.owner, fork.name, branch)


def _delete_tag_protection(m: Callable[..., object], s: Seed) -> object:
    """Exercise ``repoDeleteTagProtection`` on a fresh protection."""
    repo = s.repo_for("tag-protection-delete")
    return m(repo.owner, repo.name, s.tag_protection_for(repo, "delete"))


def _delete_branch_protection(m: Callable[..., object], s: Seed) -> object:
    """Exercise ``repoDeleteBranchProtection`` on a fresh protection."""
    repo = s.repo_for("branch-protection-delete")
    return m(repo.owner, repo.name, s.branch_protection_for(repo, "delete"))


def _delete_label(m: Callable[..., object], s: Seed) -> object:
    """Exercise ``issueDeleteLabel`` on a fresh label."""
    repo = s.repo_for("label-delete")
    return m(repo.owner, repo.name, s.label_for(repo, "delete"))


def _delete_milestone(m: Callable[..., object], s: Seed) -> object:
    """Exercise ``issueDeleteMilestone`` on a fresh milestone."""
    repo = s.repo_for("milestone-delete")
    return m(repo.owner, repo.name, s.milestone_for(repo, "delete"))


def _delete_release(m: Callable[..., object], s: Seed) -> object:
    """Exercise ``repoDeleteRelease`` on a fresh release."""
    repo = s.repo_for("release-delete")
    return m(repo.owner, repo.name, s.release_for(repo, "delete"))


def _delete_release_by_tag(m: Callable[..., object], s: Seed) -> object:
    """Exercise ``repoDeleteReleaseByTag`` on a fresh release."""
    repo = s.repo_for("release-tag-delete")
    s.release_for(repo, "delete")
    return m(repo.owner, repo.name, s.name("tag", "delete"))


def _delete_tag(m: Callable[..., object], s: Seed) -> object:
    """Exercise ``repoDeleteTag`` on a fresh lightweight tag."""
    repo = s.repo_for("tag-delete")
    sha = s.commit_sha(repo)
    s.admin.repos.tags.create(repo.owner, repo.name, tag_name="pyfj-delete-tag", target=sha)
    return m(repo.owner, repo.name, "pyfj-delete-tag")


def _delete_deploy_key(m: Callable[..., object], s: Seed) -> object:
    """Exercise ``repoDeleteKey`` on a fresh deploy key."""
    repo = s.repo_for("key-delete")
    return m(repo.owner, repo.name, s.deploy_key_for(repo, "delete"))


def _delete_repo_hook(m: Callable[..., object], s: Seed) -> object:
    """Exercise ``repoDeleteHook`` on a fresh hook."""
    repo = s.repo_for("hook-delete")
    return m(repo.owner, repo.name, s.hook_for("delete", repo=repo))


def _delete_org_hook(m: Callable[..., object], s: Seed) -> object:
    """Exercise ``orgDeleteHook`` on a fresh hook."""
    return m(s.org, s.hook_for("delete", org=s.org))


def _delete_user_hook(m: Callable[..., object], s: Seed) -> object:
    """Exercise ``userDeleteHook`` on a fresh hook."""
    return m(s.hook_for("delete"))


def _delete_admin_hook(m: Callable[..., object], s: Seed) -> object:
    """Exercise ``adminDeleteHook`` on a fresh system hook."""
    return m(s.admin_hook_for("delete"))


def _delete_org_variable(m: Callable[..., object], s: Seed) -> object:
    """Exercise ``deleteOrgVariable`` on a fresh variable."""
    return m(s.org, s.org_variable_for("delete"))


def _delete_repo_variable(m: Callable[..., object], s: Seed) -> object:
    """Exercise ``deleteRepoVariable`` on a fresh variable."""
    repo = s.repo
    return m(repo.owner, repo.name, s.repo_variable_for(repo, "delete"))


def _delete_user_variable(m: Callable[..., object], s: Seed) -> object:
    """Exercise ``deleteUserVariable`` on a fresh variable."""
    return m(s.user_variable_for("delete"))


def _delete_org_secret(m: Callable[..., object], s: Seed) -> object:
    """Exercise ``deleteOrgSecret`` on a fresh secret."""
    return m(s.org, s.org_secret_for("delete"))


def _delete_repo_secret(m: Callable[..., object], s: Seed) -> object:
    """Exercise ``deleteRepoSecret`` on a fresh secret."""
    repo = s.repo
    return m(repo.owner, repo.name, s.repo_secret_for(repo, "delete"))


def _delete_user_secret(m: Callable[..., object], s: Seed) -> object:
    """Exercise ``deleteUserSecret`` on a fresh secret."""
    return m(s.user_secret_for("delete"))


def _unwatch_repo(m: Callable[..., object], s: Seed) -> object:
    """Exercise ``userCurrentDeleteSubscription`` on a watched repository."""
    s.admin.repos.subscription.update(s.repo.owner, s.repo.name)
    return m(s.repo.owner, s.repo.name)


def _delete_wiki_page(m: Callable[..., object], s: Seed) -> object:
    """Exercise ``repoDeleteWikiPage`` on a fresh wiki page."""
    repo = s.repo_for("wiki-delete")
    page = s.wiki_for(repo, "delete")
    return m(repo.owner, repo.name, page)


def _delete_issue_comment(m: Callable[..., object], s: Seed) -> object:
    """Exercise ``issueDeleteComment`` on a fresh comment."""
    repo = s.repo_for("comment-delete")
    issue = s.issue(repo, "comment")
    comment = s.admin.repos.issues.comments.create(repo.owner, repo.name, issue.index, body="delete me")
    return m(repo.owner, repo.name, comment.id)


def _delete_issue(m: Callable[..., object], s: Seed) -> object:
    """Exercise ``issueDelete`` on a fresh issue."""
    repo = s.repo_for("issue-delete")
    issue = s.issue(repo, "delete")
    return m(repo.owner, repo.name, issue.index)


def _delete_comment_deprecated(m: Callable[..., object], s: Seed) -> object:
    """Exercise the deprecated in-issue comment delete on a fresh comment."""
    repo = s.repo_for("comment-deprecated")
    issue = s.issue(repo, "deprecated")
    comment = s.admin.repos.issues.comments.create(repo.owner, repo.name, issue.index, body="deprecated")
    return m(repo.owner, repo.name, issue.index, comment.id)


def _delete_time(m: Callable[..., object], s: Seed) -> object:
    """Exercise ``issueDeleteTime`` on a fresh tracked time."""
    repo = s.repo_for("time-delete")
    issue = s.issue(repo, "time")
    entry = s.admin.repos.issues.times.add(repo.owner, repo.name, issue.index, time=30)
    assert entry.id is not None
    return m(repo.owner, repo.name, issue.index, entry.id)


def _delete_reaction(m: Callable[..., object], s: Seed) -> object:
    """Exercise ``issueDeleteIssueReaction`` on a fresh reaction."""
    repo = s.repo_for("reaction-delete")
    issue = s.issue(repo, "reaction")
    s.admin.repos.issues.reactions.create(repo.owner, repo.name, issue.index, content="+1")
    return m(repo.owner, repo.name, issue.index, content="+1")


def _delete_comment_reaction(m: Callable[..., object], s: Seed) -> object:
    """Exercise ``issueDeleteCommentReaction`` on a fresh reaction."""
    repo = s.repo_for("comment-reaction-delete")
    issue = s.issue(repo, "reaction")
    comment = s.admin.repos.issues.comments.create(repo.owner, repo.name, issue.index, body="reaction")
    assert comment.id is not None
    s.admin.repos.issues.comments.reactions.create(repo.owner, repo.name, comment.id, content="+1")
    return m(repo.owner, repo.name, comment.id, content="+1")


def _unsubscribe_issue_user(m: Callable[..., object], s: Seed) -> object:
    """Exercise ``issueDeleteSubscription`` after subscribing a user."""
    s.admin.repos.issues.subscriptions.add(s.repo.owner, s.repo.name, s.issue_index, USER_USERNAME)
    return m(s.repo.owner, s.repo.name, s.issue_index, USER_USERNAME)


def _remove_team_member(m: Callable[..., object], s: Seed) -> object:
    """Exercise ``orgRemoveTeamMember`` on a team that already has the user."""
    team = s.team_for("remove-member", members=[s.user])
    return m(team, s.user)


def _remove_team_repository(m: Callable[..., object], s: Seed) -> object:
    """Exercise ``orgRemoveTeamRepository`` on a team that already has the repo."""
    team = s.team_for("remove-repo", repos=[s.repo])
    return m(team, s.repo.owner, s.repo.name)


def _list_issue_reactions(m: Callable[..., object], s: Seed) -> object:
    """Exercise ``issueGetIssueReactions`` after adding a reaction."""
    s.admin.repos.issues.reactions.create(s.repo.owner, s.repo.name, s.issue_index, content="+1")
    return m(s.repo.owner, s.repo.name, s.issue_index)


def _list_comment_reactions(m: Callable[..., object], s: Seed) -> object:
    """Exercise ``issueGetCommentReactions`` after adding a reaction."""
    s.admin.repos.issues.comments.reactions.create(s.repo.owner, s.repo.name, s.comment_id, content="+1")
    return m(s.repo.owner, s.repo.name, s.comment_id)


def _latest_release(m: Callable[..., object], s: Seed) -> object:
    """Exercise ``repoGetLatestRelease`` after ensuring the baseline release exists."""
    s.ensure_release()
    return m(*s.repo.args)


def _release_by_tag(m: Callable[..., object], s: Seed) -> object:
    """Exercise ``repoGetReleaseByTag`` after ensuring the baseline release exists."""
    s.ensure_release()
    return m(*s.repo.args, s.release_tag)


def _get_tag(m: Callable[..., object], s: Seed) -> object:
    """Exercise ``repoGetTag`` after ensuring the release tag exists."""
    s.ensure_release()
    return m(*s.repo.args, s.release_tag)


def _create_user_token(m: Callable[..., object], s: Seed) -> object:
    """Exercise ``userCreateToken`` through the docstring-bound method on a Basic client.

    Forgejo rejects token authentication for token management, so the method is
    located by its ``Operation ID`` on the Basic-auth client instead of using
    the sync client bound by the runner.
    """
    del m
    method = build_method_index(s.basic_user_client)["userCreateToken"]
    return method(s.user, name=s.name("token", "users"), scopes=["all"])


def _delete_user_token(m: Callable[..., object], s: Seed) -> object:
    """Exercise ``userDeleteAccessToken`` through docstring-bound Basic-client methods."""
    del m
    name = s.name("token", "users-delete")
    create = build_method_index(s.basic_user_client)["userCreateToken"]
    create(s.user, name=name, scopes=["all"])
    delete = build_method_index(s.basic_user_client)["userDeleteAccessToken"]
    return delete(s.user, name)


def _create_pull_request(m: Callable[..., object], s: Seed) -> object:
    """Exercise ``repoCreatePullRequest`` on a fresh branch in a fresh repository."""
    repo = s.repo_for("pull-create")
    s.admin.repos.contents.create(
        repo.owner,
        repo.name,
        "pull-create.txt",
        content="cHlmalBwdWxsCg==",
        message="add pull branch file",
        new_branch="pyfj-pull-create",
    )
    return m(repo.owner, repo.name, title=s.name("pull", "created"), head="pyfj-pull-create", base="main")


def _create_block(m: Callable[..., object], s: Seed) -> object:
    """Exercise ``issueCreateIssueBlocking`` on a fresh issue pair."""
    blocker = s.issue(s.repo_for("blocker-create"), "source")
    blocked = s.issue(s.repo_for("blocker-create"), "target")
    return m(
        blocker.repo.owner,
        blocker.repo.name,
        blocker.index,
        body_index=blocked.index,
        body_owner=blocked.repo.owner,
        body_repo=blocked.repo.name,
    )


def _create_dependency(m: Callable[..., object], s: Seed) -> object:
    """Exercise ``issueCreateIssueDependencies`` on a fresh issue pair."""
    dependent = s.issue(s.repo_for("dependency-create"), "dependent")
    dependency = s.issue(s.repo_for("dependency-create"), "dependency")
    return m(
        dependent.repo.owner,
        dependent.repo.name,
        dependent.index,
        body_index=dependency.index,
        body_owner=dependency.repo.owner,
        body_repo=dependency.repo.name,
    )


def _set_user_quota_groups(m: Callable[..., object], s: Seed) -> object:
    """Exercise ``adminSetUserQuotaGroups`` and restore the user's quota state.

    A user in a quota group with no matching rule is denied everything, which
    would break later tests that create or transfer repositories for the user.
    """
    group = s.quota_group_for("assign")
    result = m(s.user, groups=[group])
    m(s.user, groups=[])
    return result


def _remove_collaborator(m: Callable[..., object], s: Seed) -> object:
    """Exercise ``repoDeleteCollaborator`` on a repository with that collaborator."""
    repo = s.repo_for("collaborator-remove")
    s.admin.repos.collaborators.add(
        repo.owner,
        repo.name,
        USER_USERNAME,
        permission=pyfj.AddCollaboratorOptionPermission.READ,
    )
    return m(repo.owner, repo.name, USER_USERNAME)


def _check_collaborator(m: Callable[..., object], s: Seed) -> object:
    """Exercise ``repoCheckCollaborator`` on a repository with that collaborator."""
    repo = s.repo_for("collaborator-check")
    s.admin.repos.collaborators.add(
        repo.owner,
        repo.name,
        USER_USERNAME,
        permission=pyfj.AddCollaboratorOptionPermission.READ,
    )
    return m(repo.owner, repo.name, USER_USERNAME)


def _remove_flag(m: Callable[..., object], s: Seed) -> object:
    """Exercise ``repoDeleteFlag`` after setting the flag."""
    repo = s.repo_for("flag")
    s.admin.repos.flags.add(repo.owner, repo.name, "pyfj-delete-flag")
    return m(repo.owner, repo.name, "pyfj-delete-flag")


def _check_flag(m: Callable[..., object], s: Seed) -> object:
    """Exercise ``repoCheckFlag`` after setting the flag."""
    repo = s.repo_for("flag")
    s.admin.repos.flags.add(repo.owner, repo.name, "pyfj-check-flag")
    return m(repo.owner, repo.name, "pyfj-check-flag")


def _delete_all_flags(m: Callable[..., object], s: Seed) -> object:
    """Exercise ``repoDeleteAllFlags`` after setting a flag."""
    repo = s.repo_for("flag")
    s.admin.repos.flags.add(repo.owner, repo.name, "pyfj-delete-all-flag")
    return m(repo.owner, repo.name)


def _delete_topic(m: Callable[..., object], s: Seed) -> object:
    """Exercise ``repoDeleteTopic`` after adding the topic."""
    s.admin.repos.topics.add(s.repo.owner, s.repo.name, "pyfj-delete-topic")
    return m(s.repo.owner, s.repo.name, "pyfj-delete-topic")


def _migrate_repo(m: Callable[..., object], s: Seed) -> object:
    """Exercise ``repoMigrate`` from the instance's own localhost clone address."""
    source = s.scratch_repo_with_file("migrate-source", "migrate.txt", "migrated")
    return m(
        clone_addr=f"http://localhost:3000/{source.full_name}.git",
        repo_name=s.name("repo", "migrated"),
        repo_owner=s.org,
        service=pyfj.MigrateRepoOptionsService.GIT,
        auth_username=ADMIN_USERNAME,
        auth_password=ADMIN_PASSWORD,
    )


def _mirror_sync(m: Callable[..., object], s: Seed) -> object:
    """Exercise ``repoMirrorSync`` after advancing the mirrored source."""
    mirror = s.mirrored_repo_for("sync")
    source = s.scratch_repo_with_file("mirror-source-sync", "mirror.txt", "mirrored")
    s.admin.repos.contents.create(
        source.owner,
        source.name,
        "mirror-advance.txt",
        content="YWR2YW5jZWQ=",
        message="advance mirror source",
    )
    return m(mirror.owner, mirror.name)


def _convert_mirror(m: Callable[..., object], s: Seed) -> object:
    """Exercise ``repoConvert`` on a fresh pull mirror."""
    mirror = s.mirrored_repo_for("convert")
    return m(mirror.owner, mirror.name)


def _add_push_mirror(m: Callable[..., object], s: Seed) -> object:
    """Exercise ``repoAddPushMirror`` pointing at another repository on the instance."""
    source = s.scratch_repo_with_file("push-source-add", "push.txt", "pushed")
    target = s.repo_for("push-target-add")
    return m(
        source.owner,
        source.name,
        remote_address=f"http://localhost:3000/{target.full_name}.git",
        remote_username=ADMIN_USERNAME,
        remote_password=ADMIN_PASSWORD,
        sync_on_commit=True,
        interval="8h",
    )


def _get_push_mirror(m: Callable[..., object], s: Seed) -> object:
    """Exercise ``repoGetPushMirrorByRemoteName`` on a fresh push mirror."""
    source, remote_name = s.push_mirror_for("get")
    return m(source.owner, source.name, remote_name)


def _delete_push_mirror(m: Callable[..., object], s: Seed) -> object:
    """Exercise ``repoDeletePushMirror`` on a fresh push mirror."""
    source, remote_name = s.push_mirror_for("delete")
    return m(source.owner, source.name, remote_name)


def _push_mirror_sync(m: Callable[..., object], s: Seed) -> object:
    """Exercise ``repoPushMirrorSync`` after advancing the push-mirror source."""
    source, _ = s.push_mirror_for("sync")
    s.admin.repos.contents.create(
        source.owner,
        source.name,
        "push-advance.txt",
        content="YWR2YW5jZWQ=",
        message="advance push source",
    )
    return m(source.owner, source.name)


def _delete_org_label(m: Callable[..., object], s: Seed) -> object:
    """Exercise ``orgDeleteLabel`` on a fresh organization label."""
    return m(s.org, s.org_label_for("delete"))


def _conceal_member(m: Callable[..., object], s: Seed) -> object:
    """Exercise ``orgConcealMember`` after the user publicizes themselves."""
    with s.admin.sudo_as(USER_USERNAME):
        s.admin.orgs.public_members.publicize(s.org, s.user)
        return m(s.org, s.user)


def _follow_then_check(m: Callable[..., object], s: Seed) -> object:
    """Exercise the authenticated user's following check for a followed user."""
    target = s.user_for("followed")
    s.admin.user.following.add(target)
    return m(target)


def _follow_then_check_users(m: Callable[..., object], s: Seed) -> object:
    """Exercise the public following check for a user that is followed."""
    target = s.user_for("followed")
    s.admin.user.following.add(target)
    return m(ADMIN_USERNAME, target)


def _delete_follow(m: Callable[..., object], s: Seed) -> object:
    """Exercise ``userCurrentDeleteFollow`` for a followed user."""
    target = s.user_for("followed")
    s.admin.user.following.add(target)
    return m(target)


def _star_then_check(m: Callable[..., object], s: Seed) -> object:
    """Exercise a starring check for a repository that is starred."""
    repo = s.user_repo_for("star")
    s.admin.user.starred.add(repo.owner, repo.name)
    return m(repo.owner, repo.name)


def _unstar(m: Callable[..., object], s: Seed) -> object:
    """Exercise ``userCurrentDeleteStar`` for a starred repository."""
    repo = s.user_repo_for("star")
    s.admin.user.starred.add(repo.owner, repo.name)
    return m(repo.owner, repo.name)


def _unblock_user(m: Callable[..., object], s: Seed) -> object:
    """Exercise ``userUnblockUser`` for a blocked user."""
    target = s.user_for("user-unblock")
    s.admin.user.block(target)
    return m(target)


def _list_blocked_user(m: Callable[..., object], s: Seed) -> object:
    """Exercise ``userListBlockedUsers`` with at least one blocked user."""
    s.admin.user.block(s.user_for("user-block-list"))
    return m()


def _block_org_user(m: Callable[..., object], s: Seed) -> object:
    """Exercise ``orgBlockUser`` on a throwaway user."""
    return m(s.org, s.user_for("org-block"))


def _list_blocked_org_user(m: Callable[..., object], s: Seed) -> object:
    """Exercise ``orgListBlockedUsers`` with at least one blocked user."""
    target = s.user_for("org-block-list")
    s.admin.orgs.block(s.org, target)
    return m(s.org)


def _unblock_org_user(m: Callable[..., object], s: Seed) -> object:
    """Exercise ``orgUnblockUser`` for a blocked user."""
    target = s.user_for("org-unblock")
    s.admin.orgs.block(s.org, target)
    return m(s.org, target)


def _edit_comment_deprecated(m: Callable[..., object], s: Seed) -> object:
    """Exercise the deprecated in-issue comment edit on a fresh comment."""
    repo = s.repo_for("comment-deprecated-edit")
    issue = s.issue(repo, "deprecated-edit")
    comment = s.admin.repos.issues.comments.create(repo.owner, repo.name, issue.index, body="deprecated edit")
    return m(repo.owner, repo.name, issue.index, comment.id, body="edited deprecated")


def _pin_then_unpin(m: Callable[..., object], s: Seed) -> object:
    """Exercise ``unpinIssue`` on a pinned issue."""
    repo = s.repo_for("unpin")
    issue = s.issue(repo, "unpin")
    s.admin.repos.issues.pin(repo.owner, repo.name, issue.index)
    return m(repo.owner, repo.name, issue.index)


def _move_pin(m: Callable[..., object], s: Seed) -> object:
    """Exercise ``moveIssuePin`` with two pinned issues."""
    repo = s.repo_for("move-pin")
    first = s.issue(repo, "first")
    second = s.issue(repo, "second")
    s.admin.repos.issues.pin(repo.owner, repo.name, first.index)
    s.admin.repos.issues.pin(repo.owner, repo.name, second.index)
    return m(repo.owner, repo.name, second.index, 1)


def _remove_issue_label(m: Callable[..., object], s: Seed) -> object:
    """Exercise ``issueRemoveLabel`` for a label present on the issue."""
    repo = s.repo_for("label-remove")
    issue = s.issue(repo, "label")
    label = s.label_for(repo, "remove")
    s.admin.repos.issues.labels.add(repo.owner, repo.name, issue.index, labels=[label])
    return m(repo.owner, repo.name, issue.index, label)


def _reset_issue_times(m: Callable[..., object], s: Seed) -> object:
    """Exercise ``issueResetTime`` after adding a tracked time."""
    repo = s.repo_for("times-reset")
    issue = s.issue(repo, "reset")
    s.admin.repos.issues.times.add(repo.owner, repo.name, issue.index, time=45)
    return m(repo.owner, repo.name, issue.index)


def _delete_stopwatch(m: Callable[..., object], s: Seed) -> object:
    """Exercise ``issueDeleteStopWatch`` after starting a stopwatch."""
    repo = s.repo_for("stopwatch-delete")
    issue = s.issue(repo, "delete")
    s.admin.repos.issues.stopwatch.start(repo.owner, repo.name, issue.index)
    return m(repo.owner, repo.name, issue.index)


def _stop_stopwatch(m: Callable[..., object], s: Seed) -> object:
    """Exercise ``issueStopStopWatch`` after starting a stopwatch."""
    repo = s.repo_for("stopwatch-stop")
    issue = s.issue(repo, "stop")
    s.admin.repos.issues.stopwatch.start(repo.owner, repo.name, issue.index)
    return m(repo.owner, repo.name, issue.index)


def _submit_review(m: Callable[..., object], s: Seed) -> object:
    """Exercise ``repoSubmitPullReview`` on a fresh pending review."""
    pull = s.pull(s.repo_for("submit-review"), "review")
    review = s.pending_review(pull)
    return m(pull.repo.owner, pull.repo.name, pull.index, review, event="COMMENT", body="submitted")


def _delete_review(m: Callable[..., object], s: Seed) -> object:
    """Exercise ``repoDeletePullReview`` on a fresh pending review."""
    pull = s.pull(s.repo_for("delete-review"), "review")
    review = s.pending_review(pull)
    return m(pull.repo.owner, pull.repo.name, pull.index, review)


def _create_review_comment(m: Callable[..., object], s: Seed) -> object:
    """Exercise ``repoCreatePullReviewComment`` on a fresh pending review."""
    repo = s.repo_for("review-comment")
    pull = s.pull(repo, "comment")
    review = s.pending_review(pull)
    return m(
        pull.repo.owner,
        pull.repo.name,
        pull.index,
        review,
        body="smoke review comment",
        path="pyfj-comment.txt",
        new_position=1,
    )


def _get_review_comment(m: Callable[..., object], s: Seed) -> object:
    """Exercise ``repoGetPullReviewComment`` on a freshly created comment."""
    repo = s.repo_for("review-comment-get")
    pull = s.pull(repo, "get")
    review = s.pending_review(pull)
    comment = s.admin.repos.pulls.reviews.comments.create(
        pull.repo.owner,
        pull.repo.name,
        pull.index,
        review,
        body="get me",
        path="pyfj-get.txt",
        new_position=1,
    )
    assert comment.id is not None
    return m(pull.repo.owner, pull.repo.name, pull.index, review, comment.id)


def _delete_review_comment(m: Callable[..., object], s: Seed) -> object:
    """Exercise ``repoDeletePullReviewComment`` on a freshly created comment."""
    repo = s.repo_for("review-comment-delete")
    pull = s.pull(repo, "delete")
    review = s.pending_review(pull)
    comment = s.admin.repos.pulls.reviews.comments.create(
        pull.repo.owner,
        pull.repo.name,
        pull.index,
        review,
        body="delete me",
        path="pyfj-delete.txt",
        new_position=1,
    )
    assert comment.id is not None
    return m(pull.repo.owner, pull.repo.name, pull.index, review, comment.id)


def _dismiss_review(m: Callable[..., object], s: Seed) -> object:
    """Exercise ``repoDismissPullReview`` on a submitted review by the user."""
    pull = s.pull(s.repo_for("dismiss-review"), "review")
    review = s.user_review(pull, event="APPROVED")
    return m(pull.repo.owner, pull.repo.name, pull.index, review, message="dismissed by smoke")


def _undismiss_review(m: Callable[..., object], s: Seed) -> object:
    """Exercise ``repoUnDismissPullReview`` on a dismissed review."""
    pull = s.pull(s.repo_for("undismiss-review"), "review")
    review = s.user_review(pull, event="APPROVED")
    s.admin.repos.pulls.reviews.dismiss(pull.repo.owner, pull.repo.name, pull.index, review, message="dismiss")
    return m(pull.repo.owner, pull.repo.name, pull.index, review)


# --------------------------------------------------------------------------- admin

_ADMIN = {
    "getAdminRunners": lambda m, s: m(),
    "registerAdminRunner": lambda m, s: m(name=s.name("runner", "registered"), description="smoke runner"),
    "adminGetActionRunJobs": lambda m, s: m(),
    "adminGetRunnerRegistrationToken": lambda m, s: m(),
    "getAdminRunner": lambda m, s: m(s.admin_runner_id),
    "deleteAdminRunner": lambda m, s: m(s.runner_for("delete", scope="admin")),
    "adminCronList": lambda m, s: m(),
    "adminCronRun": lambda m, s: m(s.cron_task),
    "adminGetAllEmails": lambda m, s: m(),
    "adminSearchEmails": lambda m, s: m(q=s.run_id),
    "adminListHooks": lambda m, s: m(),
    "adminCreateHook": lambda m, s: m(
        type=pyfj.CreateHookOptionType.FORGEJO,
        config=pyfj.CreateHookOptionConfig(
            url="http://127.0.0.1:1/pyfj-scratch-hook",
            content_type="json",
        ),
        events=["push"],
    ),
    "adminGetHook": lambda m, s: m(s.admin_hook_for("base")),
    "adminDeleteHook": _delete_admin_hook,
    "adminEditHook": lambda m, s: m(s.admin_hook_for("base"), active=True),
    "adminGetAllOrgs": lambda m, s: m(),
    "adminListQuotaGroups": lambda m, s: m(),
    "adminCreateQuotaGroup": lambda m, s: m(name=s.name("quota-group", "created")),
    "adminGetQuotaGroup": lambda m, s: m(s.quota_group_for("base")),
    "adminDeleteQuotaGroup": lambda m, s: m(s.quota_group_for("delete")),
    "adminAddRuleToQuotaGroup": lambda m, s: m(s.quota_group_for("rules"), s.quota_rule_for("rules")),
    "adminRemoveRuleFromQuotaGroup": lambda m, s: m(
        s.quota_group_for("rules-remove", rules=[s.quota_rule_for("rules-remove-rule")]),
        s.quota_rule_for("rules-remove-rule"),
    ),
    "adminListUsersInQuotaGroup": lambda m, s: m(s.quota_group_for("users", users=[s.user])),
    "adminAddUserToQuotaGroup": lambda m, s: m(s.quota_group_for("users"), s.user),
    "adminRemoveUserFromQuotaGroup": lambda m, s: m(s.quota_group_for("users-remove", users=[s.user]), s.user),
    "adminListQuotaRules": lambda m, s: m(),
    "adminCreateQuotaRule": lambda m, s: m(name=s.name("quota-rule", "created"), limit=100),
    "adminGetQuotaRule": lambda m, s: m(s.quota_rule_for("base")),
    "adminDeleteQuotaRule": lambda m, s: m(s.quota_rule_for("delete")),
    "adminEditQuotaRule": lambda m, s: m(s.quota_rule_for("base"), limit=200),
    "adminSearchRunJobs": lambda m, s: m(),
    "adminGetRegistrationToken": lambda m, s: m(),
    "adminUnadoptedList": lambda m, s: m(),
    "adminSearchUsers": lambda m, s: m(),
    "adminCreateUser": lambda m, s: m(
        username=s.name("user", "created"),
        password="pyfj-scratch-pass-1234",
        email=f"{s.name('user', 'created')}@pyfj.test",
        must_change_password=False,
    ),
    "adminDeleteUser": lambda m, s: m(s.user_for("delete")),
    "adminEditUser": lambda m, s: m(s.user_for("edit"), full_name="Edited Scratch"),
    "adminListUserEmails": lambda m, s: m(s.user),
    "adminDeleteUserEmails": lambda m, s: m(s.user, emails=[s.email_for("admin-delete")]),
    "adminCreatePublicKey": lambda m, s: m(
        s.user_for("key-create"),
        key=s.ssh_key_for("admin-key-create"),
        title=s.name("admin-user-key", "create"),
        read_only=True,
    ),
    "adminDeleteUserPublicKey": lambda m, s: m(*s.admin_user_key_for("delete")),
    "adminCreateOrg": lambda m, s: m(
        s.user_for("org"),
        body_username=s.name("org", "admin"),
    ),
    "adminGetUserQuota": lambda m, s: m(s.user),
    "adminSetUserQuotaGroups": _set_user_quota_groups,
    "adminRenameUser": lambda m, s: m(s.user_for("rename"), new_username=s.name("renamed")),
    "adminCreateRepo": lambda m, s: m(s.user, name=s.name("repo", "admin-created"), auto_init=True),
    "adminListUserAccessTokens": lambda m, s: m(s.user),
    "adminCreateUserAccessToken": lambda m, s: m(
        s.user_for("token"),
        name=s.name("token", "created"),
        scopes=["all"],
    ),
    "adminDeleteUserAccessToken": lambda m, s: m(
        s.user_for("token-delete"),
        s.access_token_for(s.user_for("token-delete"), "delete"),
    ),
}

# ---------------------------------------------------------------------------- misc

_MISC = {
    "listGitignoresTemplates": lambda m, s: m(),
    "getGitignoreTemplateInfo": lambda m, s: m(s.gitignore_template),
    "listLabelTemplates": lambda m, s: m(),
    "getLabelTemplateInfo": lambda m, s: m(s.label_template),
    "listLicenseTemplates": lambda m, s: m(),
    "getLicenseTemplateInfo": lambda m, s: m(s.license_template),
    "renderMarkdown": lambda m, s: m(text="# pyfj", mode="markdown"),
    "renderMarkdownRaw": lambda m, s: m(body="# pyfj"),
    "renderMarkup": lambda m, s: m(text="**pyfj**", mode="markdown"),
    "createOrgRepoDeprecated": lambda m, s: m(s.org, name=s.name("repo", "deprecated"), auto_init=True),
    "repoGetByID": lambda m, s: m(s.repo_id),
    "getSigningKey": lambda m, s: m(),
    "topicSearch": lambda m, s: m(q="pyfj"),
    "getVersion": lambda m, s: m(),
}

# --------------------------------------------------------------------- notifications

_NOTIFICATIONS = {
    "notifyGetList": lambda m, s: m(all=True),
    "notifyReadList": lambda m, s: m(all=True, to_status="read"),
    "notifyNewAvailable": lambda m, s: m(),
    "notifyGetThread": lambda m, s: m(s.notification_id),
    "notifyReadThread": lambda m, s: m(s.notification_id, to_status="read"),
}

# -------------------------------------------------------------------------- packages

_PACKAGES = {
    "listPackages": lambda m, s: m(s.org),
}

# -------------------------------------------------------------------------- settings

_SETTINGS = {
    "getGeneralAPISettings": lambda m, s: m(),
    "getGeneralAttachmentSettings": lambda m, s: m(),
    "getGeneralRepositorySettings": lambda m, s: m(),
    "getGeneralUISettings": lambda m, s: m(),
}

# ----------------------------------------------------------------------------- orgs

_ORGS = {
    "orgGetAll": lambda m, s: m(),
    "orgCreate": lambda m, s: m(username=s.name("org", "created"), full_name="pyfj created org"),
    "orgGet": lambda m, s: m(s.org),
    "orgDelete": lambda m, s: m(s.org_for("delete")),
    "orgEdit": lambda m, s: m(s.org, description="edited by smoke"),
    "getOrgRunners": lambda m, s: m(s.org),
    "registerOrgRunner": lambda m, s: m(s.org, name=s.name("runner", "org")),
    "orgSearchRunJobs": lambda m, s: m(s.org),
    "orgGetRunnerRegistrationToken": lambda m, s: m(s.org),
    "getOrgRunner": lambda m, s: m(s.org, s.runner_for("base", scope="org")),
    "deleteOrgRunner": lambda m, s: m(s.org, s.runner_for("delete", scope="org")),
    "orgListActionsSecrets": lambda m, s: m(s.org),
    "updateOrgSecret": lambda m, s: m(s.org, s.secret_name("update"), data="dmFsdWU="),
    "deleteOrgSecret": _delete_org_secret,
    "getOrgVariablesList": lambda m, s: m(s.org),
    "getOrgVariable": lambda m, s: m(s.org, s.org_variable_for("base")),
    "updateOrgVariable": lambda m, s: m(
        s.org, s.org_variable_for("base"), name=s.org_variable_for("base"), value="two"
    ),
    "createOrgVariable": lambda m, s: m(s.org, s.variable_name("created"), value="one"),
    "deleteOrgVariable": _delete_org_variable,
    "orgListActivityFeeds": lambda m, s: m(s.org),
    "orgUpdateAvatar": lambda m, s: m(s.org, image=TINY_PNG_BASE64),
    "orgDeleteAvatar": lambda m, s: m(s.org),
    "orgBlockUser": _block_org_user,
    "orgListHooks": lambda m, s: m(s.org),
    "orgCreateHook": lambda m, s: m(
        s.org,
        type=pyfj.CreateHookOptionType.FORGEJO,
        config=pyfj.CreateHookOptionConfig(
            url="http://127.0.0.1:1/pyfj-org-created-hook",
            content_type="json",
        ),
        events=["push"],
    ),
    "orgGetHook": lambda m, s: m(s.org, s.hook_for("base", org=s.org)),
    "orgDeleteHook": _delete_org_hook,
    "orgEditHook": lambda m, s: m(s.org, s.hook_for("base", org=s.org), active=True),
    "orgListLabels": lambda m, s: m(s.org),
    "orgCreateLabel": lambda m, s: m(s.org, name=s.name("label", "created"), color="#112233"),
    "orgGetLabel": lambda m, s: m(s.org, s.org_label_for("base")),
    "orgDeleteLabel": _delete_org_label,
    "orgEditLabel": lambda m, s: m(s.org, s.org_label_for("base"), description="edited by smoke"),
    "orgListBlockedUsers": _list_blocked_org_user,
    "orgListMembers": lambda m, s: m(s.org),
    "orgIsMember": _check_membership,
    "orgDeleteMember": _remove_org_member,
    "orgListPublicMembers": lambda m, s: m(s.org),
    "orgIsPublicMember": _check_org_public_member,
    "orgPublicizeMember": _publicize_member,
    "orgConcealMember": _conceal_member,
    "orgGetQuota": lambda m, s: m(s.org),
    "orgListQuotaArtifacts": lambda m, s: m(s.org),
    "orgListQuotaAttachments": lambda m, s: m(s.org),
    "orgCheckQuota": lambda m, s: m(s.org, subject="size:all"),
    "orgListQuotaPackages": lambda m, s: m(s.org),
    "renameOrg": lambda m, s: m(s.org_for("rename"), new_name=s.name("org", "renamed")),
    "orgListRepos": lambda m, s: m(s.org),
    "createOrgRepo": lambda m, s: m(s.org, name=s.name("repo", "org-created"), auto_init=True),
    "orgListTeams": lambda m, s: m(s.org),
    "orgCreateTeam": lambda m, s: m(s.org, name=s.name("team", "created"), units=["repo.code"]),
    "teamSearch": lambda m, s: m(s.org, q=s.run_id),
    "orgUnblockUser": _unblock_org_user,
}

# ---------------------------------------------------------------------------- teams

_TEAMS = {
    "orgGetTeam": lambda m, s: m(s.team_id),
    "orgDeleteTeam": lambda m, s: m(s.team_for("delete")),
    "orgEditTeam": lambda m, s: m(s.team_id, name=s.name("team", "base"), description="edited by smoke"),
    "orgListTeamActivityFeeds": lambda m, s: m(s.team_id),
    "orgListTeamMembers": lambda m, s: m(s.team_id),
    "orgListTeamMember": lambda m, s: m(s.team_id, s.user),
    "orgAddTeamMember": lambda m, s: m(s.team_for("add-member"), s.user),
    "orgRemoveTeamMember": _remove_team_member,
    "orgListTeamRepos": lambda m, s: m(s.team_with_repo),
    "orgListTeamRepo": lambda m, s: m(s.team_with_repo, s.repo.owner, s.repo.name),
    "orgAddTeamRepository": lambda m, s: m(s.team_for("add-repo"), s.repo.owner, s.repo.name),
    "orgRemoveTeamRepository": _remove_team_repository,
}

# ---------------------------------------------------------------------------- repos

_REPOS = {
    "issueSearchIssues": lambda m, s: m(),
    "repoMigrate": _migrate_repo,
    "repoSearch": lambda m, s: m(q="pyfj"),
    "repoGet": lambda m, s: m(*s.repo.args),
    "repoDelete": lambda m, s: m(*s.repo_for("delete").args),
    "repoEdit": lambda m, s: m(*s.repo.args, description="edited by smoke"),
    "ListActionArtifacts": lambda m, s: m(*s.repo.args),
    "getRepoRunners": lambda m, s: m(*s.repo.args),
    "registerRepoRunner": lambda m, s: m(*s.repo.args, name=s.name("runner", "repo")),
    "repoGetRunnerRegistrationToken": lambda m, s: m(*s.repo.args),
    "getRepoRunner": lambda m, s: m(*s.repo.args, s.runner_for("base", scope="repo", repo=s.repo)),
    "deleteRepoRunner": lambda m, s: m(*s.repo.args, s.runner_for("delete", scope="repo", repo=s.repo)),
    "ListActionRuns": lambda m, s: m(*s.repo.args),
    "repoListActionsSecrets": lambda m, s: m(*s.repo.args),
    "updateRepoSecret": lambda m, s: m(*s.repo.args, s.secret_name("repo-update"), data="dmFsdWU="),
    "deleteRepoSecret": _delete_repo_secret,
    "ListActionTasks": lambda m, s: m(*s.repo.args),
    "getRepoVariablesList": lambda m, s: m(*s.repo.args),
    "getRepoVariable": lambda m, s: m(*s.repo.args, s.repo_variable_for(s.repo, "base")),
    "updateRepoVariable": lambda m, s: m(
        *s.repo.args,
        s.repo_variable_for(s.repo, "base"),
        name=s.repo_variable_for(s.repo, "base"),
        value="two",
    ),
    "createRepoVariable": lambda m, s: m(*s.repo.args, s.variable_name("repo-created"), value="one"),
    "deleteRepoVariable": _delete_repo_variable,
    "DispatchWorkflow": _dispatch_workflow,
    "repoListActivityFeeds": lambda m, s: m(*s.repo.args),
    "repoGetArchive": lambda m, s: m(*s.repo.args, "main.zip"),
    "repoGetAssignees": lambda m, s: m(*s.repo.args),
    "repoUpdateAvatar": lambda m, s: m(*s.repo.args, image=TINY_PNG_BASE64),
    "repoDeleteAvatar": lambda m, s: m(*s.repo.args),
    "repoListBranchProtection": lambda m, s: m(*s.repo.args),
    "repoCreateBranchProtection": lambda m, s: m(*s.repo.args, branch_name="pyfj-protected", enable_push=False),
    "repoGetBranchProtection": lambda m, s: m(*s.repo.args, s.branch_protection_for(s.repo, "base")),
    "repoDeleteBranchProtection": _delete_branch_protection,
    "repoEditBranchProtection": lambda m, s: m(
        *s.repo.args,
        s.branch_protection_for(s.repo, "base"),
        enable_push=True,
    ),
    "repoListBranches": lambda m, s: m(*s.repo.args),
    "repoCreateBranch": lambda m, s: m(*s.repo.args, new_branch_name="pyfj-smoke-branch", old_branch_name="main"),
    "repoGetBranch": lambda m, s: m(*s.repo.args, "main"),
    "repoDeleteBranch": _delete_branch,
    "repoUpdateBranch": _update_branch_name,
    "repoListCollaborators": lambda m, s: m(*s.repo.args),
    "repoCheckCollaborator": _check_collaborator,
    "repoAddCollaborator": lambda m, s: m(
        *s.repo.args,
        USER_USERNAME,
        permission=pyfj.AddCollaboratorOptionPermission.READ,
    ),
    "repoDeleteCollaborator": _remove_collaborator,
    "repoGetRepoPermissions": lambda m, s: m(*s.repo.args, USER_USERNAME),
    "repoGetAllCommits": lambda m, s: m(*s.repo.args),
    "repoGetCombinedStatusByRef": lambda m, s: m(*s.repo.args, "main"),
    "repoListStatusesByRef": lambda m, s: m(*s.repo.args, "main"),
    "repoGetCommitPullRequest": lambda m, s: m(*s.merged_pull_commit[0].args, s.merged_pull_commit[1]),
    "repoCompareDiff": lambda m, s: m(*s.repo.args, f"main...{s.branch}"),
    "repoGetContentsList": lambda m, s: m(*s.repo.args),
    "repoChangeFiles": _change_files,
    "repoGetContents": lambda m, s: m(*s.repo.args, "README.md"),
    "repoUpdateFile": _update_file,
    "repoCreateFile": lambda m, s: m(
        *s.repo.args,
        f"{s.name('file', 'created')}.txt",
        content="Y3JlYXRlZA==",
        message="create pyfj file",
    ),
    "repoDeleteFile": _delete_file,
    "repoApplyDiffPatch": _apply_diff_patch,
    "repoGetEditorConfig": lambda m, s: m(*s.editorconfig_repo.args, ".editorconfig"),
    "repoListFlags": lambda m, s: m(*s.repo.args),
    "repoReplaceAllFlags": lambda m, s: m(*s.repo.args, flags=["pyfj-flag-a", "pyfj-flag-b"]),
    "repoDeleteAllFlags": _delete_all_flags,
    "repoCheckFlag": _check_flag,
    "repoAddFlag": lambda m, s: m(*s.repo.args, "pyfj-added-flag"),
    "repoDeleteFlag": _remove_flag,
    "listForks": lambda m, s: m(*s.repo.args),
    "createFork": lambda m, s: m(*s.repo.args, name=s.name("repo", "fork-created")),
    "GetBlobs": lambda m, s: m(*s.repo.args, shas=[s.file_sha]),
    "GetBlob": lambda m, s: m(*s.repo.args, s.file_sha),
    "repoGetSingleCommit": lambda m, s: m(*s.repo.args, s.main_sha),
    "repoDownloadCommitDiffOrPatch": lambda m, s: m(*s.repo.args, s.main_sha, "diff"),
    "repoGetNote": _note_then_get,
    "repoSetNote": lambda m, s: m(*s.repo.args, s.main_sha, message="pyfj note"),
    "repoRemoveNote": _note_then_delete,
    "repoListAllGitRefs": lambda m, s: m(*s.repo.args),
    "repoListGitRefs": lambda m, s: m(*s.repo.args, "heads/main"),
    "GetAnnotatedTag": lambda m, s: m(*s.repo.args, s.annotated_tag_sha),
    "GetTree": lambda m, s: m(*s.repo.args, s.main_sha, recursive=True),
    "repoListHooks": lambda m, s: m(*s.repo.args),
    "repoCreateHook": lambda m, s: m(
        *s.repo.args,
        type=pyfj.CreateHookOptionType.FORGEJO,
        config=pyfj.CreateHookOptionConfig(
            url="http://127.0.0.1:1/pyfj-created-hook",
            content_type="json",
        ),
        events=["push"],
    ),
    "repoListGitHooks": lambda m, s: m(*s.repo.args),
    "repoGetGitHook": lambda m, s: m(*s.repo_for("git-hook-get").args, "pre-receive"),
    "repoDeleteGitHook": lambda m, s: m(*s.repo_for("git-hook-delete").args, "pre-receive"),
    "repoEditGitHook": lambda m, s: m(
        *s.repo_for("git-hook-edit").args,
        "pre-receive",
        content="#!/bin/sh\nexit 0\n",
    ),
    "repoGetHook": lambda m, s: m(*s.repo.args, s.repo_hook_id),
    "repoDeleteHook": _delete_repo_hook,
    "repoEditHook": lambda m, s: m(*s.repo.args, s.repo_hook_id, active=True),
    "repoGetIssueConfig": lambda m, s: m(*s.repo.args),
    "repoValidateIssueConfig": lambda m, s: m(*s.repo.args),
    "repoGetIssueTemplates": lambda m, s: m(*s.issue_template_repo.args),
    "issueListIssues": lambda m, s: m(*s.repo.args),
    "issueCreateIssue": lambda m, s: m(*s.repo.args, title=s.name("issue", "created")),
    "issueGetRepoComments": lambda m, s: m(*s.repo.args),
    "issueGetComment": lambda m, s: m(*s.repo.args, s.comment_id),
    "issueDeleteComment": _delete_issue_comment,
    "issueEditComment": lambda m, s: m(*s.repo.args, s.comment_id, body="edited comment"),
    "issueListIssueCommentAttachments": lambda m, s: m(*s.repo.args, s.comment_id),
    "issueCreateIssueCommentAttachment": lambda m, s: m(
        *s.repo.args,
        s.comment_id,
        attachment=("comment-upload.txt", b"comment upload", "text/plain"),
    ),
    "issueGetIssueCommentAttachment": lambda m, s: m(*s.repo.args, s.comment_id, s.comment_attachment_id),
    "issueDeleteIssueCommentAttachment": _delete_comment_asset,
    "issueEditIssueCommentAttachment": lambda m, s: m(
        *s.repo.args,
        s.comment_id,
        s.comment_attachment_id,
        name="renamed-comment.txt",
    ),
    "issueGetCommentReactions": _list_comment_reactions,
    "issuePostCommentReaction": lambda m, s: m(*s.repo.args, s.comment_id, content="+1"),
    "issueDeleteCommentReaction": _delete_comment_reaction,
    "repoListPinnedIssues": lambda m, s: m(*s.repo.args),
    "issueGetIssue": lambda m, s: m(*s.repo.args, s.issue_index),
    "issueDelete": _delete_issue,
    "issueEditIssue": lambda m, s: m(*s.repo.args, s.issue_index, body="edited issue body"),
    "issueListIssueAttachments": lambda m, s: m(*s.repo.args, s.issue_index),
    "issueCreateIssueAttachment": lambda m, s: m(
        *s.repo.args,
        s.issue_index,
        attachment=("issue-upload.txt", b"issue upload", "text/plain"),
    ),
    "issueGetIssueAttachment": lambda m, s: m(*s.repo.args, s.issue_index, s.issue_attachment_id),
    "issueDeleteIssueAttachment": _delete_attached_asset,
    "issueEditIssueAttachment": lambda m, s: m(
        *s.repo.args,
        s.issue_index,
        s.issue_attachment_id,
        name="renamed-issue.txt",
    ),
    "issueListBlocks": lambda m, s: m(*s.repo.args, s.issue_index),
    "issueCreateIssueBlocking": _create_block,
    "issueRemoveIssueBlocking": _block_then_remove,
    "issueGetComments": lambda m, s: m(*s.repo.args, s.issue_index),
    "issueCreateComment": lambda m, s: m(*s.repo.args, s.issue_index, body="smoke comment"),
    "issueDeleteCommentDeprecated": _delete_comment_deprecated,
    "issueEditCommentDeprecated": _edit_comment_deprecated,
    "issueEditIssueDeadline": lambda m, s: m(
        *s.repo.args,
        s.issue_index,
        due_date=datetime(2030, 1, 1, tzinfo=UTC),
    ),
    "issueListIssueDependencies": lambda m, s: m(*s.repo.args, s.issue_index),
    "issueCreateIssueDependencies": _create_dependency,
    "issueRemoveIssueDependencies": _dependency_then_remove,
    "issueGetLabels": lambda m, s: m(*s.repo.args, s.issue_index),
    "issueReplaceLabels": lambda m, s: m(*s.repo.args, s.issue_index, labels=[s.label_id]),
    "issueAddLabel": lambda m, s: m(*s.repo.args, s.issue_index, labels=[s.label_id]),
    "issueClearLabels": lambda m, s: m(*s.repo.args, s.issue_index),
    "issueRemoveLabel": _remove_issue_label,
    "pinIssue": lambda m, s: m(*s.repo.args, s.issue_index),
    "unpinIssue": _pin_then_unpin,
    "moveIssuePin": _move_pin,
    "issueGetIssueReactions": _list_issue_reactions,
    "issuePostIssueReaction": lambda m, s: m(*s.repo.args, s.issue_index, content="+1"),
    "issueDeleteIssueReaction": _delete_reaction,
    "issueDeleteStopWatch": _delete_stopwatch,
    "issueStartStopWatch": lambda m, s: m(*s.repo.args, s.issue_index),
    "issueStopStopWatch": _stop_stopwatch,
    "issueSubscriptions": lambda m, s: m(*s.repo.args, s.issue_index),
    "issueCheckSubscription": lambda m, s: m(*s.repo.args, s.issue_index),
    "issueAddSubscription": lambda m, s: m(*s.repo.args, s.issue_index, USER_USERNAME),
    "issueDeleteSubscription": _unsubscribe_issue_user,
    "issueGetCommentsAndTimeline": lambda m, s: m(*s.repo.args, s.issue_index),
    "issueTrackedTimes": lambda m, s: m(*s.repo.args, s.issue_index),
    "issueAddTime": lambda m, s: m(*s.repo.args, s.issue_index, time=120),
    "issueResetTime": _reset_issue_times,
    "issueDeleteTime": _delete_time,
    "repoListKeys": lambda m, s: m(*s.repo.args),
    "repoCreateKey": lambda m, s: m(
        *s.repo.args,
        title=s.name("deploy-key", "created"),
        key=s.ssh_key_for("repo-key-created"),
    ),
    "repoGetKey": lambda m, s: m(*s.repo.args, s.deploy_key_id),
    "repoDeleteKey": _delete_deploy_key,
    "issueListLabels": lambda m, s: m(*s.repo.args),
    "issueCreateLabel": lambda m, s: m(*s.repo.args, name=s.name("label", "created"), color="#ff00ff"),
    "issueGetLabel": lambda m, s: m(*s.repo.args, s.label_id),
    "issueDeleteLabel": _delete_label,
    "issueEditLabel": lambda m, s: m(*s.repo.args, s.label_id, description="edited by smoke"),
    "repoGetLanguages": lambda m, s: m(*s.repo.args),
    "repoGetRawFileOrLFS": lambda m, s: m(*s.repo.args, "README.md"),
    "issueGetMilestonesList": lambda m, s: m(*s.repo.args),
    "issueCreateMilestone": lambda m, s: m(*s.repo.args, title=s.name("milestone", "created")),
    "issueGetMilestone": lambda m, s: m(*s.repo.args, s.milestone_id),
    "issueDeleteMilestone": _delete_milestone,
    "issueEditMilestone": lambda m, s: m(*s.repo.args, s.milestone_id, description="edited by smoke"),
    "repoNewPinAllowed": lambda m, s: m(*s.repo.args),
    "notifyGetRepoList": lambda m, s: m(*s.repo.args),
    "notifyReadRepoList": lambda m, s: m(*s.repo.args, all=True, to_status="read"),
    "repoListPullRequests": lambda m, s: m(*s.repo.args),
    "repoCreatePullRequest": _create_pull_request,
    "repoListPinnedPullRequests": lambda m, s: m(*s.repo.args),
    "repoGetPullRequestByBaseHead": lambda m, s: m(*s.repo.args, "main", s.branch),
    "repoGetPullRequest": lambda m, s: m(*s.repo.args, s.pull_index),
    "repoEditPullRequest": lambda m, s: m(*s.repo.args, s.pull_index, body="edited pull body"),
    "repoDownloadPullDiffOrPatch": lambda m, s: m(*s.repo.args, s.pull_index, "diff"),
    "repoGetPullRequestCommits": lambda m, s: m(*s.repo.args, s.pull_index),
    "repoGetPullRequestFiles": lambda m, s: m(*s.repo.args, s.pull_index),
    "repoPullRequestIsMerged": _is_merged,
    "repoMergePullRequest": _merge_pull,
    "repoCancelScheduledAutoMerge": _cancel_auto_merge,
    "repoCreatePullReviewRequests": lambda m, s: m(*s.repo.args, s.pull_index, reviewers=[USER_USERNAME]),
    "repoDeletePullReviewRequests": _review_request_then_delete,
    "repoListPullReviews": lambda m, s: m(*s.repo.args, s.pull_index),
    "repoCreatePullReview": lambda m, s: m(
        *s.repo.args,
        s.pull_index,
        body="smoke review",
        event="COMMENT",
    ),
    "repoGetPullReview": lambda m, s: m(*s.repo.args, s.pull_index, s.pending_review(s.base_pull)),
    "repoSubmitPullReview": _submit_review,
    "repoDeletePullReview": _delete_review,
    "repoGetPullReviewComments": lambda m, s: m(*s.repo.args, s.pull_index, s.pending_review(s.base_pull)),
    "repoCreatePullReviewComment": _create_review_comment,
    "repoGetPullReviewComment": _get_review_comment,
    "repoDeletePullReviewComment": _delete_review_comment,
    "repoDismissPullReview": _dismiss_review,
    "repoUnDismissPullReview": _undismiss_review,
    "repoUpdatePullRequest": _update_branch,
    "repoListPushMirrors": lambda m, s: m(*s.repo.args),
    "repoAddPushMirror": _add_push_mirror,
    "repoPushMirrorSync": _push_mirror_sync,
    "repoGetPushMirrorByRemoteName": _get_push_mirror,
    "repoDeletePushMirror": _delete_push_mirror,
    "repoMirrorSync": _mirror_sync,
    "repoConvert": _convert_mirror,
    "repoGetRawFile": lambda m, s: m(*s.repo.args, "README.md"),
    "repoListReleases": lambda m, s: m(*s.repo.args),
    "repoCreateRelease": lambda m, s: m(
        *s.repo_for("release-create").args,
        tag_name=s.name("tag", "created"),
        name="created by smoke",
        target_commitish="main",
    ),
    "repoGetLatestRelease": _latest_release,
    "repoGetReleaseByTag": _release_by_tag,
    "repoDeleteReleaseByTag": _delete_release_by_tag,
    "repoGetRelease": lambda m, s: m(*s.repo.args, s.release_id),
    "repoDeleteRelease": _delete_release,
    "repoEditRelease": lambda m, s: m(*s.repo.args, s.release_id, name="edited release"),
    "repoListReleaseAttachments": lambda m, s: m(*s.repo.args, s.release_id),
    "repoCreateReleaseAttachment": lambda m, s: m(
        *s.repo.args,
        s.release_id,
        attachment=("release-upload.txt", b"release upload", "text/plain"),
    ),
    "repoGetReleaseAttachment": lambda m, s: m(*s.repo.args, s.release_id, s.release_attachment_id),
    "repoDeleteReleaseAttachment": _delete_release_asset,
    "repoEditReleaseAttachment": lambda m, s: m(
        *s.repo.args,
        s.release_id,
        s.release_attachment_id,
        name="renamed-release.txt",
    ),
    "repoGetReviewers": lambda m, s: m(*s.repo.args),
    "repoSigningKey": lambda m, s: m(*s.repo.args),
    "repoListStargazers": lambda m, s: m(*s.repo.args),
    "repoListStatuses": lambda m, s: m(*s.repo.args, s.main_sha),
    "repoCreateStatus": lambda m, s: m(
        *s.repo.args,
        s.main_sha,
        state="success",
        context="pyfj/smoke",
        description="smoke status",
    ),
    "repoListSubscribers": lambda m, s: m(*s.repo.args),
    "userCurrentCheckSubscription": lambda m, s: m(*s.repo.args),
    "userCurrentPutSubscription": lambda m, s: m(*s.repo.args),
    "userCurrentDeleteSubscription": _unwatch_repo,
    "repoSyncForkDefaultInfo": lambda m, s: m(*s.fork.args),
    "repoSyncForkDefault": _sync_fork,
    "repoSyncForkBranchInfo": lambda m, s: m(*s.fork.args, "main"),
    "repoSyncForkBranch": _sync_fork_branch,
    "repoListTagProtection": lambda m, s: m(*s.repo.args),
    "repoCreateTagProtection": lambda m, s: m(
        *s.repo.args,
        name_pattern=f"{s.run_id}-created-*",
        whitelist_usernames=[USER_USERNAME],
    ),
    "repoGetTagProtection": lambda m, s: m(*s.repo.args, s.tag_protection_for(s.repo, "base")),
    "repoDeleteTagProtection": _delete_tag_protection,
    "repoEditTagProtection": lambda m, s: m(
        *s.repo.args,
        s.tag_protection_for(s.repo, "base"),
        name_pattern=f"{s.run_id}-edited-*",
    ),
    "repoListTags": lambda m, s: m(*s.repo.args),
    "repoCreateTag": lambda m, s: m(*s.repo.args, tag_name=s.name("tag", "created-lw"), target=s.main_sha),
    "repoGetTag": _get_tag,
    "repoDeleteTag": _delete_tag,
    "repoListTeams": lambda m, s: m(*s.repo.args),
    "repoCheckTeam": lambda m, s: m(*s.repo.args, s.team_name_for("check-team", repos=[s.repo])),
    "repoAddTeam": lambda m, s: m(*s.repo.args, s.team_name_for("add-to-repo")),
    "repoDeleteTeam": lambda m, s: m(*s.repo.args, s.team_name_for("delete-team", repos=[s.repo])),
    "repoTrackedTimes": lambda m, s: m(*s.repo.args),
    "userTrackedTimes": lambda m, s: m(*s.repo.args, s.user),
    "repoListTopics": lambda m, s: m(*s.repo.args),
    "repoUpdateTopics": lambda m, s: m(*s.repo.args, topics=["pyfj-topic"]),
    "repoAddTopic": lambda m, s: m(*s.repo.args, "pyfj-added-topic"),
    "repoDeleteTopic": _delete_topic,
    "repoTransfer": lambda m, s: m(*s.repo_for("transfer").args, new_owner=USER_USERNAME),
    "repoCreateWikiPage": lambda m, s: m(
        *s.repo_for("wiki-create").args,
        title=s.name("wiki", "created"),
        content_base64="cHlmalB3aWtp",
    ),
    "repoGetWikiPage": lambda m, s: m(*s.repo.args, s.wiki_page_name),
    "repoDeleteWikiPage": _delete_wiki_page,
    "repoEditWikiPage": lambda m, s: m(
        *s.repo.args,
        s.wiki_page_name,
        content_base64="dXBkYXRlZCB3aWtp",
        title=s.wiki_page_name,
    ),
    "repoGetWikiPages": lambda m, s: m(*s.repo.args),
    "repoGetWikiPageRevisions": lambda m, s: m(*s.repo.args, s.wiki_page_name),
    "generateRepo": lambda m, s: m(
        *s.template_repo.args,
        name=s.name("repo", "generated"),
        owner=s.org,
        git_content=True,
    ),
}

# ---------------------------------------------------------------------------- users

_USERS = {
    "userSearch": lambda m, s: m(q=s.run_id),
    "userGet": lambda m, s: m(s.user),
    "userListActivityFeeds": lambda m, s: m(s.user),
    "userListFollowers": lambda m, s: m(s.user),
    "userListFollowing": lambda m, s: m(s.user),
    "userCheckFollowing": _follow_then_check_users,
    "userListGPGKeys": lambda m, s: m(s.user),
    "userGetHeatmapData": lambda m, s: m(s.user),
    "userListKeys": lambda m, s: m(s.user),
    "orgListUserOrgs": lambda m, s: m(s.user),
    "orgGetUserPermissions": lambda m, s: m(s.user, s.org),
    "userListRepos": lambda m, s: m(s.user),
    "userListStarred": lambda m, s: m(s.user),
    "userListSubscriptions": lambda m, s: m(s.user),
    "userGetTokens": lambda m, s: m(s.user),
    "userCreateToken": _create_user_token,
    "userDeleteAccessToken": _delete_user_token,
}

# ----------------------------------------------------------------------------- user

_USER = {
    "userGetCurrent": lambda m, s: m(),
    "getUserRunners": lambda m, s: m(),
    "registerUserRunner": lambda m, s: m(name=s.name("runner", "user")),
    "userGetRunnerRegistrationToken": lambda m, s: m(),
    "getUserRunner": lambda m, s: m(s.runner_for("base", scope="user")),
    "deleteUserRunner": lambda m, s: m(s.runner_for("delete", scope="user")),
    "updateUserSecret": lambda m, s: m(s.secret_name("user-update"), data="dmFsdWU="),
    "deleteUserSecret": _delete_user_secret,
    "getUserVariablesList": lambda m, s: m(),
    "getUserVariable": lambda m, s: m(s.user_variable_for("base")),
    "updateUserVariable": lambda m, s: m(
        s.user_variable_for("base"),
        name=s.user_variable_for("base"),
        value="two",
    ),
    "createUserVariable": lambda m, s: m(s.variable_name("user-created"), value="one"),
    "deleteUserVariable": _delete_user_variable,
    "userGetOAuth2Applications": lambda m, s: m(),
    "userCreateOAuth2Application": lambda m, s: m(
        name=s.name("oauth", "created"),
        redirect_uris=["http://127.0.0.1:1/callback"],
        confidential_client=True,
    ),
    "userGetOAuth2Application": lambda m, s: m(s.oauth_app_for("base")),
    "userDeleteOAuth2Application": lambda m, s: m(s.oauth_app_for("delete")),
    "userUpdateOAuth2Application": lambda m, s: m(
        s.oauth_app_for("base"),
        name=s.name("oauth", "base"),
        redirect_uris=["http://127.0.0.1:1/callback2"],
    ),
    "userUpdateAvatar": lambda m, s: m(image=TINY_PNG_BASE64),
    "userDeleteAvatar": lambda m, s: m(),
    "userBlockUser": lambda m, s: m(s.user_for("user-block")),
    "userListEmails": lambda m, s: m(),
    "userAddEmail": lambda m, s: m(emails=[f"{s.name('email', 'added')}@pyfj.test"]),
    "userDeleteEmail": lambda m, s: m(emails=[s.email_for("user-delete")]),
    "userCurrentListFollowers": lambda m, s: m(),
    "userCurrentListFollowing": lambda m, s: m(),
    "userCurrentCheckFollowing": _follow_then_check,
    "userCurrentPutFollow": lambda m, s: m(s.user_for("followed")),
    "userCurrentDeleteFollow": _delete_follow,
    "getVerificationToken": lambda m, s: m(),
    "userCurrentListGPGKeys": lambda m, s: m(),
    "userListHooks": lambda m, s: m(),
    "userCreateHook": lambda m, s: m(
        type=pyfj.CreateHookOptionType.FORGEJO,
        config=pyfj.CreateHookOptionConfig(
            url="http://127.0.0.1:1/pyfj-user-created-hook",
            content_type="json",
        ),
        events=["push"],
    ),
    "userGetHook": lambda m, s: m(s.hook_for("base")),
    "userDeleteHook": _delete_user_hook,
    "userEditHook": lambda m, s: m(s.hook_for("base"), active=True),
    "userCurrentListKeys": lambda m, s: m(),
    "userCurrentPostKey": lambda m, s: m(
        key=s.ssh_key_for("user-post"),
        title=s.name("user-key", "posted"),
        read_only=True,
    ),
    "userCurrentGetKey": lambda m, s: m(s.user_key_for("base")),
    "userCurrentDeleteKey": lambda m, s: m(s.user_key_for("delete")),
    "userListBlockedUsers": _list_blocked_user,
    "orgListCurrentUserOrgs": lambda m, s: m(),
    "userGetQuota": lambda m, s: m(),
    "userListQuotaArtifacts": lambda m, s: m(),
    "userListQuotaAttachments": lambda m, s: m(),
    "userCheckQuota": lambda m, s: m(subject="size:all"),
    "userListQuotaPackages": lambda m, s: m(),
    "userCurrentListRepos": lambda m, s: m(),
    "createCurrentUserRepo": lambda m, s: m(name=s.name("repo", "user-created"), auto_init=True),
    "getUserSettings": lambda m, s: m(),
    "updateUserSettings": lambda m, s: m(full_name="Pyfj User"),
    "userCurrentListStarred": lambda m, s: m(),
    "userCurrentCheckStarring": _star_then_check,
    "userCurrentPutStar": lambda m, s: m(*s.user_repo_for("star").args),
    "userCurrentDeleteStar": _unstar,
    "userGetStopWatches": lambda m, s: m(),
    "userCurrentListSubscriptions": lambda m, s: m(),
    "userListTeams": lambda m, s: m(),
    "userCurrentTrackedTimes": lambda m, s: m(),
    "userUnblockUser": _unblock_user,
}

#: The complete smoke registry: every generated operation bound by operationId.
EXERCISES: dict[str, SmokeCall] = {
    **_ADMIN,
    **_MISC,
    **_NOTIFICATIONS,
    **_PACKAGES,
    **_SETTINGS,
    **_ORGS,
    **_TEAMS,
    **_REPOS,
    **_USERS,
    **_USER,
}
