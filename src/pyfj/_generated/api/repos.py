"""Generated resource namespaces for the ``repos`` group. Do not edit by hand.

Regenerate with ``python -m codegen``; see docs/development/codegen.md.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from pyfj._generated.models.action_artifact import ActionArtifact
from pyfj._generated.models.action_run import ActionRun
from pyfj._generated.models.action_run_job import ActionRunJob
from pyfj._generated.models.action_runner import ActionRunner
from pyfj._generated.models.action_task_response import ActionTaskResponse
from pyfj._generated.models.action_variable import ActionVariable
from pyfj._generated.models.activity import Activity
from pyfj._generated.models.add_collaborator_option import AddCollaboratorOption
from pyfj._generated.models.add_time_option import AddTimeOption
from pyfj._generated.models.annotated_tag import AnnotatedTag
from pyfj._generated.models.attachment import Attachment
from pyfj._generated.models.branch import Branch
from pyfj._generated.models.branch_protection import BranchProtection
from pyfj._generated.models.change_files_options import ChangeFilesOptions
from pyfj._generated.models.changed_file import ChangedFile
from pyfj._generated.models.combined_status import CombinedStatus
from pyfj._generated.models.comment import Comment
from pyfj._generated.models.commit import Commit
from pyfj._generated.models.commit_status import CommitStatus
from pyfj._generated.models.compare import Compare
from pyfj._generated.models.contents_response import ContentsResponse
from pyfj._generated.models.create_branch_protection_option import CreateBranchProtectionOption
from pyfj._generated.models.create_branch_repo_option import CreateBranchRepoOption
from pyfj._generated.models.create_file_options import CreateFileOptions
from pyfj._generated.models.create_fork_option import CreateForkOption
from pyfj._generated.models.create_hook_option import CreateHookOption
from pyfj._generated.models.create_issue_comment_option import CreateIssueCommentOption
from pyfj._generated.models.create_issue_option import CreateIssueOption
from pyfj._generated.models.create_key_option import CreateKeyOption
from pyfj._generated.models.create_label_option import CreateLabelOption
from pyfj._generated.models.create_milestone_option import CreateMilestoneOption
from pyfj._generated.models.create_or_update_secret_option import CreateOrUpdateSecretOption
from pyfj._generated.models.create_pull_request_option import CreatePullRequestOption
from pyfj._generated.models.create_pull_review_comment import CreatePullReviewComment
from pyfj._generated.models.create_pull_review_options import CreatePullReviewOptions
from pyfj._generated.models.create_push_mirror_option import CreatePushMirrorOption
from pyfj._generated.models.create_release_option import CreateReleaseOption
from pyfj._generated.models.create_status_option import CreateStatusOption
from pyfj._generated.models.create_tag_option import CreateTagOption
from pyfj._generated.models.create_tag_protection_option import CreateTagProtectionOption
from pyfj._generated.models.create_variable_option import CreateVariableOption
from pyfj._generated.models.create_wiki_page_options import CreateWikiPageOptions
from pyfj._generated.models.delete_file_options import DeleteFileOptions
from pyfj._generated.models.delete_labels_option import DeleteLabelsOption
from pyfj._generated.models.deploy_key import DeployKey
from pyfj._generated.models.dismiss_pull_review_options import DismissPullReviewOptions
from pyfj._generated.models.dispatch_workflow_option import DispatchWorkflowOption
from pyfj._generated.models.dispatch_workflow_run import DispatchWorkflowRun
from pyfj._generated.models.edit_attachment_options import EditAttachmentOptions
from pyfj._generated.models.edit_branch_protection_option import EditBranchProtectionOption
from pyfj._generated.models.edit_deadline_option import EditDeadlineOption
from pyfj._generated.models.edit_git_hook_option import EditGitHookOption
from pyfj._generated.models.edit_hook_option import EditHookOption
from pyfj._generated.models.edit_issue_comment_option import EditIssueCommentOption
from pyfj._generated.models.edit_issue_option import EditIssueOption
from pyfj._generated.models.edit_label_option import EditLabelOption
from pyfj._generated.models.edit_milestone_option import EditMilestoneOption
from pyfj._generated.models.edit_pull_request_option import EditPullRequestOption
from pyfj._generated.models.edit_reaction_option import EditReactionOption
from pyfj._generated.models.edit_release_option import EditReleaseOption
from pyfj._generated.models.edit_repo_option import EditRepoOption
from pyfj._generated.models.edit_tag_protection_option import EditTagProtectionOption
from pyfj._generated.models.file_delete_response import FileDeleteResponse
from pyfj._generated.models.file_response import FileResponse
from pyfj._generated.models.files_response import FilesResponse
from pyfj._generated.models.generate_repo_option import GenerateRepoOption
from pyfj._generated.models.git_blob import GitBlob
from pyfj._generated.models.git_hook import GitHook
from pyfj._generated.models.git_tree_response import GitTreeResponse
from pyfj._generated.models.hook import Hook
from pyfj._generated.models.issue import Issue
from pyfj._generated.models.issue_config import IssueConfig
from pyfj._generated.models.issue_config_validation import IssueConfigValidation
from pyfj._generated.models.issue_deadline import IssueDeadline
from pyfj._generated.models.issue_labels_option import IssueLabelsOption
from pyfj._generated.models.issue_meta import IssueMeta
from pyfj._generated.models.issue_template import IssueTemplate
from pyfj._generated.models.label import Label
from pyfj._generated.models.list_action_run_response import ListActionRunResponse
from pyfj._generated.models.merge_pull_request_option import MergePullRequestOption
from pyfj._generated.models.migrate_repo_options import MigrateRepoOptions
from pyfj._generated.models.milestone import Milestone
from pyfj._generated.models.new_issue_pins_allowed import NewIssuePinsAllowed
from pyfj._generated.models.note import Note
from pyfj._generated.models.note_options import NoteOptions
from pyfj._generated.models.notification_thread import NotificationThread
from pyfj._generated.models.pull_request import PullRequest
from pyfj._generated.models.pull_review import PullReview
from pyfj._generated.models.pull_review_comment import PullReviewComment
from pyfj._generated.models.pull_review_request_options import PullReviewRequestOptions
from pyfj._generated.models.push_mirror import PushMirror
from pyfj._generated.models.reaction import Reaction
from pyfj._generated.models.reference import Reference
from pyfj._generated.models.register_runner_options import RegisterRunnerOptions
from pyfj._generated.models.register_runner_response import RegisterRunnerResponse
from pyfj._generated.models.registration_token import RegistrationToken
from pyfj._generated.models.release import Release
from pyfj._generated.models.replace_flags_option import ReplaceFlagsOption
from pyfj._generated.models.repo_collaborator_permission import RepoCollaboratorPermission
from pyfj._generated.models.repo_topic_options import RepoTopicOptions
from pyfj._generated.models.repository import Repository
from pyfj._generated.models.search_results import SearchResults
from pyfj._generated.models.secret import Secret
from pyfj._generated.models.submit_pull_review_options import SubmitPullReviewOptions
from pyfj._generated.models.sync_fork_info import SyncForkInfo
from pyfj._generated.models.tag import Tag
from pyfj._generated.models.tag_protection import TagProtection
from pyfj._generated.models.team import Team
from pyfj._generated.models.timeline_comment import TimelineComment
from pyfj._generated.models.topic_name import TopicName
from pyfj._generated.models.tracked_time import TrackedTime
from pyfj._generated.models.transfer_repo_option import TransferRepoOption
from pyfj._generated.models.update_branch_repo_option import UpdateBranchRepoOption
from pyfj._generated.models.update_file_options import UpdateFileOptions
from pyfj._generated.models.update_repo_avatar_option import UpdateRepoAvatarOption
from pyfj._generated.models.update_variable_option import UpdateVariableOption
from pyfj._generated.models.user import User
from pyfj._generated.models.watch_info import WatchInfo
from pyfj._generated.models.wiki_commit_list import WikiCommitList
from pyfj._generated.models.wiki_page import WikiPage
from pyfj._generated.models.wiki_page_meta_data import WikiPageMetaData
from pyfj._runtime import decode

if TYPE_CHECKING:
    import builtins
    from collections.abc import Mapping
    from datetime import date, datetime
    from typing import Literal

    from pyfj._generated.models.add_collaborator_option import AddCollaboratorOptionPermission
    from pyfj._generated.models.change_file_operation import ChangeFileOperation
    from pyfj._generated.models.commit_date_options import CommitDateOptions
    from pyfj._generated.models.create_hook_option import CreateHookOptionType
    from pyfj._generated.models.create_hook_option_config import CreateHookOptionConfig
    from pyfj._generated.models.create_milestone_option import CreateMilestoneOptionState
    from pyfj._generated.models.external_tracker import ExternalTracker
    from pyfj._generated.models.external_wiki import ExternalWiki
    from pyfj._generated.models.identity import Identity
    from pyfj._generated.models.internal_tracker import InternalTracker
    from pyfj._generated.models.merge_pull_request_option import MergePullRequestOptionDo
    from pyfj._generated.models.migrate_repo_options import MigrateRepoOptionsService
    from pyfj._runtime import AsyncForgejo as _RuntimeAsyncForgejo
    from pyfj._runtime import AsyncPaginated, Paginated
    from pyfj._runtime import Forgejo as _RuntimeForgejo

    FileContent = bytes | str
    FilePart = (
        FileContent
        | tuple[str | None, FileContent]
        | tuple[str | None, FileContent, str | None]
        | tuple[str | None, FileContent, str | None, Mapping[str, str]]
    )


class Repos:
    """The ``repos`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client
        self.actions: ReposActions = ReposActions(client)
        self.activities: ReposActivities = ReposActivities(client)
        self.archive: ReposArchive = ReposArchive(client)
        self.avatar: ReposAvatar = ReposAvatar(client)
        self.branch_protections: ReposBranchProtections = ReposBranchProtections(client)
        self.branches: ReposBranches = ReposBranches(client)
        self.collaborators: ReposCollaborators = ReposCollaborators(client)
        self.commits: ReposCommits = ReposCommits(client)
        self.contents: ReposContents = ReposContents(client)
        self.editorconfig: ReposEditorconfig = ReposEditorconfig(client)
        self.flags: ReposFlags = ReposFlags(client)
        self.forks: ReposForks = ReposForks(client)
        self.git: ReposGit = ReposGit(client)
        self.hooks: ReposHooks = ReposHooks(client)
        self.issue_config: ReposIssueConfig = ReposIssueConfig(client)
        self.issues: ReposIssues = ReposIssues(client)
        self.keys: ReposKeys = ReposKeys(client)
        self.labels: ReposLabels = ReposLabels(client)
        self.media: ReposMedia = ReposMedia(client)
        self.milestones: ReposMilestones = ReposMilestones(client)
        self.notifications: ReposNotifications = ReposNotifications(client)
        self.pulls: ReposPulls = ReposPulls(client)
        self.push_mirrors: ReposPushMirrors = ReposPushMirrors(client)
        self.raw: ReposRaw = ReposRaw(client)
        self.releases: ReposReleases = ReposReleases(client)
        self.statuses: ReposStatuses = ReposStatuses(client)
        self.subscription: ReposSubscription = ReposSubscription(client)
        self.sync_fork: ReposSyncFork = ReposSyncFork(client)
        self.tag_protections: ReposTagProtections = ReposTagProtections(client)
        self.tags: ReposTags = ReposTags(client)
        self.teams: ReposTeams = ReposTeams(client)
        self.times: ReposTimes = ReposTimes(client)
        self.topics: ReposTopics = ReposTopics(client)
        self.wiki: ReposWiki = ReposWiki(client)

    def migrate(
        self,
        *,
        auth_password: str | None = None,
        auth_token: str | None = None,
        auth_username: str | None = None,
        clone_addr: str,
        description: str | None = None,
        issues: bool | None = None,
        labels: bool | None = None,
        lfs: bool | None = None,
        lfs_endpoint: str | None = None,
        milestones: bool | None = None,
        mirror: bool | None = None,
        mirror_interval: str | None = None,
        private: bool | None = None,
        pull_requests: bool | None = None,
        releases: bool | None = None,
        repo_name: str,
        repo_owner: str | None = None,
        service: MigrateRepoOptionsService | None = None,
        uid: int | None = None,
        wiki: bool | None = None,
    ) -> Repository:
        """
        Migrate a remote git repository.

        Args:
            auth_password:
            auth_token:
            auth_username:
            clone_addr:
            description:
            issues:
            labels:
            lfs:
            lfs_endpoint:
            milestones:
            mirror:
            mirror_interval:
            private:
            pull_requests:
            releases:
            repo_name:
            repo_owner: Name of User or Organisation who will own Repo after migration
            service:
            uid: deprecated (only for backwards compatibility)
            wiki:

        Returns:
            Repository.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            ConflictError: 409. The repository with the same name already exists.
            PayloadTooLargeError: 413. QuotaExceeded.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: repoMigrate
        """
        _payload = MigrateRepoOptions(
            auth_password=auth_password,
            auth_token=auth_token,
            auth_username=auth_username,
            clone_addr=clone_addr,
            description=description,
            issues=issues,
            labels=labels,
            lfs=lfs,
            lfs_endpoint=lfs_endpoint,
            milestones=milestones,
            mirror=mirror,
            mirror_interval=mirror_interval,
            private=private,
            pull_requests=pull_requests,
            releases=releases,
            repo_name=repo_name,
            repo_owner=repo_owner,
            service=service,
            uid=uid,
            wiki=wiki,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = self._client._request("POST", "/repos/migrate", json=_payload)
        return decode(_response, Repository)

    def search(
        self,
        *,
        q: str | None = None,
        topic: bool | None = None,
        include_desc: bool | None = None,
        uid: int | None = None,
        priority_owner_id: int | None = None,
        team_id: int | None = None,
        starred_by: int | None = None,
        private: bool | None = None,
        is_private: bool | None = None,
        template: bool | None = None,
        archived: bool | None = None,
        mode: str | None = None,
        exclusive: bool | None = None,
        sort: Literal["alpha", "created", "updated", "size", "git_size", "lfs_size", "id", "stars", "forks"]
        | None = None,
        order: Literal["asc", "desc"] | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> SearchResults:
        """
        Search for repositories.

        Args:
            q: keyword
            topic: Limit search to repositories with keyword as topic
            include_desc: include search of keyword within repository description
            uid: search only for repos that the user with the given id owns or contributes to
            priority_owner_id: repo owner to prioritize in the results
            team_id: search only for repos that belong to the given team id
            starred_by: search only for repos that the user with the given id has starred
            private: include private repositories this user has access to (defaults to true)
            is_private: show only public, private or all repositories (defaults to all)
            template: show only template, non-template or all repositories (defaults to all)
            archived: show only archived, non-archived or all repositories (defaults to all)
            mode: type of repository to search for. Supported values are "fork", "source", "mirror" and "collaborative"
            exclusive: if `uid` is given, search only for repos that the user owns
            sort: sort repos by attribute. Supported values are "alpha", "created", "updated", "size", "git_size",
                "lfs_size", "stars", "forks" and "id". Default is "alpha"
            order: sort order, either "asc" (ascending) or "desc" (descending). Default is "asc", ignored if "sort" is
                not specified.
            page: page number of results to return (1-based)
            limit: page size of results

        Returns:
            SearchResults.

        Raises:
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: repoSearch
        """
        _query: dict[str, object] = {
            "q": q,
            "topic": topic,
            "includeDesc": include_desc,
            "uid": uid,
            "priority_owner_id": priority_owner_id,
            "team_id": team_id,
            "starredBy": starred_by,
            "private": private,
            "is_private": is_private,
            "template": template,
            "archived": archived,
            "mode": mode,
            "exclusive": exclusive,
            "sort": sort,
            "order": order,
            "page": page,
            "limit": limit,
        }

        _response = self._client._request("GET", "/repos/search", params=_query)
        return decode(_response, SearchResults)

    def get(self, owner: str, repo: str) -> Repository:
        """
        Get a repository.

        Args:
            owner: owner of the repo
            repo: name of the repo

        Returns:
            Repository.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoGet
        """
        _response = self._client._request("GET", f"/repos/{owner}/{repo}")
        return decode(_response, Repository)

    def update(
        self,
        owner: str,
        repo: str,
        *,
        allow_fast_forward_only_merge: bool | None = None,
        allow_manual_merge: bool | None = None,
        allow_merge_commits: bool | None = None,
        allow_rebase: bool | None = None,
        allow_rebase_explicit: bool | None = None,
        allow_rebase_update: bool | None = None,
        allow_squash_merge: bool | None = None,
        archived: bool | None = None,
        autodetect_manual_merge: bool | None = None,
        default_allow_maintainer_edit: bool | None = None,
        default_branch: str | None = None,
        default_delete_branch_after_merge: bool | None = None,
        default_merge_style: str | None = None,
        default_update_style: str | None = None,
        description: str | None = None,
        enable_prune: bool | None = None,
        external_tracker: ExternalTracker | None = None,
        external_wiki: ExternalWiki | None = None,
        globally_editable_wiki: bool | None = None,
        has_actions: bool | None = None,
        has_issues: bool | None = None,
        has_packages: bool | None = None,
        has_projects: bool | None = None,
        has_pull_requests: bool | None = None,
        has_releases: bool | None = None,
        has_wiki: bool | None = None,
        ignore_whitespace_conflicts: bool | None = None,
        internal_tracker: InternalTracker | None = None,
        mirror_interval: str | None = None,
        name: str | None = None,
        private: bool | None = None,
        template: bool | None = None,
        website: str | None = None,
        wiki_branch: str | None = None,
    ) -> Repository:
        """
        Edit a repository's properties. Only fields that are set will be changed.

        Args:
            owner: owner of the repo to edit
            repo: name of the repo to edit
            allow_fast_forward_only_merge: either `true` to allow fast-forward-only merging pull requests, or `false` to
                prevent fast-forward-only merging.
            allow_manual_merge: either `true` to allow mark pr as merged manually, or `false` to prevent it.
            allow_merge_commits: either `true` to allow merging pull requests with a merge commit, or `false` to prevent
                merging pull requests with merge commits.
            allow_rebase: either `true` to allow rebase-merging pull requests, or `false` to prevent rebase-merging.
            allow_rebase_explicit: either `true` to allow rebase with explicit merge commits (--no-ff), or `false` to
                prevent rebase with explicit merge commits.
            allow_rebase_update: either `true` to allow updating pull request branch by rebase, or `false` to prevent
                it.
            allow_squash_merge: either `true` to allow squash-merging pull requests, or `false` to prevent
                squash-merging.
            archived: set to `true` to archive this repository.
            autodetect_manual_merge: either `true` to enable AutodetectManualMerge, or `false` to prevent it. Note: In
                some special cases, misjudgments can occur.
            default_allow_maintainer_edit: set to `true` to allow edits from maintainers by default
            default_branch: sets the default branch for this repository.
            default_delete_branch_after_merge: set to `true` to delete pr branch after merge by default
            default_merge_style: set to a merge style to be used by this repository: "merge", "rebase", "rebase-merge",
                "squash", "fast-forward-only", "manually-merged", or "rebase-update-only".
            default_update_style: set to a update style to be used by this repository: "rebase" or "merge"
            description: a short description of the repository.
            enable_prune: enable prune - remove obsolete remote-tracking references when mirroring
            external_tracker:
            external_wiki:
            globally_editable_wiki: set the globally editable state of the wiki
            has_actions: either `true` to enable actions unit, or `false` to disable them.
            has_issues: either `true` to enable issues for this repository or `false` to disable them.
            has_packages: either `true` to enable packages unit, or `false` to disable them.
            has_projects: either `true` to enable project unit, or `false` to disable them.
            has_pull_requests: either `true` to allow pull requests, or `false` to prevent pull request.
            has_releases: either `true` to enable releases unit, or `false` to disable them.
            has_wiki: either `true` to enable the wiki for this repository or `false` to disable it.
            ignore_whitespace_conflicts: either `true` to ignore whitespace for conflicts, or `false` to not ignore
                whitespace.
            internal_tracker:
            mirror_interval: set to a string like `8h30m0s` to set the mirror interval time
            name: name of the repository
            private: either `true` to make the repository private or `false` to make it public. Note: you will get a 422
                error if the organization restricts changing repository visibility to organization owners and a
                non-owner tries to change the value of private.
            template: either `true` to make this repository a template or `false` to make it a normal repository
            website: a URL with more information about the repository.
            wiki_branch: sets the branch used for this repository's wiki.

        Returns:
            Repository.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: repoEdit
        """
        if (
            allow_fast_forward_only_merge is not None
            or allow_manual_merge is not None
            or allow_merge_commits is not None
            or allow_rebase is not None
            or allow_rebase_explicit is not None
            or allow_rebase_update is not None
            or allow_squash_merge is not None
            or archived is not None
            or autodetect_manual_merge is not None
            or default_allow_maintainer_edit is not None
            or default_branch is not None
            or default_delete_branch_after_merge is not None
            or default_merge_style is not None
            or default_update_style is not None
            or description is not None
            or enable_prune is not None
            or external_tracker is not None
            or external_wiki is not None
            or globally_editable_wiki is not None
            or has_actions is not None
            or has_issues is not None
            or has_packages is not None
            or has_projects is not None
            or has_pull_requests is not None
            or has_releases is not None
            or has_wiki is not None
            or ignore_whitespace_conflicts is not None
            or internal_tracker is not None
            or mirror_interval is not None
            or name is not None
            or private is not None
            or template is not None
            or website is not None
            or wiki_branch is not None
        ):
            _payload = EditRepoOption(
                allow_fast_forward_only_merge=allow_fast_forward_only_merge,
                allow_manual_merge=allow_manual_merge,
                allow_merge_commits=allow_merge_commits,
                allow_rebase=allow_rebase,
                allow_rebase_explicit=allow_rebase_explicit,
                allow_rebase_update=allow_rebase_update,
                allow_squash_merge=allow_squash_merge,
                archived=archived,
                autodetect_manual_merge=autodetect_manual_merge,
                default_allow_maintainer_edit=default_allow_maintainer_edit,
                default_branch=default_branch,
                default_delete_branch_after_merge=default_delete_branch_after_merge,
                default_merge_style=default_merge_style,
                default_update_style=default_update_style,
                description=description,
                enable_prune=enable_prune,
                external_tracker=external_tracker,
                external_wiki=external_wiki,
                globally_editable_wiki=globally_editable_wiki,
                has_actions=has_actions,
                has_issues=has_issues,
                has_packages=has_packages,
                has_projects=has_projects,
                has_pull_requests=has_pull_requests,
                has_releases=has_releases,
                has_wiki=has_wiki,
                ignore_whitespace_conflicts=ignore_whitespace_conflicts,
                internal_tracker=internal_tracker,
                mirror_interval=mirror_interval,
                name=name,
                private=private,
                template=template,
                website=website,
                wiki_branch=wiki_branch,
            ).model_dump(mode="json", by_alias=True, exclude_none=True)
        else:
            _payload = None

        _response = self._client._request("PATCH", f"/repos/{owner}/{repo}", json=_payload)
        return decode(_response, Repository)

    def delete(self, owner: str, repo: str) -> None:
        """
        Delete a repository.

        Args:
            owner: owner of the repo to delete
            repo: name of the repo to delete

        Returns:
            No content.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoDelete
        """
        _response = self._client._request("DELETE", f"/repos/{owner}/{repo}")
        return decode(_response, None)

    def assignees(self, owner: str, repo: str) -> builtins.list[User]:
        """
        Return all users that have write access and can be assigned to issues.

        Args:
            owner: owner of the repo
            repo: name of the repo

        Returns:
            UserList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoGetAssignees
        """
        _response = self._client._request("GET", f"/repos/{owner}/{repo}/assignees")
        return decode(_response, list[User])

    def compare(self, owner: str, repo: str, basehead: str) -> Compare:
        """
        Get commit comparison information.

        Args:
            owner: owner of the repo
            repo: name of the repo
            basehead: compare two branches or commits

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoCompareDiff
        """
        _response = self._client._request("GET", f"/repos/{owner}/{repo}/compare/{basehead}")
        return decode(_response, Compare)

    def convert(self, owner: str, repo: str) -> Repository:
        """
        Convert a mirror repo to a normal repo.

        Args:
            owner: owner of the repo to convert
            repo: name of the repo to convert

        Returns:
            Repository.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: repoConvert
        """
        _response = self._client._request("POST", f"/repos/{owner}/{repo}/convert")
        return decode(_response, Repository)

    def apply_diff_patch(
        self,
        owner: str,
        repo: str,
        *,
        author: Identity | None = None,
        branch: str | None = None,
        committer: Identity | None = None,
        content: str,
        dates: CommitDateOptions | None = None,
        force_overwrite_new_branch: bool | None = None,
        from_path: str | None = None,
        message: str | None = None,
        new_branch: str | None = None,
        sha: str,
        signoff: bool | None = None,
    ) -> FileResponse:
        """
        Apply diff patch to repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            author:
            branch: branch (optional) to base this file from. if not given, the default branch is used
            committer:
            content: content must be base64 encoded
            dates:
            force_overwrite_new_branch: (optional) will do a force-push if the new branch already exists
            from_path: from_path (optional) is the path of the original file which will be moved/renamed to the path in
                the URL
            message: message (optional) for the commit of this file. if not supplied, a default message will be used
            new_branch: new_branch (optional) will make a new branch from `branch` before creating the file
            sha: sha is the SHA for the file that already exists
            signoff: Add a Signed-off-by trailer by the committer at the end of the commit log message.

        Returns:
            FileResponse.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.
            PayloadTooLargeError: 413. QuotaExceeded.
            LockedError: 423. APIRepoArchivedError is an error that is raised when an archived repo should be modified.

        Operation ID: repoApplyDiffPatch
        """
        _payload = UpdateFileOptions(
            author=author,
            branch=branch,
            committer=committer,
            content=content,
            dates=dates,
            force_overwrite_new_branch=force_overwrite_new_branch,
            from_path=from_path,
            message=message,
            new_branch=new_branch,
            sha=sha,
            signoff=signoff,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = self._client._request("POST", f"/repos/{owner}/{repo}/diffpatch", json=_payload)
        return decode(_response, FileResponse)

    def issue_templates(self, owner: str, repo: str) -> builtins.list[IssueTemplate]:
        """
        Get available issue templates for a repository.

        Args:
            owner: owner of the repo
            repo: name of the repo

        Returns:
            IssueTemplates.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoGetIssueTemplates
        """
        _response = self._client._request("GET", f"/repos/{owner}/{repo}/issue_templates")
        return decode(_response, list[IssueTemplate])

    def languages(self, owner: str, repo: str) -> dict[str, int]:
        """
        Get languages and number of bytes of code written.

        Args:
            owner: owner of the repo
            repo: name of the repo

        Returns:
            LanguageStatistics.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoGetLanguages
        """
        _response = self._client._request("GET", f"/repos/{owner}/{repo}/languages")
        return decode(_response, dict[str, int])

    def mirror_sync(self, owner: str, repo: str) -> None:
        """
        Sync a mirrored repository.

        Args:
            owner: owner of the repo to sync
            repo: name of the repo to sync

        Returns:
            No content.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.
            PayloadTooLargeError: 413. QuotaExceeded.

        Operation ID: repoMirrorSync
        """
        _response = self._client._request("POST", f"/repos/{owner}/{repo}/mirror-sync")
        return decode(_response, None)

    def new_pin_allowed(self, owner: str, repo: str) -> NewIssuePinsAllowed:
        """
        Returns if new Issue Pins are allowed.

        Args:
            owner: owner of the repo
            repo: name of the repo

        Returns:
            RepoNewIssuePinsAllowed.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoNewPinAllowed
        """
        _response = self._client._request("GET", f"/repos/{owner}/{repo}/new_pin_allowed")
        return decode(_response, NewIssuePinsAllowed)

    def push_mirrors_sync(self, owner: str, repo: str) -> None:
        """
        Sync all push mirrored repository.

        Args:
            owner: owner of the repo to sync
            repo: name of the repo to sync

        Returns:
            No content.

        Raises:
            BadRequestError: 400. APIError is error format response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.
            PayloadTooLargeError: 413. QuotaExceeded.

        Operation ID: repoPushMirrorSync
        """
        _response = self._client._request("POST", f"/repos/{owner}/{repo}/push_mirrors-sync")
        return decode(_response, None)

    def reviewers(self, owner: str, repo: str) -> builtins.list[User]:
        """
        Return all users that can be requested to review in this repo.

        Args:
            owner: owner of the repo
            repo: name of the repo

        Returns:
            UserList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoGetReviewers
        """
        _response = self._client._request("GET", f"/repos/{owner}/{repo}/reviewers")
        return decode(_response, list[User])

    def signing_key_gpg(self, owner: str, repo: str) -> str:
        """
        Get signing-key.gpg for given repository.

        Args:
            owner: owner of the repo
            repo: name of the repo

        Returns:
            GPG armored public key.

        Operation ID: repoSigningKey
        """
        _response = self._client._request("GET", f"/repos/{owner}/{repo}/signing-key.gpg")
        return decode(_response, str)

    def stargazers(
        self,
        owner: str,
        repo: str,
        *,
        page: int | None = None,
        limit: int | None = None,
    ) -> Paginated[User]:
        """
        List a repo's stargazers.

        Args:
            owner: owner of the repo
            repo: name of the repo
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            UserList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoListStargazers
        """
        return self._client._paginate("GET", f"/repos/{owner}/{repo}/stargazers", model=User, page=page, limit=limit)

    def subscribers(
        self,
        owner: str,
        repo: str,
        *,
        page: int | None = None,
        limit: int | None = None,
    ) -> Paginated[User]:
        """
        List a repo's watchers.

        Args:
            owner: owner of the repo
            repo: name of the repo
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            UserList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoListSubscribers
        """
        return self._client._paginate("GET", f"/repos/{owner}/{repo}/subscribers", model=User, page=page, limit=limit)

    def transfer(
        self,
        owner: str,
        repo: str,
        *,
        new_owner: str,
        team_ids: builtins.list[int] | None = None,
    ) -> Repository:
        """
        Transfer a repo ownership.

        Args:
            owner: owner of the repo to transfer
            repo: name of the repo to transfer
            new_owner:
            team_ids: ID of the team or teams to add to the repository. Teams can only be added to organization-owned
                repositories.

        Returns:
            Repository.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.
            PayloadTooLargeError: 413. QuotaExceeded.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: repoTransfer
        """
        _payload = TransferRepoOption(
            new_owner=new_owner,
            team_ids=team_ids,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = self._client._request("POST", f"/repos/{owner}/{repo}/transfer", json=_payload)
        return decode(_response, Repository)

    def accept_transfer(self, owner: str, repo: str) -> Repository:
        """
        Accept a repo transfer.

        Args:
            owner: owner of the repo to transfer
            repo: name of the repo to transfer

        Returns:
            Repository.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.
            PayloadTooLargeError: 413. QuotaExceeded.

        Operation ID: acceptRepoTransfer
        """
        _response = self._client._request("POST", f"/repos/{owner}/{repo}/transfer/accept")
        return decode(_response, Repository)

    def reject_transfer(self, owner: str, repo: str) -> Repository:
        """
        Reject a repo transfer.

        Args:
            owner: owner of the repo to transfer
            repo: name of the repo to transfer

        Returns:
            Repository.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: rejectRepoTransfer
        """
        _response = self._client._request("POST", f"/repos/{owner}/{repo}/transfer/reject")
        return decode(_response, Repository)

    def generate(
        self,
        template_owner: str,
        template_repo: str,
        *,
        avatar: bool | None = None,
        default_branch: str | None = None,
        description: str | None = None,
        git_content: bool | None = None,
        git_hooks: bool | None = None,
        labels: bool | None = None,
        name: str,
        owner: str,
        private: bool | None = None,
        protected_branch: bool | None = None,
        topics: bool | None = None,
        webhooks: bool | None = None,
    ) -> Repository:
        """
        Create a repository using a template.

        Args:
            template_owner: name of the template repository owner
            template_repo: name of the template repository
            avatar: include avatar of the template repo
            default_branch: Default branch of the new repository
            description: Description of the repository to create
            git_content: include git content of default branch in template repo
            git_hooks: include git hooks in template repo
            labels: include labels in template repo
            name: Name of the repository to create
            owner: The organization or person who will own the new repository
            private: Whether the repository is private
            protected_branch: include protected branches in template repo
            topics: include topics in template repo
            webhooks: include webhooks in template repo

        Returns:
            Repository.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.
            ConflictError: 409. The repository with the same name already exists.
            PayloadTooLargeError: 413. QuotaExceeded.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: generateRepo
        """
        _payload = GenerateRepoOption(
            avatar=avatar,
            default_branch=default_branch,
            description=description,
            git_content=git_content,
            git_hooks=git_hooks,
            labels=labels,
            name=name,
            owner=owner,
            private=private,
            protected_branch=protected_branch,
            topics=topics,
            webhooks=webhooks,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = self._client._request("POST", f"/repos/{template_owner}/{template_repo}/generate", json=_payload)
        return decode(_response, Repository)


class AsyncRepos:
    """The ``repos`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client
        self.actions: AsyncReposActions = AsyncReposActions(client)
        self.activities: AsyncReposActivities = AsyncReposActivities(client)
        self.archive: AsyncReposArchive = AsyncReposArchive(client)
        self.avatar: AsyncReposAvatar = AsyncReposAvatar(client)
        self.branch_protections: AsyncReposBranchProtections = AsyncReposBranchProtections(client)
        self.branches: AsyncReposBranches = AsyncReposBranches(client)
        self.collaborators: AsyncReposCollaborators = AsyncReposCollaborators(client)
        self.commits: AsyncReposCommits = AsyncReposCommits(client)
        self.contents: AsyncReposContents = AsyncReposContents(client)
        self.editorconfig: AsyncReposEditorconfig = AsyncReposEditorconfig(client)
        self.flags: AsyncReposFlags = AsyncReposFlags(client)
        self.forks: AsyncReposForks = AsyncReposForks(client)
        self.git: AsyncReposGit = AsyncReposGit(client)
        self.hooks: AsyncReposHooks = AsyncReposHooks(client)
        self.issue_config: AsyncReposIssueConfig = AsyncReposIssueConfig(client)
        self.issues: AsyncReposIssues = AsyncReposIssues(client)
        self.keys: AsyncReposKeys = AsyncReposKeys(client)
        self.labels: AsyncReposLabels = AsyncReposLabels(client)
        self.media: AsyncReposMedia = AsyncReposMedia(client)
        self.milestones: AsyncReposMilestones = AsyncReposMilestones(client)
        self.notifications: AsyncReposNotifications = AsyncReposNotifications(client)
        self.pulls: AsyncReposPulls = AsyncReposPulls(client)
        self.push_mirrors: AsyncReposPushMirrors = AsyncReposPushMirrors(client)
        self.raw: AsyncReposRaw = AsyncReposRaw(client)
        self.releases: AsyncReposReleases = AsyncReposReleases(client)
        self.statuses: AsyncReposStatuses = AsyncReposStatuses(client)
        self.subscription: AsyncReposSubscription = AsyncReposSubscription(client)
        self.sync_fork: AsyncReposSyncFork = AsyncReposSyncFork(client)
        self.tag_protections: AsyncReposTagProtections = AsyncReposTagProtections(client)
        self.tags: AsyncReposTags = AsyncReposTags(client)
        self.teams: AsyncReposTeams = AsyncReposTeams(client)
        self.times: AsyncReposTimes = AsyncReposTimes(client)
        self.topics: AsyncReposTopics = AsyncReposTopics(client)
        self.wiki: AsyncReposWiki = AsyncReposWiki(client)

    async def migrate(
        self,
        *,
        auth_password: str | None = None,
        auth_token: str | None = None,
        auth_username: str | None = None,
        clone_addr: str,
        description: str | None = None,
        issues: bool | None = None,
        labels: bool | None = None,
        lfs: bool | None = None,
        lfs_endpoint: str | None = None,
        milestones: bool | None = None,
        mirror: bool | None = None,
        mirror_interval: str | None = None,
        private: bool | None = None,
        pull_requests: bool | None = None,
        releases: bool | None = None,
        repo_name: str,
        repo_owner: str | None = None,
        service: MigrateRepoOptionsService | None = None,
        uid: int | None = None,
        wiki: bool | None = None,
    ) -> Repository:
        """
        Migrate a remote git repository.

        Args:
            auth_password:
            auth_token:
            auth_username:
            clone_addr:
            description:
            issues:
            labels:
            lfs:
            lfs_endpoint:
            milestones:
            mirror:
            mirror_interval:
            private:
            pull_requests:
            releases:
            repo_name:
            repo_owner: Name of User or Organisation who will own Repo after migration
            service:
            uid: deprecated (only for backwards compatibility)
            wiki:

        Returns:
            Repository.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            ConflictError: 409. The repository with the same name already exists.
            PayloadTooLargeError: 413. QuotaExceeded.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: repoMigrate
        """
        _payload = MigrateRepoOptions(
            auth_password=auth_password,
            auth_token=auth_token,
            auth_username=auth_username,
            clone_addr=clone_addr,
            description=description,
            issues=issues,
            labels=labels,
            lfs=lfs,
            lfs_endpoint=lfs_endpoint,
            milestones=milestones,
            mirror=mirror,
            mirror_interval=mirror_interval,
            private=private,
            pull_requests=pull_requests,
            releases=releases,
            repo_name=repo_name,
            repo_owner=repo_owner,
            service=service,
            uid=uid,
            wiki=wiki,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = await self._client._request("POST", "/repos/migrate", json=_payload)
        return decode(_response, Repository)

    async def search(
        self,
        *,
        q: str | None = None,
        topic: bool | None = None,
        include_desc: bool | None = None,
        uid: int | None = None,
        priority_owner_id: int | None = None,
        team_id: int | None = None,
        starred_by: int | None = None,
        private: bool | None = None,
        is_private: bool | None = None,
        template: bool | None = None,
        archived: bool | None = None,
        mode: str | None = None,
        exclusive: bool | None = None,
        sort: Literal["alpha", "created", "updated", "size", "git_size", "lfs_size", "id", "stars", "forks"]
        | None = None,
        order: Literal["asc", "desc"] | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> SearchResults:
        """
        Search for repositories.

        Args:
            q: keyword
            topic: Limit search to repositories with keyword as topic
            include_desc: include search of keyword within repository description
            uid: search only for repos that the user with the given id owns or contributes to
            priority_owner_id: repo owner to prioritize in the results
            team_id: search only for repos that belong to the given team id
            starred_by: search only for repos that the user with the given id has starred
            private: include private repositories this user has access to (defaults to true)
            is_private: show only public, private or all repositories (defaults to all)
            template: show only template, non-template or all repositories (defaults to all)
            archived: show only archived, non-archived or all repositories (defaults to all)
            mode: type of repository to search for. Supported values are "fork", "source", "mirror" and "collaborative"
            exclusive: if `uid` is given, search only for repos that the user owns
            sort: sort repos by attribute. Supported values are "alpha", "created", "updated", "size", "git_size",
                "lfs_size", "stars", "forks" and "id". Default is "alpha"
            order: sort order, either "asc" (ascending) or "desc" (descending). Default is "asc", ignored if "sort" is
                not specified.
            page: page number of results to return (1-based)
            limit: page size of results

        Returns:
            SearchResults.

        Raises:
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: repoSearch
        """
        _query: dict[str, object] = {
            "q": q,
            "topic": topic,
            "includeDesc": include_desc,
            "uid": uid,
            "priority_owner_id": priority_owner_id,
            "team_id": team_id,
            "starredBy": starred_by,
            "private": private,
            "is_private": is_private,
            "template": template,
            "archived": archived,
            "mode": mode,
            "exclusive": exclusive,
            "sort": sort,
            "order": order,
            "page": page,
            "limit": limit,
        }

        _response = await self._client._request("GET", "/repos/search", params=_query)
        return decode(_response, SearchResults)

    async def get(self, owner: str, repo: str) -> Repository:
        """
        Get a repository.

        Args:
            owner: owner of the repo
            repo: name of the repo

        Returns:
            Repository.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoGet
        """
        _response = await self._client._request("GET", f"/repos/{owner}/{repo}")
        return decode(_response, Repository)

    async def update(
        self,
        owner: str,
        repo: str,
        *,
        allow_fast_forward_only_merge: bool | None = None,
        allow_manual_merge: bool | None = None,
        allow_merge_commits: bool | None = None,
        allow_rebase: bool | None = None,
        allow_rebase_explicit: bool | None = None,
        allow_rebase_update: bool | None = None,
        allow_squash_merge: bool | None = None,
        archived: bool | None = None,
        autodetect_manual_merge: bool | None = None,
        default_allow_maintainer_edit: bool | None = None,
        default_branch: str | None = None,
        default_delete_branch_after_merge: bool | None = None,
        default_merge_style: str | None = None,
        default_update_style: str | None = None,
        description: str | None = None,
        enable_prune: bool | None = None,
        external_tracker: ExternalTracker | None = None,
        external_wiki: ExternalWiki | None = None,
        globally_editable_wiki: bool | None = None,
        has_actions: bool | None = None,
        has_issues: bool | None = None,
        has_packages: bool | None = None,
        has_projects: bool | None = None,
        has_pull_requests: bool | None = None,
        has_releases: bool | None = None,
        has_wiki: bool | None = None,
        ignore_whitespace_conflicts: bool | None = None,
        internal_tracker: InternalTracker | None = None,
        mirror_interval: str | None = None,
        name: str | None = None,
        private: bool | None = None,
        template: bool | None = None,
        website: str | None = None,
        wiki_branch: str | None = None,
    ) -> Repository:
        """
        Edit a repository's properties. Only fields that are set will be changed.

        Args:
            owner: owner of the repo to edit
            repo: name of the repo to edit
            allow_fast_forward_only_merge: either `true` to allow fast-forward-only merging pull requests, or `false` to
                prevent fast-forward-only merging.
            allow_manual_merge: either `true` to allow mark pr as merged manually, or `false` to prevent it.
            allow_merge_commits: either `true` to allow merging pull requests with a merge commit, or `false` to prevent
                merging pull requests with merge commits.
            allow_rebase: either `true` to allow rebase-merging pull requests, or `false` to prevent rebase-merging.
            allow_rebase_explicit: either `true` to allow rebase with explicit merge commits (--no-ff), or `false` to
                prevent rebase with explicit merge commits.
            allow_rebase_update: either `true` to allow updating pull request branch by rebase, or `false` to prevent
                it.
            allow_squash_merge: either `true` to allow squash-merging pull requests, or `false` to prevent
                squash-merging.
            archived: set to `true` to archive this repository.
            autodetect_manual_merge: either `true` to enable AutodetectManualMerge, or `false` to prevent it. Note: In
                some special cases, misjudgments can occur.
            default_allow_maintainer_edit: set to `true` to allow edits from maintainers by default
            default_branch: sets the default branch for this repository.
            default_delete_branch_after_merge: set to `true` to delete pr branch after merge by default
            default_merge_style: set to a merge style to be used by this repository: "merge", "rebase", "rebase-merge",
                "squash", "fast-forward-only", "manually-merged", or "rebase-update-only".
            default_update_style: set to a update style to be used by this repository: "rebase" or "merge"
            description: a short description of the repository.
            enable_prune: enable prune - remove obsolete remote-tracking references when mirroring
            external_tracker:
            external_wiki:
            globally_editable_wiki: set the globally editable state of the wiki
            has_actions: either `true` to enable actions unit, or `false` to disable them.
            has_issues: either `true` to enable issues for this repository or `false` to disable them.
            has_packages: either `true` to enable packages unit, or `false` to disable them.
            has_projects: either `true` to enable project unit, or `false` to disable them.
            has_pull_requests: either `true` to allow pull requests, or `false` to prevent pull request.
            has_releases: either `true` to enable releases unit, or `false` to disable them.
            has_wiki: either `true` to enable the wiki for this repository or `false` to disable it.
            ignore_whitespace_conflicts: either `true` to ignore whitespace for conflicts, or `false` to not ignore
                whitespace.
            internal_tracker:
            mirror_interval: set to a string like `8h30m0s` to set the mirror interval time
            name: name of the repository
            private: either `true` to make the repository private or `false` to make it public. Note: you will get a 422
                error if the organization restricts changing repository visibility to organization owners and a
                non-owner tries to change the value of private.
            template: either `true` to make this repository a template or `false` to make it a normal repository
            website: a URL with more information about the repository.
            wiki_branch: sets the branch used for this repository's wiki.

        Returns:
            Repository.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: repoEdit
        """
        if (
            allow_fast_forward_only_merge is not None
            or allow_manual_merge is not None
            or allow_merge_commits is not None
            or allow_rebase is not None
            or allow_rebase_explicit is not None
            or allow_rebase_update is not None
            or allow_squash_merge is not None
            or archived is not None
            or autodetect_manual_merge is not None
            or default_allow_maintainer_edit is not None
            or default_branch is not None
            or default_delete_branch_after_merge is not None
            or default_merge_style is not None
            or default_update_style is not None
            or description is not None
            or enable_prune is not None
            or external_tracker is not None
            or external_wiki is not None
            or globally_editable_wiki is not None
            or has_actions is not None
            or has_issues is not None
            or has_packages is not None
            or has_projects is not None
            or has_pull_requests is not None
            or has_releases is not None
            or has_wiki is not None
            or ignore_whitespace_conflicts is not None
            or internal_tracker is not None
            or mirror_interval is not None
            or name is not None
            or private is not None
            or template is not None
            or website is not None
            or wiki_branch is not None
        ):
            _payload = EditRepoOption(
                allow_fast_forward_only_merge=allow_fast_forward_only_merge,
                allow_manual_merge=allow_manual_merge,
                allow_merge_commits=allow_merge_commits,
                allow_rebase=allow_rebase,
                allow_rebase_explicit=allow_rebase_explicit,
                allow_rebase_update=allow_rebase_update,
                allow_squash_merge=allow_squash_merge,
                archived=archived,
                autodetect_manual_merge=autodetect_manual_merge,
                default_allow_maintainer_edit=default_allow_maintainer_edit,
                default_branch=default_branch,
                default_delete_branch_after_merge=default_delete_branch_after_merge,
                default_merge_style=default_merge_style,
                default_update_style=default_update_style,
                description=description,
                enable_prune=enable_prune,
                external_tracker=external_tracker,
                external_wiki=external_wiki,
                globally_editable_wiki=globally_editable_wiki,
                has_actions=has_actions,
                has_issues=has_issues,
                has_packages=has_packages,
                has_projects=has_projects,
                has_pull_requests=has_pull_requests,
                has_releases=has_releases,
                has_wiki=has_wiki,
                ignore_whitespace_conflicts=ignore_whitespace_conflicts,
                internal_tracker=internal_tracker,
                mirror_interval=mirror_interval,
                name=name,
                private=private,
                template=template,
                website=website,
                wiki_branch=wiki_branch,
            ).model_dump(mode="json", by_alias=True, exclude_none=True)
        else:
            _payload = None

        _response = await self._client._request("PATCH", f"/repos/{owner}/{repo}", json=_payload)
        return decode(_response, Repository)

    async def delete(self, owner: str, repo: str) -> None:
        """
        Delete a repository.

        Args:
            owner: owner of the repo to delete
            repo: name of the repo to delete

        Returns:
            No content.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoDelete
        """
        _response = await self._client._request("DELETE", f"/repos/{owner}/{repo}")
        return decode(_response, None)

    async def assignees(self, owner: str, repo: str) -> builtins.list[User]:
        """
        Return all users that have write access and can be assigned to issues.

        Args:
            owner: owner of the repo
            repo: name of the repo

        Returns:
            UserList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoGetAssignees
        """
        _response = await self._client._request("GET", f"/repos/{owner}/{repo}/assignees")
        return decode(_response, list[User])

    async def compare(self, owner: str, repo: str, basehead: str) -> Compare:
        """
        Get commit comparison information.

        Args:
            owner: owner of the repo
            repo: name of the repo
            basehead: compare two branches or commits

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoCompareDiff
        """
        _response = await self._client._request("GET", f"/repos/{owner}/{repo}/compare/{basehead}")
        return decode(_response, Compare)

    async def convert(self, owner: str, repo: str) -> Repository:
        """
        Convert a mirror repo to a normal repo.

        Args:
            owner: owner of the repo to convert
            repo: name of the repo to convert

        Returns:
            Repository.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: repoConvert
        """
        _response = await self._client._request("POST", f"/repos/{owner}/{repo}/convert")
        return decode(_response, Repository)

    async def apply_diff_patch(
        self,
        owner: str,
        repo: str,
        *,
        author: Identity | None = None,
        branch: str | None = None,
        committer: Identity | None = None,
        content: str,
        dates: CommitDateOptions | None = None,
        force_overwrite_new_branch: bool | None = None,
        from_path: str | None = None,
        message: str | None = None,
        new_branch: str | None = None,
        sha: str,
        signoff: bool | None = None,
    ) -> FileResponse:
        """
        Apply diff patch to repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            author:
            branch: branch (optional) to base this file from. if not given, the default branch is used
            committer:
            content: content must be base64 encoded
            dates:
            force_overwrite_new_branch: (optional) will do a force-push if the new branch already exists
            from_path: from_path (optional) is the path of the original file which will be moved/renamed to the path in
                the URL
            message: message (optional) for the commit of this file. if not supplied, a default message will be used
            new_branch: new_branch (optional) will make a new branch from `branch` before creating the file
            sha: sha is the SHA for the file that already exists
            signoff: Add a Signed-off-by trailer by the committer at the end of the commit log message.

        Returns:
            FileResponse.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.
            PayloadTooLargeError: 413. QuotaExceeded.
            LockedError: 423. APIRepoArchivedError is an error that is raised when an archived repo should be modified.

        Operation ID: repoApplyDiffPatch
        """
        _payload = UpdateFileOptions(
            author=author,
            branch=branch,
            committer=committer,
            content=content,
            dates=dates,
            force_overwrite_new_branch=force_overwrite_new_branch,
            from_path=from_path,
            message=message,
            new_branch=new_branch,
            sha=sha,
            signoff=signoff,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = await self._client._request("POST", f"/repos/{owner}/{repo}/diffpatch", json=_payload)
        return decode(_response, FileResponse)

    async def issue_templates(self, owner: str, repo: str) -> builtins.list[IssueTemplate]:
        """
        Get available issue templates for a repository.

        Args:
            owner: owner of the repo
            repo: name of the repo

        Returns:
            IssueTemplates.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoGetIssueTemplates
        """
        _response = await self._client._request("GET", f"/repos/{owner}/{repo}/issue_templates")
        return decode(_response, list[IssueTemplate])

    async def languages(self, owner: str, repo: str) -> dict[str, int]:
        """
        Get languages and number of bytes of code written.

        Args:
            owner: owner of the repo
            repo: name of the repo

        Returns:
            LanguageStatistics.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoGetLanguages
        """
        _response = await self._client._request("GET", f"/repos/{owner}/{repo}/languages")
        return decode(_response, dict[str, int])

    async def mirror_sync(self, owner: str, repo: str) -> None:
        """
        Sync a mirrored repository.

        Args:
            owner: owner of the repo to sync
            repo: name of the repo to sync

        Returns:
            No content.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.
            PayloadTooLargeError: 413. QuotaExceeded.

        Operation ID: repoMirrorSync
        """
        _response = await self._client._request("POST", f"/repos/{owner}/{repo}/mirror-sync")
        return decode(_response, None)

    async def new_pin_allowed(self, owner: str, repo: str) -> NewIssuePinsAllowed:
        """
        Returns if new Issue Pins are allowed.

        Args:
            owner: owner of the repo
            repo: name of the repo

        Returns:
            RepoNewIssuePinsAllowed.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoNewPinAllowed
        """
        _response = await self._client._request("GET", f"/repos/{owner}/{repo}/new_pin_allowed")
        return decode(_response, NewIssuePinsAllowed)

    async def push_mirrors_sync(self, owner: str, repo: str) -> None:
        """
        Sync all push mirrored repository.

        Args:
            owner: owner of the repo to sync
            repo: name of the repo to sync

        Returns:
            No content.

        Raises:
            BadRequestError: 400. APIError is error format response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.
            PayloadTooLargeError: 413. QuotaExceeded.

        Operation ID: repoPushMirrorSync
        """
        _response = await self._client._request("POST", f"/repos/{owner}/{repo}/push_mirrors-sync")
        return decode(_response, None)

    async def reviewers(self, owner: str, repo: str) -> builtins.list[User]:
        """
        Return all users that can be requested to review in this repo.

        Args:
            owner: owner of the repo
            repo: name of the repo

        Returns:
            UserList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoGetReviewers
        """
        _response = await self._client._request("GET", f"/repos/{owner}/{repo}/reviewers")
        return decode(_response, list[User])

    async def signing_key_gpg(self, owner: str, repo: str) -> str:
        """
        Get signing-key.gpg for given repository.

        Args:
            owner: owner of the repo
            repo: name of the repo

        Returns:
            GPG armored public key.

        Operation ID: repoSigningKey
        """
        _response = await self._client._request("GET", f"/repos/{owner}/{repo}/signing-key.gpg")
        return decode(_response, str)

    async def stargazers(
        self,
        owner: str,
        repo: str,
        *,
        page: int | None = None,
        limit: int | None = None,
    ) -> AsyncPaginated[User]:
        """
        List a repo's stargazers.

        Args:
            owner: owner of the repo
            repo: name of the repo
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            UserList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoListStargazers
        """
        return await self._client._paginate(
            "GET", f"/repos/{owner}/{repo}/stargazers", model=User, page=page, limit=limit
        )

    async def subscribers(
        self,
        owner: str,
        repo: str,
        *,
        page: int | None = None,
        limit: int | None = None,
    ) -> AsyncPaginated[User]:
        """
        List a repo's watchers.

        Args:
            owner: owner of the repo
            repo: name of the repo
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            UserList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoListSubscribers
        """
        return await self._client._paginate(
            "GET", f"/repos/{owner}/{repo}/subscribers", model=User, page=page, limit=limit
        )

    async def transfer(
        self,
        owner: str,
        repo: str,
        *,
        new_owner: str,
        team_ids: builtins.list[int] | None = None,
    ) -> Repository:
        """
        Transfer a repo ownership.

        Args:
            owner: owner of the repo to transfer
            repo: name of the repo to transfer
            new_owner:
            team_ids: ID of the team or teams to add to the repository. Teams can only be added to organization-owned
                repositories.

        Returns:
            Repository.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.
            PayloadTooLargeError: 413. QuotaExceeded.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: repoTransfer
        """
        _payload = TransferRepoOption(
            new_owner=new_owner,
            team_ids=team_ids,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = await self._client._request("POST", f"/repos/{owner}/{repo}/transfer", json=_payload)
        return decode(_response, Repository)

    async def accept_transfer(self, owner: str, repo: str) -> Repository:
        """
        Accept a repo transfer.

        Args:
            owner: owner of the repo to transfer
            repo: name of the repo to transfer

        Returns:
            Repository.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.
            PayloadTooLargeError: 413. QuotaExceeded.

        Operation ID: acceptRepoTransfer
        """
        _response = await self._client._request("POST", f"/repos/{owner}/{repo}/transfer/accept")
        return decode(_response, Repository)

    async def reject_transfer(self, owner: str, repo: str) -> Repository:
        """
        Reject a repo transfer.

        Args:
            owner: owner of the repo to transfer
            repo: name of the repo to transfer

        Returns:
            Repository.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: rejectRepoTransfer
        """
        _response = await self._client._request("POST", f"/repos/{owner}/{repo}/transfer/reject")
        return decode(_response, Repository)

    async def generate(
        self,
        template_owner: str,
        template_repo: str,
        *,
        avatar: bool | None = None,
        default_branch: str | None = None,
        description: str | None = None,
        git_content: bool | None = None,
        git_hooks: bool | None = None,
        labels: bool | None = None,
        name: str,
        owner: str,
        private: bool | None = None,
        protected_branch: bool | None = None,
        topics: bool | None = None,
        webhooks: bool | None = None,
    ) -> Repository:
        """
        Create a repository using a template.

        Args:
            template_owner: name of the template repository owner
            template_repo: name of the template repository
            avatar: include avatar of the template repo
            default_branch: Default branch of the new repository
            description: Description of the repository to create
            git_content: include git content of default branch in template repo
            git_hooks: include git hooks in template repo
            labels: include labels in template repo
            name: Name of the repository to create
            owner: The organization or person who will own the new repository
            private: Whether the repository is private
            protected_branch: include protected branches in template repo
            topics: include topics in template repo
            webhooks: include webhooks in template repo

        Returns:
            Repository.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.
            ConflictError: 409. The repository with the same name already exists.
            PayloadTooLargeError: 413. QuotaExceeded.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: generateRepo
        """
        _payload = GenerateRepoOption(
            avatar=avatar,
            default_branch=default_branch,
            description=description,
            git_content=git_content,
            git_hooks=git_hooks,
            labels=labels,
            name=name,
            owner=owner,
            private=private,
            protected_branch=protected_branch,
            topics=topics,
            webhooks=webhooks,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = await self._client._request(
            "POST", f"/repos/{template_owner}/{template_repo}/generate", json=_payload
        )
        return decode(_response, Repository)


class ReposActions:
    """The ``repos.actions`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client
        self.artifacts: ReposActionsArtifacts = ReposActionsArtifacts(client)
        self.jobs: ReposActionsJobs = ReposActionsJobs(client)
        self.runners: ReposActionsRunners = ReposActionsRunners(client)
        self.runs: ReposActionsRuns = ReposActionsRuns(client)
        self.secrets: ReposActionsSecrets = ReposActionsSecrets(client)
        self.variables: ReposActionsVariables = ReposActionsVariables(client)
        self.workflows: ReposActionsWorkflows = ReposActionsWorkflows(client)

    def tasks(
        self,
        owner: str,
        repo: str,
        *,
        page: int | None = None,
        limit: int | None = None,
        status: builtins.list[
            Literal["unknown", "waiting", "running", "success", "failure", "cancelled", "skipped", "blocked"]
        ]
        | None = None,
    ) -> ActionTaskResponse:
        """
        List a repository's action tasks.

        Args:
            owner: owner of the repo
            repo: name of the repo
            page: page number of results to return (1-based)
            limit: page size of results, default maximum page size is 50
            status: Returns workflow tasks with the check run status or conclusion that is specified. For example, a
                conclusion can be success or a status can be in_progress.

        Returns:
            TasksList.

        Raises:
            BadRequestError: 400. APIError is error format response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.
            ConflictError: 409. APIConflict is a conflict empty response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: ListActionTasks
        """
        _query: dict[str, object] = {"page": page, "limit": limit, "status": status}

        _response = self._client._request("GET", f"/repos/{owner}/{repo}/actions/tasks", params=_query)
        return decode(_response, ActionTaskResponse)


class AsyncReposActions:
    """The ``repos.actions`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client
        self.artifacts: AsyncReposActionsArtifacts = AsyncReposActionsArtifacts(client)
        self.jobs: AsyncReposActionsJobs = AsyncReposActionsJobs(client)
        self.runners: AsyncReposActionsRunners = AsyncReposActionsRunners(client)
        self.runs: AsyncReposActionsRuns = AsyncReposActionsRuns(client)
        self.secrets: AsyncReposActionsSecrets = AsyncReposActionsSecrets(client)
        self.variables: AsyncReposActionsVariables = AsyncReposActionsVariables(client)
        self.workflows: AsyncReposActionsWorkflows = AsyncReposActionsWorkflows(client)

    async def tasks(
        self,
        owner: str,
        repo: str,
        *,
        page: int | None = None,
        limit: int | None = None,
        status: builtins.list[
            Literal["unknown", "waiting", "running", "success", "failure", "cancelled", "skipped", "blocked"]
        ]
        | None = None,
    ) -> ActionTaskResponse:
        """
        List a repository's action tasks.

        Args:
            owner: owner of the repo
            repo: name of the repo
            page: page number of results to return (1-based)
            limit: page size of results, default maximum page size is 50
            status: Returns workflow tasks with the check run status or conclusion that is specified. For example, a
                conclusion can be success or a status can be in_progress.

        Returns:
            TasksList.

        Raises:
            BadRequestError: 400. APIError is error format response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.
            ConflictError: 409. APIConflict is a conflict empty response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: ListActionTasks
        """
        _query: dict[str, object] = {"page": page, "limit": limit, "status": status}

        _response = await self._client._request("GET", f"/repos/{owner}/{repo}/actions/tasks", params=_query)
        return decode(_response, ActionTaskResponse)


class ReposActionsArtifacts:
    """The ``repos.actions.artifacts`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def list(
        self,
        owner: str,
        repo: str,
        *,
        name: str | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> Paginated[ActionArtifact]:
        """
        List a repository's artifacts.

        Args:
            owner: owner of the repo
            repo: name of the repo
            name: filter by artifact name
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            ActionArtifactList.

        Raises:
            BadRequestError: 400. APIError is error format response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.

        Operation ID: ListActionArtifacts
        """
        _query: dict[str, object] = {"name": name}

        return self._client._paginate(
            "GET",
            f"/repos/{owner}/{repo}/actions/artifacts",
            model=ActionArtifact,
            params=_query,
            page=page,
            limit=limit,
        )

    def get(self, owner: str, repo: str, artifact_id: int) -> ActionArtifact:
        """
        Get an artifact by ID.

        Args:
            owner: owner of the repo
            repo: name of the repo
            artifact_id: ID of the artifact

        Returns:
            ActionArtifact.

        Raises:
            BadRequestError: 400. APIError is error format response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: GetActionArtifact
        """
        _response = self._client._request("GET", f"/repos/{owner}/{repo}/actions/artifacts/{artifact_id}")
        return decode(_response, ActionArtifact)

    def delete(self, owner: str, repo: str, artifact_id: int) -> None:
        """
        Mark an artifact for deletion.

        Marks the artifact for deletion. Storage space will be reclaimed
        asynchronously by a background job.

        Args:
            owner: owner of the repo
            repo: name of the repo
            artifact_id: ID of the artifact

        Returns:
            No content.

        Raises:
            BadRequestError: 400. APIError is error format response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: DeleteActionArtifact
        """
        _response = self._client._request("DELETE", f"/repos/{owner}/{repo}/actions/artifacts/{artifact_id}")
        return decode(_response, None)

    def download(self, owner: str, repo: str, artifact_id: int) -> bytes:
        """
        Download an artifact.

        Args:
            owner: owner of the repo
            repo: name of the repo
            artifact_id: ID of the artifact

        Returns:
            the artifact archive.

        Raises:
            BadRequestError: 400. APIError is error format response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: DownloadActionArtifact
        """
        _response = self._client._request("GET", f"/repos/{owner}/{repo}/actions/artifacts/{artifact_id}/zip")
        return decode(_response, bytes)


class AsyncReposActionsArtifacts:
    """The ``repos.actions.artifacts`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def list(
        self,
        owner: str,
        repo: str,
        *,
        name: str | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> AsyncPaginated[ActionArtifact]:
        """
        List a repository's artifacts.

        Args:
            owner: owner of the repo
            repo: name of the repo
            name: filter by artifact name
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            ActionArtifactList.

        Raises:
            BadRequestError: 400. APIError is error format response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.

        Operation ID: ListActionArtifacts
        """
        _query: dict[str, object] = {"name": name}

        return await self._client._paginate(
            "GET",
            f"/repos/{owner}/{repo}/actions/artifacts",
            model=ActionArtifact,
            params=_query,
            page=page,
            limit=limit,
        )

    async def get(self, owner: str, repo: str, artifact_id: int) -> ActionArtifact:
        """
        Get an artifact by ID.

        Args:
            owner: owner of the repo
            repo: name of the repo
            artifact_id: ID of the artifact

        Returns:
            ActionArtifact.

        Raises:
            BadRequestError: 400. APIError is error format response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: GetActionArtifact
        """
        _response = await self._client._request("GET", f"/repos/{owner}/{repo}/actions/artifacts/{artifact_id}")
        return decode(_response, ActionArtifact)

    async def delete(self, owner: str, repo: str, artifact_id: int) -> None:
        """
        Mark an artifact for deletion.

        Marks the artifact for deletion. Storage space will be reclaimed
        asynchronously by a background job.

        Args:
            owner: owner of the repo
            repo: name of the repo
            artifact_id: ID of the artifact

        Returns:
            No content.

        Raises:
            BadRequestError: 400. APIError is error format response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: DeleteActionArtifact
        """
        _response = await self._client._request("DELETE", f"/repos/{owner}/{repo}/actions/artifacts/{artifact_id}")
        return decode(_response, None)

    async def download(self, owner: str, repo: str, artifact_id: int) -> bytes:
        """
        Download an artifact.

        Args:
            owner: owner of the repo
            repo: name of the repo
            artifact_id: ID of the artifact

        Returns:
            the artifact archive.

        Raises:
            BadRequestError: 400. APIError is error format response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: DownloadActionArtifact
        """
        _response = await self._client._request("GET", f"/repos/{owner}/{repo}/actions/artifacts/{artifact_id}/zip")
        return decode(_response, bytes)


class ReposActionsJobs:
    """The ``repos.actions.jobs`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def logs(self, owner: str, repo: str, job_id: int, *, attempt: int | None = None) -> str:
        """
        Download the plaintext logs of an action job.

        Returns the plaintext log for the job. By default the log for the most recent attempt is returned
        (ActionRunJob.TaskID tracks the latest task). Pass `?attempt=N` to fetch the log for a specific historical
        attempt; the value matches the `attempt` field returned by the job listing endpoints.

        Args:
            owner: owner of the repo
            repo: name of the repo
            job_id: ID of the workflow job
            attempt: 1-based attempt number matching the value of `attempt` in the job listing; omit to fetch the latest
                attempt of the job

        Returns:
            Plaintext log content.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoGetActionJobLogs
        """
        _query: dict[str, object] = {"attempt": attempt}

        _response = self._client._request("GET", f"/repos/{owner}/{repo}/actions/jobs/{job_id}/logs", params=_query)
        return decode(_response, str)


class AsyncReposActionsJobs:
    """The ``repos.actions.jobs`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def logs(self, owner: str, repo: str, job_id: int, *, attempt: int | None = None) -> str:
        """
        Download the plaintext logs of an action job.

        Returns the plaintext log for the job. By default the log for the most recent attempt is returned
        (ActionRunJob.TaskID tracks the latest task). Pass `?attempt=N` to fetch the log for a specific historical
        attempt; the value matches the `attempt` field returned by the job listing endpoints.

        Args:
            owner: owner of the repo
            repo: name of the repo
            job_id: ID of the workflow job
            attempt: 1-based attempt number matching the value of `attempt` in the job listing; omit to fetch the latest
                attempt of the job

        Returns:
            Plaintext log content.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoGetActionJobLogs
        """
        _query: dict[str, object] = {"attempt": attempt}

        _response = await self._client._request(
            "GET", f"/repos/{owner}/{repo}/actions/jobs/{job_id}/logs", params=_query
        )
        return decode(_response, str)


class ReposActionsRunners:
    """The ``repos.actions.runners`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def list(
        self,
        owner: str,
        repo: str,
        *,
        visible: bool | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> Paginated[ActionRunner]:
        """
        Get runners belonging to the repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            visible: whether to include all visible runners (true) or only those that are directly owned by the
                repository (false)
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            ActionRunnerList is a list of Forgejo Action runners.

        Raises:
            BadRequestError: 400. APIError is error format response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: getRepoRunners
        """
        _query: dict[str, object] = {"visible": visible}

        return self._client._paginate(
            "GET", f"/repos/{owner}/{repo}/actions/runners", model=ActionRunner, params=_query, page=page, limit=limit
        )

    def register(
        self,
        owner: str,
        repo: str,
        *,
        description: str | None = None,
        ephemeral: bool | None = None,
        name: str,
    ) -> RegisterRunnerResponse:
        """
        Register a new repository-level runner.

        Args:
            owner: owner of the repo
            repo: name of the repo
            description: Description of the runner to register.
            ephemeral: Register as ephemeral runner
                https://forgejo.org/docs/latest/admin/actions/security/#ephemeral-runner
            name: Name of the runner to register. The name of the runner does not have to be unique.

        Returns:
            RegisterRunnerResponse contains the details of the just registered runner.

        Raises:
            BadRequestError: 400. APIError is error format response.
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: registerRepoRunner
        """
        _payload = RegisterRunnerOptions(
            description=description,
            ephemeral=ephemeral,
            name=name,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = self._client._request("POST", f"/repos/{owner}/{repo}/actions/runners", json=_payload)
        return decode(_response, RegisterRunnerResponse)

    def jobs(self, owner: str, repo: str, *, labels: str | None = None) -> builtins.list[ActionRunJob]:
        """
        Search for repository's action jobs according filter conditions.

        Args:
            owner: owner of the repo
            repo: name of the repo
            labels: a comma separated list of run job labels to search for

        Returns:
            RunJobList is a list of action run jobs.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.

        Operation ID: repoSearchRunJobs
        """
        _query: dict[str, object] = {"labels": labels}

        _response = self._client._request("GET", f"/repos/{owner}/{repo}/actions/runners/jobs", params=_query)
        return decode(_response, list[ActionRunJob])

    def registration_token(self, owner: str, repo: str) -> RegistrationToken:
        """
        Get a repository's runner registration token.

        This operation has been deprecated in Forgejo 15. Use the web UI or
        [`/repos/{owner}/{repo}/actions/runners`](#/repository/registerRepoRunner) instead.

        Args:
            owner: owner of the repo
            repo: name of the repo

        Returns:
            RegistrationToken is a string used to register a runner with a server.

        Deprecated:
            Deprecated in the vendored Spec; generated for compatibility.

        Operation ID: repoGetRunnerRegistrationToken
        """
        _response = self._client._request("GET", f"/repos/{owner}/{repo}/actions/runners/registration-token")
        return decode(_response, RegistrationToken)

    def get(self, owner: str, repo: str, runner_id: str) -> ActionRunner:
        """
        Get a particular runner that belongs to the repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            runner_id: ID of the runner

        Returns:
            ActionRunner represents a runner.

        Raises:
            BadRequestError: 400. APIError is error format response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: getRepoRunner
        """
        _response = self._client._request("GET", f"/repos/{owner}/{repo}/actions/runners/{runner_id}")
        return decode(_response, ActionRunner)

    def delete(self, owner: str, repo: str, runner_id: str) -> None:
        """
        Delete a particular runner that belongs to a repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            runner_id: ID of the runner

        Returns:
            No content.

        Raises:
            BadRequestError: 400. APIError is error format response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: deleteRepoRunner
        """
        _response = self._client._request("DELETE", f"/repos/{owner}/{repo}/actions/runners/{runner_id}")
        return decode(_response, None)


class AsyncReposActionsRunners:
    """The ``repos.actions.runners`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def list(
        self,
        owner: str,
        repo: str,
        *,
        visible: bool | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> AsyncPaginated[ActionRunner]:
        """
        Get runners belonging to the repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            visible: whether to include all visible runners (true) or only those that are directly owned by the
                repository (false)
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            ActionRunnerList is a list of Forgejo Action runners.

        Raises:
            BadRequestError: 400. APIError is error format response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: getRepoRunners
        """
        _query: dict[str, object] = {"visible": visible}

        return await self._client._paginate(
            "GET", f"/repos/{owner}/{repo}/actions/runners", model=ActionRunner, params=_query, page=page, limit=limit
        )

    async def register(
        self,
        owner: str,
        repo: str,
        *,
        description: str | None = None,
        ephemeral: bool | None = None,
        name: str,
    ) -> RegisterRunnerResponse:
        """
        Register a new repository-level runner.

        Args:
            owner: owner of the repo
            repo: name of the repo
            description: Description of the runner to register.
            ephemeral: Register as ephemeral runner
                https://forgejo.org/docs/latest/admin/actions/security/#ephemeral-runner
            name: Name of the runner to register. The name of the runner does not have to be unique.

        Returns:
            RegisterRunnerResponse contains the details of the just registered runner.

        Raises:
            BadRequestError: 400. APIError is error format response.
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: registerRepoRunner
        """
        _payload = RegisterRunnerOptions(
            description=description,
            ephemeral=ephemeral,
            name=name,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = await self._client._request("POST", f"/repos/{owner}/{repo}/actions/runners", json=_payload)
        return decode(_response, RegisterRunnerResponse)

    async def jobs(self, owner: str, repo: str, *, labels: str | None = None) -> builtins.list[ActionRunJob]:
        """
        Search for repository's action jobs according filter conditions.

        Args:
            owner: owner of the repo
            repo: name of the repo
            labels: a comma separated list of run job labels to search for

        Returns:
            RunJobList is a list of action run jobs.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.

        Operation ID: repoSearchRunJobs
        """
        _query: dict[str, object] = {"labels": labels}

        _response = await self._client._request("GET", f"/repos/{owner}/{repo}/actions/runners/jobs", params=_query)
        return decode(_response, list[ActionRunJob])

    async def registration_token(self, owner: str, repo: str) -> RegistrationToken:
        """
        Get a repository's runner registration token.

        This operation has been deprecated in Forgejo 15. Use the web UI or
        [`/repos/{owner}/{repo}/actions/runners`](#/repository/registerRepoRunner) instead.

        Args:
            owner: owner of the repo
            repo: name of the repo

        Returns:
            RegistrationToken is a string used to register a runner with a server.

        Deprecated:
            Deprecated in the vendored Spec; generated for compatibility.

        Operation ID: repoGetRunnerRegistrationToken
        """
        _response = await self._client._request("GET", f"/repos/{owner}/{repo}/actions/runners/registration-token")
        return decode(_response, RegistrationToken)

    async def get(self, owner: str, repo: str, runner_id: str) -> ActionRunner:
        """
        Get a particular runner that belongs to the repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            runner_id: ID of the runner

        Returns:
            ActionRunner represents a runner.

        Raises:
            BadRequestError: 400. APIError is error format response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: getRepoRunner
        """
        _response = await self._client._request("GET", f"/repos/{owner}/{repo}/actions/runners/{runner_id}")
        return decode(_response, ActionRunner)

    async def delete(self, owner: str, repo: str, runner_id: str) -> None:
        """
        Delete a particular runner that belongs to a repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            runner_id: ID of the runner

        Returns:
            No content.

        Raises:
            BadRequestError: 400. APIError is error format response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: deleteRepoRunner
        """
        _response = await self._client._request("DELETE", f"/repos/{owner}/{repo}/actions/runners/{runner_id}")
        return decode(_response, None)


class ReposActionsRuns:
    """The ``repos.actions.runs`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def list(
        self,
        owner: str,
        repo: str,
        *,
        page: int | None = None,
        limit: int | None = None,
        event: builtins.list[str] | None = None,
        status: builtins.list[
            Literal["unknown", "waiting", "running", "success", "failure", "cancelled", "skipped", "blocked"]
        ]
        | None = None,
        run_number: int | None = None,
        head_sha: str | None = None,
        ref: str | None = None,
        workflow_id: str | None = None,
    ) -> ListActionRunResponse:
        """
        List a repository's action runs.

        Args:
            owner: owner of the repo
            repo: name of the repo
            page: page number of results to return (1-based)
            limit: page size of results, default maximum page size is 50
            event: Returns workflow run triggered by the specified events. For example, `push`, `pull_request` or
                `workflow_dispatch`.
            status: Returns workflow runs with the check run status or conclusion that is specified. For example, a
                conclusion can be success or a status can be in_progress. Only Forgejo Actions can set a status of
                waiting, pending, or requested.
            run_number: Returns the workflow run associated with the run number.
            head_sha: Only returns workflow runs that are associated with the specified head_sha.
            ref: Only return workflow runs that involve the given Git reference, for example, `refs/heads/main`.
            workflow_id: Only return workflow runs that involve the given workflow ID.

        Returns:
            ActionRunList.

        Raises:
            BadRequestError: 400. APIError is error format response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.

        Operation ID: ListActionRuns
        """
        _query: dict[str, object] = {
            "page": page,
            "limit": limit,
            "event": event,
            "status": status,
            "run_number": run_number,
            "head_sha": head_sha,
            "ref": ref,
            "workflow_id": workflow_id,
        }

        _response = self._client._request("GET", f"/repos/{owner}/{repo}/actions/runs", params=_query)
        return decode(_response, ListActionRunResponse)

    def get(self, owner: str, repo: str, run_id: int) -> ActionRun:
        """
        Get an action run.

        Args:
            owner: owner of the repo
            repo: name of the repo
            run_id: id of the action run

        Returns:
            ActionRun.

        Raises:
            BadRequestError: 400. APIError is error format response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: ActionRun
        """
        _response = self._client._request("GET", f"/repos/{owner}/{repo}/actions/runs/{run_id}")
        return decode(_response, ActionRun)

    def delete(self, owner: str, repo: str, run_id: int) -> None:
        """
        Delete a completed workflow run.

        Remove a particular workflow run. The workflow run must have completed (succeeded, failed, cancelled) for the
        operation to succeed. Otherwise, an error is returned.

        Args:
            owner: owner of the repo
            repo: name of the repo
            run_id: id of the action run

        Returns:
            No content.

        Raises:
            BadRequestError: 400. APIError is error format response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: DeleteActionRun
        """
        _response = self._client._request("DELETE", f"/repos/{owner}/{repo}/actions/runs/{run_id}")
        return decode(_response, None)

    def artifacts(
        self,
        owner: str,
        repo: str,
        run_id: int,
        *,
        name: str | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> Paginated[ActionArtifact]:
        """
        List artifacts of a workflow run.

        Args:
            owner: owner of the repo
            repo: name of the repo
            run_id: ID of the workflow run
            name: filter by artifact name
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            ActionArtifactList.

        Raises:
            BadRequestError: 400. APIError is error format response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: ListActionRunArtifacts
        """
        _query: dict[str, object] = {"name": name}

        return self._client._paginate(
            "GET",
            f"/repos/{owner}/{repo}/actions/runs/{run_id}/artifacts",
            model=ActionArtifact,
            params=_query,
            page=page,
            limit=limit,
        )

    def cancel(self, owner: str, repo: str, run_id: int) -> None:
        """
        Cancel a pending or running workflow run.

        Cancel a particular workflow run. Pending or running jobs of the run are cancelled. A run that has already
        finished, whether cancelled, failed, skipped or succeeded, is left unchanged. In both cases the endpoint
        responds with HTTP 204.

        Args:
            owner: owner of the repo
            repo: name of the repo
            run_id: ID of the workflow run

        Returns:
            No content.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: CancelActionRun
        """
        _response = self._client._request("POST", f"/repos/{owner}/{repo}/actions/runs/{run_id}/cancel")
        return decode(_response, None)

    def jobs(self, owner: str, repo: str, run_id: int) -> builtins.list[ActionRunJob]:
        """
        List jobs of a workflow run.

        Args:
            owner: owner of the repo
            repo: name of the repo
            run_id: ID of the workflow run

        Returns:
            ActionRunJobList.

        Raises:
            BadRequestError: 400. APIError is error format response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: ListActionRunJobs
        """
        _response = self._client._request("GET", f"/repos/{owner}/{repo}/actions/runs/{run_id}/jobs")
        return decode(_response, list[ActionRunJob])

    def logs(self, owner: str, repo: str, run_id: int) -> bytes:
        """
        Download a ZIP of plaintext logs for every job in an action run.

        Args:
            owner: owner of the repo
            repo: name of the repo
            run_id: ID of the workflow run. The ZIP contains the latest attempt of each job in the run, with each entry
                named `{job-name}-{job-id}-attempt-{N}.log` (the job ID prevents collisions when two jobs share a name;
                the attempt number records which run the log came from). The run itself has no attempt number - jobs are
                re-run independently, so use the per-job logs endpoint with `?attempt` to fetch a specific historical
                attempt of one job.

        Returns:
            ZIP archive of per-job log files.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoGetActionRunLogs
        """
        _response = self._client._request("GET", f"/repos/{owner}/{repo}/actions/runs/{run_id}/logs")
        return decode(_response, bytes)


class AsyncReposActionsRuns:
    """The ``repos.actions.runs`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def list(
        self,
        owner: str,
        repo: str,
        *,
        page: int | None = None,
        limit: int | None = None,
        event: builtins.list[str] | None = None,
        status: builtins.list[
            Literal["unknown", "waiting", "running", "success", "failure", "cancelled", "skipped", "blocked"]
        ]
        | None = None,
        run_number: int | None = None,
        head_sha: str | None = None,
        ref: str | None = None,
        workflow_id: str | None = None,
    ) -> ListActionRunResponse:
        """
        List a repository's action runs.

        Args:
            owner: owner of the repo
            repo: name of the repo
            page: page number of results to return (1-based)
            limit: page size of results, default maximum page size is 50
            event: Returns workflow run triggered by the specified events. For example, `push`, `pull_request` or
                `workflow_dispatch`.
            status: Returns workflow runs with the check run status or conclusion that is specified. For example, a
                conclusion can be success or a status can be in_progress. Only Forgejo Actions can set a status of
                waiting, pending, or requested.
            run_number: Returns the workflow run associated with the run number.
            head_sha: Only returns workflow runs that are associated with the specified head_sha.
            ref: Only return workflow runs that involve the given Git reference, for example, `refs/heads/main`.
            workflow_id: Only return workflow runs that involve the given workflow ID.

        Returns:
            ActionRunList.

        Raises:
            BadRequestError: 400. APIError is error format response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.

        Operation ID: ListActionRuns
        """
        _query: dict[str, object] = {
            "page": page,
            "limit": limit,
            "event": event,
            "status": status,
            "run_number": run_number,
            "head_sha": head_sha,
            "ref": ref,
            "workflow_id": workflow_id,
        }

        _response = await self._client._request("GET", f"/repos/{owner}/{repo}/actions/runs", params=_query)
        return decode(_response, ListActionRunResponse)

    async def get(self, owner: str, repo: str, run_id: int) -> ActionRun:
        """
        Get an action run.

        Args:
            owner: owner of the repo
            repo: name of the repo
            run_id: id of the action run

        Returns:
            ActionRun.

        Raises:
            BadRequestError: 400. APIError is error format response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: ActionRun
        """
        _response = await self._client._request("GET", f"/repos/{owner}/{repo}/actions/runs/{run_id}")
        return decode(_response, ActionRun)

    async def delete(self, owner: str, repo: str, run_id: int) -> None:
        """
        Delete a completed workflow run.

        Remove a particular workflow run. The workflow run must have completed (succeeded, failed, cancelled) for the
        operation to succeed. Otherwise, an error is returned.

        Args:
            owner: owner of the repo
            repo: name of the repo
            run_id: id of the action run

        Returns:
            No content.

        Raises:
            BadRequestError: 400. APIError is error format response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: DeleteActionRun
        """
        _response = await self._client._request("DELETE", f"/repos/{owner}/{repo}/actions/runs/{run_id}")
        return decode(_response, None)

    async def artifacts(
        self,
        owner: str,
        repo: str,
        run_id: int,
        *,
        name: str | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> AsyncPaginated[ActionArtifact]:
        """
        List artifacts of a workflow run.

        Args:
            owner: owner of the repo
            repo: name of the repo
            run_id: ID of the workflow run
            name: filter by artifact name
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            ActionArtifactList.

        Raises:
            BadRequestError: 400. APIError is error format response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: ListActionRunArtifacts
        """
        _query: dict[str, object] = {"name": name}

        return await self._client._paginate(
            "GET",
            f"/repos/{owner}/{repo}/actions/runs/{run_id}/artifacts",
            model=ActionArtifact,
            params=_query,
            page=page,
            limit=limit,
        )

    async def cancel(self, owner: str, repo: str, run_id: int) -> None:
        """
        Cancel a pending or running workflow run.

        Cancel a particular workflow run. Pending or running jobs of the run are cancelled. A run that has already
        finished, whether cancelled, failed, skipped or succeeded, is left unchanged. In both cases the endpoint
        responds with HTTP 204.

        Args:
            owner: owner of the repo
            repo: name of the repo
            run_id: ID of the workflow run

        Returns:
            No content.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: CancelActionRun
        """
        _response = await self._client._request("POST", f"/repos/{owner}/{repo}/actions/runs/{run_id}/cancel")
        return decode(_response, None)

    async def jobs(self, owner: str, repo: str, run_id: int) -> builtins.list[ActionRunJob]:
        """
        List jobs of a workflow run.

        Args:
            owner: owner of the repo
            repo: name of the repo
            run_id: ID of the workflow run

        Returns:
            ActionRunJobList.

        Raises:
            BadRequestError: 400. APIError is error format response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: ListActionRunJobs
        """
        _response = await self._client._request("GET", f"/repos/{owner}/{repo}/actions/runs/{run_id}/jobs")
        return decode(_response, list[ActionRunJob])

    async def logs(self, owner: str, repo: str, run_id: int) -> bytes:
        """
        Download a ZIP of plaintext logs for every job in an action run.

        Args:
            owner: owner of the repo
            repo: name of the repo
            run_id: ID of the workflow run. The ZIP contains the latest attempt of each job in the run, with each entry
                named `{job-name}-{job-id}-attempt-{N}.log` (the job ID prevents collisions when two jobs share a name;
                the attempt number records which run the log came from). The run itself has no attempt number - jobs are
                re-run independently, so use the per-job logs endpoint with `?attempt` to fetch a specific historical
                attempt of one job.

        Returns:
            ZIP archive of per-job log files.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoGetActionRunLogs
        """
        _response = await self._client._request("GET", f"/repos/{owner}/{repo}/actions/runs/{run_id}/logs")
        return decode(_response, bytes)


class ReposActionsSecrets:
    """The ``repos.actions.secrets`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def list(self, owner: str, repo: str, *, page: int | None = None, limit: int | None = None) -> Paginated[Secret]:
        """
        List an repo's actions secrets.

        Args:
            owner: owner of the repository
            repo: name of the repository
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            SecretList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoListActionsSecrets
        """
        return self._client._paginate(
            "GET", f"/repos/{owner}/{repo}/actions/secrets", model=Secret, page=page, limit=limit
        )

    def update(self, owner: str, repo: str, secretname: str, *, data: str) -> None:
        """
        Create or Update a secret value in a repository.

        Args:
            owner: owner of the repository
            repo: name of the repository
            secretname: name of the secret
            data: Data of the secret. Special characters will be retained. Line endings will be normalized to LF to
                match the behaviour of browsers. Encode the data with Base64 if line endings should be retained.

        Returns:
            No content.

        Raises:
            BadRequestError: 400. APIError is error format response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: updateRepoSecret
        """
        _payload = CreateOrUpdateSecretOption(
            data=data,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = self._client._request("PUT", f"/repos/{owner}/{repo}/actions/secrets/{secretname}", json=_payload)
        return decode(_response, None)

    def delete(self, owner: str, repo: str, secretname: str) -> None:
        """
        Delete a secret in a repository.

        Args:
            owner: owner of the repository
            repo: name of the repository
            secretname: name of the secret

        Returns:
            No content.

        Raises:
            BadRequestError: 400. APIError is error format response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: deleteRepoSecret
        """
        _response = self._client._request("DELETE", f"/repos/{owner}/{repo}/actions/secrets/{secretname}")
        return decode(_response, None)


class AsyncReposActionsSecrets:
    """The ``repos.actions.secrets`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def list(
        self,
        owner: str,
        repo: str,
        *,
        page: int | None = None,
        limit: int | None = None,
    ) -> AsyncPaginated[Secret]:
        """
        List an repo's actions secrets.

        Args:
            owner: owner of the repository
            repo: name of the repository
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            SecretList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoListActionsSecrets
        """
        return await self._client._paginate(
            "GET", f"/repos/{owner}/{repo}/actions/secrets", model=Secret, page=page, limit=limit
        )

    async def update(self, owner: str, repo: str, secretname: str, *, data: str) -> None:
        """
        Create or Update a secret value in a repository.

        Args:
            owner: owner of the repository
            repo: name of the repository
            secretname: name of the secret
            data: Data of the secret. Special characters will be retained. Line endings will be normalized to LF to
                match the behaviour of browsers. Encode the data with Base64 if line endings should be retained.

        Returns:
            No content.

        Raises:
            BadRequestError: 400. APIError is error format response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: updateRepoSecret
        """
        _payload = CreateOrUpdateSecretOption(
            data=data,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = await self._client._request(
            "PUT", f"/repos/{owner}/{repo}/actions/secrets/{secretname}", json=_payload
        )
        return decode(_response, None)

    async def delete(self, owner: str, repo: str, secretname: str) -> None:
        """
        Delete a secret in a repository.

        Args:
            owner: owner of the repository
            repo: name of the repository
            secretname: name of the secret

        Returns:
            No content.

        Raises:
            BadRequestError: 400. APIError is error format response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: deleteRepoSecret
        """
        _response = await self._client._request("DELETE", f"/repos/{owner}/{repo}/actions/secrets/{secretname}")
        return decode(_response, None)


class ReposActionsVariables:
    """The ``repos.actions.variables`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def list(
        self,
        owner: str,
        repo: str,
        *,
        page: int | None = None,
        limit: int | None = None,
    ) -> Paginated[ActionVariable]:
        """
        Get repo-level variables list.

        Args:
            owner: name of the owner
            repo: name of the repository
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            VariableList.

        Raises:
            BadRequestError: 400. APIError is error format response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: getRepoVariablesList
        """
        return self._client._paginate(
            "GET", f"/repos/{owner}/{repo}/actions/variables", model=ActionVariable, page=page, limit=limit
        )

    def get(self, owner: str, repo: str, variablename: str) -> ActionVariable:
        """
        Get a repo-level variable.

        Args:
            owner: name of the owner
            repo: name of the repository
            variablename: name of the variable

        Returns:
            ActionVariable.

        Raises:
            BadRequestError: 400. APIError is error format response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: getRepoVariable
        """
        _response = self._client._request("GET", f"/repos/{owner}/{repo}/actions/variables/{variablename}")
        return decode(_response, ActionVariable)

    def create(self, owner: str, repo: str, variablename: str, *, value: str) -> None:
        """
        Create a repo-level variable.

        Args:
            owner: name of the owner
            repo: name of the repository
            variablename: name of the variable
            value: Value of the variable to create. Special characters will be retained. Line endings will be normalized
                to LF to match the behaviour of browsers. Encode the data with Base64 if line endings should be
                retained.

        Returns:
            No content.

        Raises:
            BadRequestError: 400. APIError is error format response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: createRepoVariable
        """
        _payload = CreateVariableOption(
            value=value,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = self._client._request(
            "POST", f"/repos/{owner}/{repo}/actions/variables/{variablename}", json=_payload
        )
        return decode(_response, None)

    def update(self, owner: str, repo: str, variablename: str, *, name: str | None = None, value: str) -> None:
        """
        Update a repo-level variable.

        Args:
            owner: name of the owner
            repo: name of the repository
            variablename: name of the variable
            name: New name for the variable. If the field is empty, the variable name won't be updated. Forgejo will
                convert it to uppercase.
            value: Value of the variable to update. Special characters will be retained. Line endings will be normalized
                to LF to match the behaviour of browsers. Encode the data with Base64 if line endings should be
                retained.

        Returns:
            No content.

        Raises:
            BadRequestError: 400. APIError is error format response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: updateRepoVariable
        """
        _payload = UpdateVariableOption(
            name=name,
            value=value,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = self._client._request(
            "PUT", f"/repos/{owner}/{repo}/actions/variables/{variablename}", json=_payload
        )
        return decode(_response, None)

    def delete(self, owner: str, repo: str, variablename: str) -> None:
        """
        Delete a repo-level variable.

        Args:
            owner: name of the owner
            repo: name of the repository
            variablename: name of the variable

        Returns:
            No content.

        Raises:
            BadRequestError: 400. APIError is error format response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: deleteRepoVariable
        """
        _response = self._client._request("DELETE", f"/repos/{owner}/{repo}/actions/variables/{variablename}")
        return decode(_response, None)


class AsyncReposActionsVariables:
    """The ``repos.actions.variables`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def list(
        self,
        owner: str,
        repo: str,
        *,
        page: int | None = None,
        limit: int | None = None,
    ) -> AsyncPaginated[ActionVariable]:
        """
        Get repo-level variables list.

        Args:
            owner: name of the owner
            repo: name of the repository
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            VariableList.

        Raises:
            BadRequestError: 400. APIError is error format response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: getRepoVariablesList
        """
        return await self._client._paginate(
            "GET", f"/repos/{owner}/{repo}/actions/variables", model=ActionVariable, page=page, limit=limit
        )

    async def get(self, owner: str, repo: str, variablename: str) -> ActionVariable:
        """
        Get a repo-level variable.

        Args:
            owner: name of the owner
            repo: name of the repository
            variablename: name of the variable

        Returns:
            ActionVariable.

        Raises:
            BadRequestError: 400. APIError is error format response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: getRepoVariable
        """
        _response = await self._client._request("GET", f"/repos/{owner}/{repo}/actions/variables/{variablename}")
        return decode(_response, ActionVariable)

    async def create(self, owner: str, repo: str, variablename: str, *, value: str) -> None:
        """
        Create a repo-level variable.

        Args:
            owner: name of the owner
            repo: name of the repository
            variablename: name of the variable
            value: Value of the variable to create. Special characters will be retained. Line endings will be normalized
                to LF to match the behaviour of browsers. Encode the data with Base64 if line endings should be
                retained.

        Returns:
            No content.

        Raises:
            BadRequestError: 400. APIError is error format response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: createRepoVariable
        """
        _payload = CreateVariableOption(
            value=value,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = await self._client._request(
            "POST", f"/repos/{owner}/{repo}/actions/variables/{variablename}", json=_payload
        )
        return decode(_response, None)

    async def update(self, owner: str, repo: str, variablename: str, *, name: str | None = None, value: str) -> None:
        """
        Update a repo-level variable.

        Args:
            owner: name of the owner
            repo: name of the repository
            variablename: name of the variable
            name: New name for the variable. If the field is empty, the variable name won't be updated. Forgejo will
                convert it to uppercase.
            value: Value of the variable to update. Special characters will be retained. Line endings will be normalized
                to LF to match the behaviour of browsers. Encode the data with Base64 if line endings should be
                retained.

        Returns:
            No content.

        Raises:
            BadRequestError: 400. APIError is error format response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: updateRepoVariable
        """
        _payload = UpdateVariableOption(
            name=name,
            value=value,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = await self._client._request(
            "PUT", f"/repos/{owner}/{repo}/actions/variables/{variablename}", json=_payload
        )
        return decode(_response, None)

    async def delete(self, owner: str, repo: str, variablename: str) -> None:
        """
        Delete a repo-level variable.

        Args:
            owner: name of the owner
            repo: name of the repository
            variablename: name of the variable

        Returns:
            No content.

        Raises:
            BadRequestError: 400. APIError is error format response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: deleteRepoVariable
        """
        _response = await self._client._request("DELETE", f"/repos/{owner}/{repo}/actions/variables/{variablename}")
        return decode(_response, None)


class ReposActionsWorkflows:
    """The ``repos.actions.workflows`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def dispatch(
        self,
        owner: str,
        repo: str,
        workflowfilename: str,
        *,
        inputs: dict[str, str] | None = None,
        ref: str,
        return_run_info: bool | None = None,
    ) -> DispatchWorkflowRun | None:
        """
        Dispatches a workflow.

        Args:
            owner: owner of the repo
            repo: name of the repo
            workflowfilename: name of the workflow
            inputs: Input keys and values configured in the workflow file.
            ref: Git reference for the workflow
            return_run_info: Flag to return the run info

        Returns:
            DispatchWorkflowRun is a Workflow Run after dispatching.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: DispatchWorkflow
        """
        _payload = DispatchWorkflowOption(
            inputs=inputs,
            ref=ref,
            return_run_info=return_run_info,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = self._client._request(
            "POST", f"/repos/{owner}/{repo}/actions/workflows/{workflowfilename}/dispatches", json=_payload
        )
        return decode(_response, DispatchWorkflowRun)


class AsyncReposActionsWorkflows:
    """The ``repos.actions.workflows`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def dispatch(
        self,
        owner: str,
        repo: str,
        workflowfilename: str,
        *,
        inputs: dict[str, str] | None = None,
        ref: str,
        return_run_info: bool | None = None,
    ) -> DispatchWorkflowRun | None:
        """
        Dispatches a workflow.

        Args:
            owner: owner of the repo
            repo: name of the repo
            workflowfilename: name of the workflow
            inputs: Input keys and values configured in the workflow file.
            ref: Git reference for the workflow
            return_run_info: Flag to return the run info

        Returns:
            DispatchWorkflowRun is a Workflow Run after dispatching.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: DispatchWorkflow
        """
        _payload = DispatchWorkflowOption(
            inputs=inputs,
            ref=ref,
            return_run_info=return_run_info,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = await self._client._request(
            "POST", f"/repos/{owner}/{repo}/actions/workflows/{workflowfilename}/dispatches", json=_payload
        )
        return decode(_response, DispatchWorkflowRun)


class ReposActivities:
    """The ``repos.activities`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def feeds(
        self,
        owner: str,
        repo: str,
        *,
        date: date | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> Paginated[Activity]:
        """
        List a repository's activity feeds.

        Args:
            owner: owner of the repo
            repo: name of the repo
            date: the date of the activities to be found
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            ActivityFeedsList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoListActivityFeeds
        """
        _query: dict[str, object] = {"date": None if date is None else date.isoformat()}

        return self._client._paginate(
            "GET", f"/repos/{owner}/{repo}/activities/feeds", model=Activity, params=_query, page=page, limit=limit
        )


class AsyncReposActivities:
    """The ``repos.activities`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def feeds(
        self,
        owner: str,
        repo: str,
        *,
        date: date | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> AsyncPaginated[Activity]:
        """
        List a repository's activity feeds.

        Args:
            owner: owner of the repo
            repo: name of the repo
            date: the date of the activities to be found
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            ActivityFeedsList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoListActivityFeeds
        """
        _query: dict[str, object] = {"date": None if date is None else date.isoformat()}

        return await self._client._paginate(
            "GET", f"/repos/{owner}/{repo}/activities/feeds", model=Activity, params=_query, page=page, limit=limit
        )


class ReposArchive:
    """The ``repos.archive`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def get(self, owner: str, repo: str, archive: str) -> bytes:
        """
        Get an archive of a repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            archive: the git reference for download with attached archive format (e.g. master.zip)

        Returns:
            success.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoGetArchive
        """
        _response = self._client._request("GET", f"/repos/{owner}/{repo}/archive/{archive}")
        return decode(_response, bytes)


class AsyncReposArchive:
    """The ``repos.archive`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def get(self, owner: str, repo: str, archive: str) -> bytes:
        """
        Get an archive of a repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            archive: the git reference for download with attached archive format (e.g. master.zip)

        Returns:
            success.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoGetArchive
        """
        _response = await self._client._request("GET", f"/repos/{owner}/{repo}/archive/{archive}")
        return decode(_response, bytes)


class ReposAvatar:
    """The ``repos.avatar`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def update(self, owner: str, repo: str, *, image: str | None = None) -> None:
        """
        Update a repository's avatar.

        Args:
            owner: owner of the repo
            repo: name of the repo
            image: image must be base64 encoded

        Returns:
            No content.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoUpdateAvatar
        """
        if image is not None:
            _payload = UpdateRepoAvatarOption(image=image).model_dump(mode="json", by_alias=True, exclude_none=True)
        else:
            _payload = None

        _response = self._client._request("POST", f"/repos/{owner}/{repo}/avatar", json=_payload)
        return decode(_response, None)

    def delete(self, owner: str, repo: str) -> None:
        """
        Delete a repository's avatar.

        Args:
            owner: owner of the repo
            repo: name of the repo

        Returns:
            No content.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoDeleteAvatar
        """
        _response = self._client._request("DELETE", f"/repos/{owner}/{repo}/avatar")
        return decode(_response, None)


class AsyncReposAvatar:
    """The ``repos.avatar`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def update(self, owner: str, repo: str, *, image: str | None = None) -> None:
        """
        Update a repository's avatar.

        Args:
            owner: owner of the repo
            repo: name of the repo
            image: image must be base64 encoded

        Returns:
            No content.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoUpdateAvatar
        """
        if image is not None:
            _payload = UpdateRepoAvatarOption(image=image).model_dump(mode="json", by_alias=True, exclude_none=True)
        else:
            _payload = None

        _response = await self._client._request("POST", f"/repos/{owner}/{repo}/avatar", json=_payload)
        return decode(_response, None)

    async def delete(self, owner: str, repo: str) -> None:
        """
        Delete a repository's avatar.

        Args:
            owner: owner of the repo
            repo: name of the repo

        Returns:
            No content.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoDeleteAvatar
        """
        _response = await self._client._request("DELETE", f"/repos/{owner}/{repo}/avatar")
        return decode(_response, None)


class ReposBranchProtections:
    """The ``repos.branch_protections`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def list(self, owner: str, repo: str) -> builtins.list[BranchProtection]:
        """
        List branch protections for a repository.

        Args:
            owner: owner of the repo
            repo: name of the repo

        Returns:
            BranchProtectionList.

        Operation ID: repoListBranchProtection
        """
        _response = self._client._request("GET", f"/repos/{owner}/{repo}/branch_protections")
        return decode(_response, list[BranchProtection])

    def create(
        self,
        owner: str,
        repo: str,
        *,
        apply_to_admins: bool | None = None,
        approvals_whitelist_teams: builtins.list[str] | None = None,
        approvals_whitelist_username: builtins.list[str] | None = None,
        block_on_official_review_requests: bool | None = None,
        block_on_outdated_branch: bool | None = None,
        block_on_rejected_reviews: bool | None = None,
        branch_name: str | None = None,
        dismiss_stale_approvals: bool | None = None,
        enable_approvals_whitelist: bool | None = None,
        enable_merge_whitelist: bool | None = None,
        enable_push: bool | None = None,
        enable_push_whitelist: bool | None = None,
        enable_status_check: bool | None = None,
        ignore_stale_approvals: bool | None = None,
        merge_whitelist_teams: builtins.list[str] | None = None,
        merge_whitelist_usernames: builtins.list[str] | None = None,
        protected_file_patterns: str | None = None,
        push_whitelist_deploy_keys: bool | None = None,
        push_whitelist_teams: builtins.list[str] | None = None,
        push_whitelist_usernames: builtins.list[str] | None = None,
        require_signed_commits: bool | None = None,
        required_approvals: int | None = None,
        rule_name: str | None = None,
        status_check_contexts: builtins.list[str] | None = None,
        unprotected_file_patterns: str | None = None,
    ) -> BranchProtection:
        """
        Create a branch protections for a repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            apply_to_admins:
            approvals_whitelist_teams:
            approvals_whitelist_username:
            block_on_official_review_requests:
            block_on_outdated_branch:
            block_on_rejected_reviews:
            branch_name: Deprecated: true
            dismiss_stale_approvals:
            enable_approvals_whitelist:
            enable_merge_whitelist:
            enable_push:
            enable_push_whitelist:
            enable_status_check:
            ignore_stale_approvals:
            merge_whitelist_teams:
            merge_whitelist_usernames:
            protected_file_patterns:
            push_whitelist_deploy_keys:
            push_whitelist_teams:
            push_whitelist_usernames:
            require_signed_commits:
            required_approvals:
            rule_name:
            status_check_contexts:
            unprotected_file_patterns:

        Returns:
            BranchProtection.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.
            LockedError: 423. APIRepoArchivedError is an error that is raised when an archived repo should be modified.

        Operation ID: repoCreateBranchProtection
        """
        if (
            apply_to_admins is not None
            or approvals_whitelist_teams is not None
            or approvals_whitelist_username is not None
            or block_on_official_review_requests is not None
            or block_on_outdated_branch is not None
            or block_on_rejected_reviews is not None
            or branch_name is not None
            or dismiss_stale_approvals is not None
            or enable_approvals_whitelist is not None
            or enable_merge_whitelist is not None
            or enable_push is not None
            or enable_push_whitelist is not None
            or enable_status_check is not None
            or ignore_stale_approvals is not None
            or merge_whitelist_teams is not None
            or merge_whitelist_usernames is not None
            or protected_file_patterns is not None
            or push_whitelist_deploy_keys is not None
            or push_whitelist_teams is not None
            or push_whitelist_usernames is not None
            or require_signed_commits is not None
            or required_approvals is not None
            or rule_name is not None
            or status_check_contexts is not None
            or unprotected_file_patterns is not None
        ):
            _payload = CreateBranchProtectionOption(
                apply_to_admins=apply_to_admins,
                approvals_whitelist_teams=approvals_whitelist_teams,
                approvals_whitelist_username=approvals_whitelist_username,
                block_on_official_review_requests=block_on_official_review_requests,
                block_on_outdated_branch=block_on_outdated_branch,
                block_on_rejected_reviews=block_on_rejected_reviews,
                branch_name=branch_name,
                dismiss_stale_approvals=dismiss_stale_approvals,
                enable_approvals_whitelist=enable_approvals_whitelist,
                enable_merge_whitelist=enable_merge_whitelist,
                enable_push=enable_push,
                enable_push_whitelist=enable_push_whitelist,
                enable_status_check=enable_status_check,
                ignore_stale_approvals=ignore_stale_approvals,
                merge_whitelist_teams=merge_whitelist_teams,
                merge_whitelist_usernames=merge_whitelist_usernames,
                protected_file_patterns=protected_file_patterns,
                push_whitelist_deploy_keys=push_whitelist_deploy_keys,
                push_whitelist_teams=push_whitelist_teams,
                push_whitelist_usernames=push_whitelist_usernames,
                require_signed_commits=require_signed_commits,
                required_approvals=required_approvals,
                rule_name=rule_name,
                status_check_contexts=status_check_contexts,
                unprotected_file_patterns=unprotected_file_patterns,
            ).model_dump(mode="json", by_alias=True, exclude_none=True)
        else:
            _payload = None

        _response = self._client._request("POST", f"/repos/{owner}/{repo}/branch_protections", json=_payload)
        return decode(_response, BranchProtection)

    def get(self, owner: str, repo: str, name: str) -> BranchProtection:
        """
        Get a specific branch protection for the repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            name: name of protected branch

        Returns:
            BranchProtection.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoGetBranchProtection
        """
        _response = self._client._request("GET", f"/repos/{owner}/{repo}/branch_protections/{name}")
        return decode(_response, BranchProtection)

    def update(
        self,
        owner: str,
        repo: str,
        name: str,
        *,
        apply_to_admins: bool | None = None,
        approvals_whitelist_teams: builtins.list[str] | None = None,
        approvals_whitelist_username: builtins.list[str] | None = None,
        block_on_official_review_requests: bool | None = None,
        block_on_outdated_branch: bool | None = None,
        block_on_rejected_reviews: bool | None = None,
        dismiss_stale_approvals: bool | None = None,
        enable_approvals_whitelist: bool | None = None,
        enable_merge_whitelist: bool | None = None,
        enable_push: bool | None = None,
        enable_push_whitelist: bool | None = None,
        enable_status_check: bool | None = None,
        ignore_stale_approvals: bool | None = None,
        merge_whitelist_teams: builtins.list[str] | None = None,
        merge_whitelist_usernames: builtins.list[str] | None = None,
        protected_file_patterns: str | None = None,
        push_whitelist_deploy_keys: bool | None = None,
        push_whitelist_teams: builtins.list[str] | None = None,
        push_whitelist_usernames: builtins.list[str] | None = None,
        require_signed_commits: bool | None = None,
        required_approvals: int | None = None,
        status_check_contexts: builtins.list[str] | None = None,
        unprotected_file_patterns: str | None = None,
    ) -> BranchProtection:
        """
        Edit a branch protections for a repository. Only fields that are set will be changed.

        Args:
            owner: owner of the repo
            repo: name of the repo
            name: name of protected branch
            apply_to_admins:
            approvals_whitelist_teams:
            approvals_whitelist_username:
            block_on_official_review_requests:
            block_on_outdated_branch:
            block_on_rejected_reviews:
            dismiss_stale_approvals:
            enable_approvals_whitelist:
            enable_merge_whitelist:
            enable_push:
            enable_push_whitelist:
            enable_status_check:
            ignore_stale_approvals:
            merge_whitelist_teams:
            merge_whitelist_usernames:
            protected_file_patterns:
            push_whitelist_deploy_keys:
            push_whitelist_teams:
            push_whitelist_usernames:
            require_signed_commits:
            required_approvals:
            status_check_contexts:
            unprotected_file_patterns:

        Returns:
            BranchProtection.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.
            LockedError: 423. APIRepoArchivedError is an error that is raised when an archived repo should be modified.

        Operation ID: repoEditBranchProtection
        """
        if (
            apply_to_admins is not None
            or approvals_whitelist_teams is not None
            or approvals_whitelist_username is not None
            or block_on_official_review_requests is not None
            or block_on_outdated_branch is not None
            or block_on_rejected_reviews is not None
            or dismiss_stale_approvals is not None
            or enable_approvals_whitelist is not None
            or enable_merge_whitelist is not None
            or enable_push is not None
            or enable_push_whitelist is not None
            or enable_status_check is not None
            or ignore_stale_approvals is not None
            or merge_whitelist_teams is not None
            or merge_whitelist_usernames is not None
            or protected_file_patterns is not None
            or push_whitelist_deploy_keys is not None
            or push_whitelist_teams is not None
            or push_whitelist_usernames is not None
            or require_signed_commits is not None
            or required_approvals is not None
            or status_check_contexts is not None
            or unprotected_file_patterns is not None
        ):
            _payload = EditBranchProtectionOption(
                apply_to_admins=apply_to_admins,
                approvals_whitelist_teams=approvals_whitelist_teams,
                approvals_whitelist_username=approvals_whitelist_username,
                block_on_official_review_requests=block_on_official_review_requests,
                block_on_outdated_branch=block_on_outdated_branch,
                block_on_rejected_reviews=block_on_rejected_reviews,
                dismiss_stale_approvals=dismiss_stale_approvals,
                enable_approvals_whitelist=enable_approvals_whitelist,
                enable_merge_whitelist=enable_merge_whitelist,
                enable_push=enable_push,
                enable_push_whitelist=enable_push_whitelist,
                enable_status_check=enable_status_check,
                ignore_stale_approvals=ignore_stale_approvals,
                merge_whitelist_teams=merge_whitelist_teams,
                merge_whitelist_usernames=merge_whitelist_usernames,
                protected_file_patterns=protected_file_patterns,
                push_whitelist_deploy_keys=push_whitelist_deploy_keys,
                push_whitelist_teams=push_whitelist_teams,
                push_whitelist_usernames=push_whitelist_usernames,
                require_signed_commits=require_signed_commits,
                required_approvals=required_approvals,
                status_check_contexts=status_check_contexts,
                unprotected_file_patterns=unprotected_file_patterns,
            ).model_dump(mode="json", by_alias=True, exclude_none=True)
        else:
            _payload = None

        _response = self._client._request("PATCH", f"/repos/{owner}/{repo}/branch_protections/{name}", json=_payload)
        return decode(_response, BranchProtection)

    def delete(self, owner: str, repo: str, name: str) -> None:
        """
        Delete a specific branch protection for the repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            name: name of protected branch

        Returns:
            No content.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoDeleteBranchProtection
        """
        _response = self._client._request("DELETE", f"/repos/{owner}/{repo}/branch_protections/{name}")
        return decode(_response, None)


class AsyncReposBranchProtections:
    """The ``repos.branch_protections`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def list(self, owner: str, repo: str) -> builtins.list[BranchProtection]:
        """
        List branch protections for a repository.

        Args:
            owner: owner of the repo
            repo: name of the repo

        Returns:
            BranchProtectionList.

        Operation ID: repoListBranchProtection
        """
        _response = await self._client._request("GET", f"/repos/{owner}/{repo}/branch_protections")
        return decode(_response, list[BranchProtection])

    async def create(
        self,
        owner: str,
        repo: str,
        *,
        apply_to_admins: bool | None = None,
        approvals_whitelist_teams: builtins.list[str] | None = None,
        approvals_whitelist_username: builtins.list[str] | None = None,
        block_on_official_review_requests: bool | None = None,
        block_on_outdated_branch: bool | None = None,
        block_on_rejected_reviews: bool | None = None,
        branch_name: str | None = None,
        dismiss_stale_approvals: bool | None = None,
        enable_approvals_whitelist: bool | None = None,
        enable_merge_whitelist: bool | None = None,
        enable_push: bool | None = None,
        enable_push_whitelist: bool | None = None,
        enable_status_check: bool | None = None,
        ignore_stale_approvals: bool | None = None,
        merge_whitelist_teams: builtins.list[str] | None = None,
        merge_whitelist_usernames: builtins.list[str] | None = None,
        protected_file_patterns: str | None = None,
        push_whitelist_deploy_keys: bool | None = None,
        push_whitelist_teams: builtins.list[str] | None = None,
        push_whitelist_usernames: builtins.list[str] | None = None,
        require_signed_commits: bool | None = None,
        required_approvals: int | None = None,
        rule_name: str | None = None,
        status_check_contexts: builtins.list[str] | None = None,
        unprotected_file_patterns: str | None = None,
    ) -> BranchProtection:
        """
        Create a branch protections for a repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            apply_to_admins:
            approvals_whitelist_teams:
            approvals_whitelist_username:
            block_on_official_review_requests:
            block_on_outdated_branch:
            block_on_rejected_reviews:
            branch_name: Deprecated: true
            dismiss_stale_approvals:
            enable_approvals_whitelist:
            enable_merge_whitelist:
            enable_push:
            enable_push_whitelist:
            enable_status_check:
            ignore_stale_approvals:
            merge_whitelist_teams:
            merge_whitelist_usernames:
            protected_file_patterns:
            push_whitelist_deploy_keys:
            push_whitelist_teams:
            push_whitelist_usernames:
            require_signed_commits:
            required_approvals:
            rule_name:
            status_check_contexts:
            unprotected_file_patterns:

        Returns:
            BranchProtection.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.
            LockedError: 423. APIRepoArchivedError is an error that is raised when an archived repo should be modified.

        Operation ID: repoCreateBranchProtection
        """
        if (
            apply_to_admins is not None
            or approvals_whitelist_teams is not None
            or approvals_whitelist_username is not None
            or block_on_official_review_requests is not None
            or block_on_outdated_branch is not None
            or block_on_rejected_reviews is not None
            or branch_name is not None
            or dismiss_stale_approvals is not None
            or enable_approvals_whitelist is not None
            or enable_merge_whitelist is not None
            or enable_push is not None
            or enable_push_whitelist is not None
            or enable_status_check is not None
            or ignore_stale_approvals is not None
            or merge_whitelist_teams is not None
            or merge_whitelist_usernames is not None
            or protected_file_patterns is not None
            or push_whitelist_deploy_keys is not None
            or push_whitelist_teams is not None
            or push_whitelist_usernames is not None
            or require_signed_commits is not None
            or required_approvals is not None
            or rule_name is not None
            or status_check_contexts is not None
            or unprotected_file_patterns is not None
        ):
            _payload = CreateBranchProtectionOption(
                apply_to_admins=apply_to_admins,
                approvals_whitelist_teams=approvals_whitelist_teams,
                approvals_whitelist_username=approvals_whitelist_username,
                block_on_official_review_requests=block_on_official_review_requests,
                block_on_outdated_branch=block_on_outdated_branch,
                block_on_rejected_reviews=block_on_rejected_reviews,
                branch_name=branch_name,
                dismiss_stale_approvals=dismiss_stale_approvals,
                enable_approvals_whitelist=enable_approvals_whitelist,
                enable_merge_whitelist=enable_merge_whitelist,
                enable_push=enable_push,
                enable_push_whitelist=enable_push_whitelist,
                enable_status_check=enable_status_check,
                ignore_stale_approvals=ignore_stale_approvals,
                merge_whitelist_teams=merge_whitelist_teams,
                merge_whitelist_usernames=merge_whitelist_usernames,
                protected_file_patterns=protected_file_patterns,
                push_whitelist_deploy_keys=push_whitelist_deploy_keys,
                push_whitelist_teams=push_whitelist_teams,
                push_whitelist_usernames=push_whitelist_usernames,
                require_signed_commits=require_signed_commits,
                required_approvals=required_approvals,
                rule_name=rule_name,
                status_check_contexts=status_check_contexts,
                unprotected_file_patterns=unprotected_file_patterns,
            ).model_dump(mode="json", by_alias=True, exclude_none=True)
        else:
            _payload = None

        _response = await self._client._request("POST", f"/repos/{owner}/{repo}/branch_protections", json=_payload)
        return decode(_response, BranchProtection)

    async def get(self, owner: str, repo: str, name: str) -> BranchProtection:
        """
        Get a specific branch protection for the repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            name: name of protected branch

        Returns:
            BranchProtection.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoGetBranchProtection
        """
        _response = await self._client._request("GET", f"/repos/{owner}/{repo}/branch_protections/{name}")
        return decode(_response, BranchProtection)

    async def update(
        self,
        owner: str,
        repo: str,
        name: str,
        *,
        apply_to_admins: bool | None = None,
        approvals_whitelist_teams: builtins.list[str] | None = None,
        approvals_whitelist_username: builtins.list[str] | None = None,
        block_on_official_review_requests: bool | None = None,
        block_on_outdated_branch: bool | None = None,
        block_on_rejected_reviews: bool | None = None,
        dismiss_stale_approvals: bool | None = None,
        enable_approvals_whitelist: bool | None = None,
        enable_merge_whitelist: bool | None = None,
        enable_push: bool | None = None,
        enable_push_whitelist: bool | None = None,
        enable_status_check: bool | None = None,
        ignore_stale_approvals: bool | None = None,
        merge_whitelist_teams: builtins.list[str] | None = None,
        merge_whitelist_usernames: builtins.list[str] | None = None,
        protected_file_patterns: str | None = None,
        push_whitelist_deploy_keys: bool | None = None,
        push_whitelist_teams: builtins.list[str] | None = None,
        push_whitelist_usernames: builtins.list[str] | None = None,
        require_signed_commits: bool | None = None,
        required_approvals: int | None = None,
        status_check_contexts: builtins.list[str] | None = None,
        unprotected_file_patterns: str | None = None,
    ) -> BranchProtection:
        """
        Edit a branch protections for a repository. Only fields that are set will be changed.

        Args:
            owner: owner of the repo
            repo: name of the repo
            name: name of protected branch
            apply_to_admins:
            approvals_whitelist_teams:
            approvals_whitelist_username:
            block_on_official_review_requests:
            block_on_outdated_branch:
            block_on_rejected_reviews:
            dismiss_stale_approvals:
            enable_approvals_whitelist:
            enable_merge_whitelist:
            enable_push:
            enable_push_whitelist:
            enable_status_check:
            ignore_stale_approvals:
            merge_whitelist_teams:
            merge_whitelist_usernames:
            protected_file_patterns:
            push_whitelist_deploy_keys:
            push_whitelist_teams:
            push_whitelist_usernames:
            require_signed_commits:
            required_approvals:
            status_check_contexts:
            unprotected_file_patterns:

        Returns:
            BranchProtection.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.
            LockedError: 423. APIRepoArchivedError is an error that is raised when an archived repo should be modified.

        Operation ID: repoEditBranchProtection
        """
        if (
            apply_to_admins is not None
            or approvals_whitelist_teams is not None
            or approvals_whitelist_username is not None
            or block_on_official_review_requests is not None
            or block_on_outdated_branch is not None
            or block_on_rejected_reviews is not None
            or dismiss_stale_approvals is not None
            or enable_approvals_whitelist is not None
            or enable_merge_whitelist is not None
            or enable_push is not None
            or enable_push_whitelist is not None
            or enable_status_check is not None
            or ignore_stale_approvals is not None
            or merge_whitelist_teams is not None
            or merge_whitelist_usernames is not None
            or protected_file_patterns is not None
            or push_whitelist_deploy_keys is not None
            or push_whitelist_teams is not None
            or push_whitelist_usernames is not None
            or require_signed_commits is not None
            or required_approvals is not None
            or status_check_contexts is not None
            or unprotected_file_patterns is not None
        ):
            _payload = EditBranchProtectionOption(
                apply_to_admins=apply_to_admins,
                approvals_whitelist_teams=approvals_whitelist_teams,
                approvals_whitelist_username=approvals_whitelist_username,
                block_on_official_review_requests=block_on_official_review_requests,
                block_on_outdated_branch=block_on_outdated_branch,
                block_on_rejected_reviews=block_on_rejected_reviews,
                dismiss_stale_approvals=dismiss_stale_approvals,
                enable_approvals_whitelist=enable_approvals_whitelist,
                enable_merge_whitelist=enable_merge_whitelist,
                enable_push=enable_push,
                enable_push_whitelist=enable_push_whitelist,
                enable_status_check=enable_status_check,
                ignore_stale_approvals=ignore_stale_approvals,
                merge_whitelist_teams=merge_whitelist_teams,
                merge_whitelist_usernames=merge_whitelist_usernames,
                protected_file_patterns=protected_file_patterns,
                push_whitelist_deploy_keys=push_whitelist_deploy_keys,
                push_whitelist_teams=push_whitelist_teams,
                push_whitelist_usernames=push_whitelist_usernames,
                require_signed_commits=require_signed_commits,
                required_approvals=required_approvals,
                status_check_contexts=status_check_contexts,
                unprotected_file_patterns=unprotected_file_patterns,
            ).model_dump(mode="json", by_alias=True, exclude_none=True)
        else:
            _payload = None

        _response = await self._client._request(
            "PATCH", f"/repos/{owner}/{repo}/branch_protections/{name}", json=_payload
        )
        return decode(_response, BranchProtection)

    async def delete(self, owner: str, repo: str, name: str) -> None:
        """
        Delete a specific branch protection for the repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            name: name of protected branch

        Returns:
            No content.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoDeleteBranchProtection
        """
        _response = await self._client._request("DELETE", f"/repos/{owner}/{repo}/branch_protections/{name}")
        return decode(_response, None)


class ReposBranches:
    """The ``repos.branches`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def list(self, owner: str, repo: str, *, page: int | None = None, limit: int | None = None) -> Paginated[Branch]:
        """
        List a repository's branches.

        Args:
            owner: owner of the repo
            repo: name of the repo
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            BranchList.

        Operation ID: repoListBranches
        """
        return self._client._paginate("GET", f"/repos/{owner}/{repo}/branches", model=Branch, page=page, limit=limit)

    def create(
        self,
        owner: str,
        repo: str,
        *,
        new_branch_name: str,
        old_branch_name: str | None = None,
        old_ref_name: str | None = None,
    ) -> Branch:
        """
        Create a branch.

        Args:
            owner: owner of the repo
            repo: name of the repo
            new_branch_name: Name of the branch to create
            old_branch_name: Deprecated: true Name of the old branch to create from
            old_ref_name: Name of the old branch/tag/commit to create from

        Returns:
            Branch.

        Raises:
            ForbiddenError: 403. The branch is archived or a mirror.
            NotFoundError: 404. The old branch does not exist.
            ConflictError: 409. The branch with the same name already exists.
            PayloadTooLargeError: 413. QuotaExceeded.
            LockedError: 423. APIRepoArchivedError is an error that is raised when an archived repo should be modified.

        Operation ID: repoCreateBranch
        """
        _payload = CreateBranchRepoOption(
            new_branch_name=new_branch_name,
            old_branch_name=old_branch_name,
            old_ref_name=old_ref_name,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = self._client._request("POST", f"/repos/{owner}/{repo}/branches", json=_payload)
        return decode(_response, Branch)

    def get(self, owner: str, repo: str, branch: str) -> Branch:
        """
        Retrieve a specific branch from a repository, including its effective branch protection.

        Args:
            owner: owner of the repo
            repo: name of the repo
            branch: branch to get

        Returns:
            Branch.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoGetBranch
        """
        _response = self._client._request("GET", f"/repos/{owner}/{repo}/branches/{branch}")
        return decode(_response, Branch)

    def update(self, owner: str, repo: str, branch: str, *, name: str) -> None:
        """
        Update a branch.

        Args:
            owner: owner of the repo
            repo: name of the repo
            branch: name of the branch
            name: New branch name

        Returns:
            No content.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: repoUpdateBranch
        """
        _payload = UpdateBranchRepoOption(
            name=name,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = self._client._request("PATCH", f"/repos/{owner}/{repo}/branches/{branch}", json=_payload)
        return decode(_response, None)

    def delete(self, owner: str, repo: str, branch: str) -> None:
        """
        Delete a specific branch from a repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            branch: branch to delete

        Returns:
            No content.

        Raises:
            ForbiddenError: 403. APIError is error format response.
            NotFoundError: 404. APINotFound is a not found error response.
            LockedError: 423. APIRepoArchivedError is an error that is raised when an archived repo should be modified.

        Operation ID: repoDeleteBranch
        """
        _response = self._client._request("DELETE", f"/repos/{owner}/{repo}/branches/{branch}")
        return decode(_response, None)


class AsyncReposBranches:
    """The ``repos.branches`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def list(
        self,
        owner: str,
        repo: str,
        *,
        page: int | None = None,
        limit: int | None = None,
    ) -> AsyncPaginated[Branch]:
        """
        List a repository's branches.

        Args:
            owner: owner of the repo
            repo: name of the repo
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            BranchList.

        Operation ID: repoListBranches
        """
        return await self._client._paginate(
            "GET", f"/repos/{owner}/{repo}/branches", model=Branch, page=page, limit=limit
        )

    async def create(
        self,
        owner: str,
        repo: str,
        *,
        new_branch_name: str,
        old_branch_name: str | None = None,
        old_ref_name: str | None = None,
    ) -> Branch:
        """
        Create a branch.

        Args:
            owner: owner of the repo
            repo: name of the repo
            new_branch_name: Name of the branch to create
            old_branch_name: Deprecated: true Name of the old branch to create from
            old_ref_name: Name of the old branch/tag/commit to create from

        Returns:
            Branch.

        Raises:
            ForbiddenError: 403. The branch is archived or a mirror.
            NotFoundError: 404. The old branch does not exist.
            ConflictError: 409. The branch with the same name already exists.
            PayloadTooLargeError: 413. QuotaExceeded.
            LockedError: 423. APIRepoArchivedError is an error that is raised when an archived repo should be modified.

        Operation ID: repoCreateBranch
        """
        _payload = CreateBranchRepoOption(
            new_branch_name=new_branch_name,
            old_branch_name=old_branch_name,
            old_ref_name=old_ref_name,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = await self._client._request("POST", f"/repos/{owner}/{repo}/branches", json=_payload)
        return decode(_response, Branch)

    async def get(self, owner: str, repo: str, branch: str) -> Branch:
        """
        Retrieve a specific branch from a repository, including its effective branch protection.

        Args:
            owner: owner of the repo
            repo: name of the repo
            branch: branch to get

        Returns:
            Branch.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoGetBranch
        """
        _response = await self._client._request("GET", f"/repos/{owner}/{repo}/branches/{branch}")
        return decode(_response, Branch)

    async def update(self, owner: str, repo: str, branch: str, *, name: str) -> None:
        """
        Update a branch.

        Args:
            owner: owner of the repo
            repo: name of the repo
            branch: name of the branch
            name: New branch name

        Returns:
            No content.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: repoUpdateBranch
        """
        _payload = UpdateBranchRepoOption(
            name=name,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = await self._client._request("PATCH", f"/repos/{owner}/{repo}/branches/{branch}", json=_payload)
        return decode(_response, None)

    async def delete(self, owner: str, repo: str, branch: str) -> None:
        """
        Delete a specific branch from a repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            branch: branch to delete

        Returns:
            No content.

        Raises:
            ForbiddenError: 403. APIError is error format response.
            NotFoundError: 404. APINotFound is a not found error response.
            LockedError: 423. APIRepoArchivedError is an error that is raised when an archived repo should be modified.

        Operation ID: repoDeleteBranch
        """
        _response = await self._client._request("DELETE", f"/repos/{owner}/{repo}/branches/{branch}")
        return decode(_response, None)


class ReposCollaborators:
    """The ``repos.collaborators`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def list(self, owner: str, repo: str, *, page: int | None = None, limit: int | None = None) -> Paginated[User]:
        """
        List a repository's collaborators.

        Args:
            owner: owner of the repo
            repo: name of the repo
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            UserList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoListCollaborators
        """
        return self._client._paginate("GET", f"/repos/{owner}/{repo}/collaborators", model=User, page=page, limit=limit)

    def get(self, owner: str, repo: str, collaborator: str) -> None:
        """
        Check if a user is a collaborator of a repository.

        If the user is a collaborator, return 204. If the user is not a collaborator, return 404.

        Args:
            owner: owner of the repo
            repo: name of the repo
            collaborator: username of the collaborator

        Returns:
            No content.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: repoCheckCollaborator
        """
        _response = self._client._request("GET", f"/repos/{owner}/{repo}/collaborators/{collaborator}")
        return decode(_response, None)

    def add(
        self,
        owner: str,
        repo: str,
        collaborator: str,
        *,
        permission: AddCollaboratorOptionPermission | None = None,
    ) -> None:
        """
        Add a collaborator to a repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            collaborator: username of the collaborator to add
            permission:

        Returns:
            No content.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: repoAddCollaborator
        """
        if permission is not None:
            _payload = AddCollaboratorOption(permission=permission).model_dump(
                mode="json", by_alias=True, exclude_none=True
            )
        else:
            _payload = None

        _response = self._client._request("PUT", f"/repos/{owner}/{repo}/collaborators/{collaborator}", json=_payload)
        return decode(_response, None)

    def remove(self, owner: str, repo: str, collaborator: str) -> None:
        """
        Delete a collaborator from a repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            collaborator: username of the collaborator to delete

        Returns:
            No content.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: repoDeleteCollaborator
        """
        _response = self._client._request("DELETE", f"/repos/{owner}/{repo}/collaborators/{collaborator}")
        return decode(_response, None)

    def permission(self, owner: str, repo: str, collaborator: str) -> RepoCollaboratorPermission:
        """
        Get repository permissions for a user.

        Args:
            owner: owner of the repo
            repo: name of the repo
            collaborator: username of the collaborator

        Returns:
            RepoCollaboratorPermission.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoGetRepoPermissions
        """
        _response = self._client._request("GET", f"/repos/{owner}/{repo}/collaborators/{collaborator}/permission")
        return decode(_response, RepoCollaboratorPermission)


class AsyncReposCollaborators:
    """The ``repos.collaborators`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def list(
        self,
        owner: str,
        repo: str,
        *,
        page: int | None = None,
        limit: int | None = None,
    ) -> AsyncPaginated[User]:
        """
        List a repository's collaborators.

        Args:
            owner: owner of the repo
            repo: name of the repo
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            UserList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoListCollaborators
        """
        return await self._client._paginate(
            "GET", f"/repos/{owner}/{repo}/collaborators", model=User, page=page, limit=limit
        )

    async def get(self, owner: str, repo: str, collaborator: str) -> None:
        """
        Check if a user is a collaborator of a repository.

        If the user is a collaborator, return 204. If the user is not a collaborator, return 404.

        Args:
            owner: owner of the repo
            repo: name of the repo
            collaborator: username of the collaborator

        Returns:
            No content.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: repoCheckCollaborator
        """
        _response = await self._client._request("GET", f"/repos/{owner}/{repo}/collaborators/{collaborator}")
        return decode(_response, None)

    async def add(
        self,
        owner: str,
        repo: str,
        collaborator: str,
        *,
        permission: AddCollaboratorOptionPermission | None = None,
    ) -> None:
        """
        Add a collaborator to a repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            collaborator: username of the collaborator to add
            permission:

        Returns:
            No content.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: repoAddCollaborator
        """
        if permission is not None:
            _payload = AddCollaboratorOption(permission=permission).model_dump(
                mode="json", by_alias=True, exclude_none=True
            )
        else:
            _payload = None

        _response = await self._client._request(
            "PUT", f"/repos/{owner}/{repo}/collaborators/{collaborator}", json=_payload
        )
        return decode(_response, None)

    async def remove(self, owner: str, repo: str, collaborator: str) -> None:
        """
        Delete a collaborator from a repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            collaborator: username of the collaborator to delete

        Returns:
            No content.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: repoDeleteCollaborator
        """
        _response = await self._client._request("DELETE", f"/repos/{owner}/{repo}/collaborators/{collaborator}")
        return decode(_response, None)

    async def permission(self, owner: str, repo: str, collaborator: str) -> RepoCollaboratorPermission:
        """
        Get repository permissions for a user.

        Args:
            owner: owner of the repo
            repo: name of the repo
            collaborator: username of the collaborator

        Returns:
            RepoCollaboratorPermission.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoGetRepoPermissions
        """
        _response = await self._client._request("GET", f"/repos/{owner}/{repo}/collaborators/{collaborator}/permission")
        return decode(_response, RepoCollaboratorPermission)


class ReposCommits:
    """The ``repos.commits`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def list(
        self,
        owner: str,
        repo: str,
        *,
        sha: str | None = None,
        path: str | None = None,
        stat: bool | None = None,
        verification: bool | None = None,
        files: bool | None = None,
        not_: str | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> Paginated[Commit]:
        """
        Get a list of all commits from a repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            sha: SHA or branch to start listing commits from (usually 'master')
            path: filepath of a file/dir
            stat: include diff stats for every commit (disable for speedup, default 'true')
            verification: include verification for every commit (disable for speedup, default 'true')
            files: include a list of affected files for every commit (disable for speedup, default 'true')
            not_: commits that match the given specifier will not be listed.
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            CommitList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.
            ConflictError: 409. EmptyRepository.

        Operation ID: repoGetAllCommits
        """
        _query: dict[str, object] = {
            "sha": sha,
            "path": path,
            "stat": stat,
            "verification": verification,
            "files": files,
            "not": not_,
        }

        return self._client._paginate(
            "GET", f"/repos/{owner}/{repo}/commits", model=Commit, params=_query, page=page, limit=limit
        )

    def status(
        self,
        owner: str,
        repo: str,
        ref: str,
        *,
        page: int | None = None,
        limit: int | None = None,
    ) -> CombinedStatus:
        """
        Get a commit's combined status, by branch/tag/commit reference.

        Args:
            owner: owner of the repo
            repo: name of the repo
            ref: name of branch/tag/commit
            page: page number of results to return (1-based)
            limit: page size of results

        Returns:
            CombinedStatus.

        Raises:
            BadRequestError: 400. APIError is error format response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoGetCombinedStatusByRef
        """
        _query: dict[str, object] = {"page": page, "limit": limit}

        _response = self._client._request("GET", f"/repos/{owner}/{repo}/commits/{ref}/status", params=_query)
        return decode(_response, CombinedStatus)

    def statuses(
        self,
        owner: str,
        repo: str,
        ref: str,
        *,
        sort: Literal["oldest", "recentupdate", "leastupdate", "leastindex", "highestindex"] | None = None,
        state: Literal["pending", "success", "error", "failure", "warning"] | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> Paginated[CommitStatus]:
        """
        Get a commit's statuses, by branch/tag/commit reference.

        Args:
            owner: owner of the repo
            repo: name of the repo
            ref: name of branch/tag/commit
            sort: type of sort
            state: type of state
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            CommitStatusList.

        Raises:
            BadRequestError: 400. APIError is error format response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoListStatusesByRef
        """
        _query: dict[str, object] = {"sort": sort, "state": state}

        return self._client._paginate(
            "GET",
            f"/repos/{owner}/{repo}/commits/{ref}/statuses",
            model=CommitStatus,
            params=_query,
            page=page,
            limit=limit,
        )

    def pull_request(self, owner: str, repo: str, sha: str) -> PullRequest:
        """
        Get the pull request of the commit.

        Args:
            owner: owner of the repo
            repo: name of the repo
            sha: SHA of the commit to get

        Returns:
            PullRequest.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoGetCommitPullRequest
        """
        _response = self._client._request("GET", f"/repos/{owner}/{repo}/commits/{sha}/pull")
        return decode(_response, PullRequest)


class AsyncReposCommits:
    """The ``repos.commits`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def list(
        self,
        owner: str,
        repo: str,
        *,
        sha: str | None = None,
        path: str | None = None,
        stat: bool | None = None,
        verification: bool | None = None,
        files: bool | None = None,
        not_: str | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> AsyncPaginated[Commit]:
        """
        Get a list of all commits from a repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            sha: SHA or branch to start listing commits from (usually 'master')
            path: filepath of a file/dir
            stat: include diff stats for every commit (disable for speedup, default 'true')
            verification: include verification for every commit (disable for speedup, default 'true')
            files: include a list of affected files for every commit (disable for speedup, default 'true')
            not_: commits that match the given specifier will not be listed.
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            CommitList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.
            ConflictError: 409. EmptyRepository.

        Operation ID: repoGetAllCommits
        """
        _query: dict[str, object] = {
            "sha": sha,
            "path": path,
            "stat": stat,
            "verification": verification,
            "files": files,
            "not": not_,
        }

        return await self._client._paginate(
            "GET", f"/repos/{owner}/{repo}/commits", model=Commit, params=_query, page=page, limit=limit
        )

    async def status(
        self,
        owner: str,
        repo: str,
        ref: str,
        *,
        page: int | None = None,
        limit: int | None = None,
    ) -> CombinedStatus:
        """
        Get a commit's combined status, by branch/tag/commit reference.

        Args:
            owner: owner of the repo
            repo: name of the repo
            ref: name of branch/tag/commit
            page: page number of results to return (1-based)
            limit: page size of results

        Returns:
            CombinedStatus.

        Raises:
            BadRequestError: 400. APIError is error format response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoGetCombinedStatusByRef
        """
        _query: dict[str, object] = {"page": page, "limit": limit}

        _response = await self._client._request("GET", f"/repos/{owner}/{repo}/commits/{ref}/status", params=_query)
        return decode(_response, CombinedStatus)

    async def statuses(
        self,
        owner: str,
        repo: str,
        ref: str,
        *,
        sort: Literal["oldest", "recentupdate", "leastupdate", "leastindex", "highestindex"] | None = None,
        state: Literal["pending", "success", "error", "failure", "warning"] | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> AsyncPaginated[CommitStatus]:
        """
        Get a commit's statuses, by branch/tag/commit reference.

        Args:
            owner: owner of the repo
            repo: name of the repo
            ref: name of branch/tag/commit
            sort: type of sort
            state: type of state
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            CommitStatusList.

        Raises:
            BadRequestError: 400. APIError is error format response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoListStatusesByRef
        """
        _query: dict[str, object] = {"sort": sort, "state": state}

        return await self._client._paginate(
            "GET",
            f"/repos/{owner}/{repo}/commits/{ref}/statuses",
            model=CommitStatus,
            params=_query,
            page=page,
            limit=limit,
        )

    async def pull_request(self, owner: str, repo: str, sha: str) -> PullRequest:
        """
        Get the pull request of the commit.

        Args:
            owner: owner of the repo
            repo: name of the repo
            sha: SHA of the commit to get

        Returns:
            PullRequest.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoGetCommitPullRequest
        """
        _response = await self._client._request("GET", f"/repos/{owner}/{repo}/commits/{sha}/pull")
        return decode(_response, PullRequest)


class ReposContents:
    """The ``repos.contents`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def list(self, owner: str, repo: str, *, ref: str | None = None) -> builtins.list[ContentsResponse]:
        """
        Gets the metadata of all the entries of the root dir.

        Args:
            owner: owner of the repo
            repo: name of the repo
            ref: The name of the commit/branch/tag. Default the repository's default branch (usually master)

        Returns:
            ContentsListResponse.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoGetContentsList
        """
        _query: dict[str, object] = {"ref": ref}

        _response = self._client._request("GET", f"/repos/{owner}/{repo}/contents", params=_query)
        return decode(_response, list[ContentsResponse])

    def change_files(
        self,
        owner: str,
        repo: str,
        *,
        author: Identity | None = None,
        branch: str | None = None,
        committer: Identity | None = None,
        dates: CommitDateOptions | None = None,
        files: builtins.list[ChangeFileOperation],
        force_overwrite_new_branch: bool | None = None,
        message: str | None = None,
        new_branch: str | None = None,
        signoff: bool | None = None,
    ) -> FilesResponse:
        """
        Modify multiple files in a repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            author:
            branch: branch (optional) to base this file from. if not given, the default branch is used
            committer:
            dates:
            files: list of file operations
            force_overwrite_new_branch: (optional) will do a force-push if the new branch already exists
            message: message (optional) for the commit of this file. if not supplied, a default message will be used
            new_branch: new_branch (optional) will make a new branch from `branch` before creating the file
            signoff: Add a Signed-off-by trailer by the committer at the end of the commit log message.

        Returns:
            FilesResponse.

        Raises:
            ForbiddenError: 403. APIError is error format response.
            NotFoundError: 404. APINotFound is a not found error response.
            ConflictError: 409. APIConflict is a conflict empty response.
            PayloadTooLargeError: 413. QuotaExceeded.
            UnprocessableEntityError: 422. APIError is error format response.
            LockedError: 423. APIRepoArchivedError is an error that is raised when an archived repo should be modified.

        Operation ID: repoChangeFiles
        """
        _payload = ChangeFilesOptions(
            author=author,
            branch=branch,
            committer=committer,
            dates=dates,
            files=files,
            force_overwrite_new_branch=force_overwrite_new_branch,
            message=message,
            new_branch=new_branch,
            signoff=signoff,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = self._client._request("POST", f"/repos/{owner}/{repo}/contents", json=_payload)
        return decode(_response, FilesResponse)

    def get(self, owner: str, repo: str, filepath: str, *, ref: str | None = None) -> ContentsResponse:
        """
        Gets the metadata and contents (if a file) of an entry in a repository, or a list of entries if a dir.

        Args:
            owner: owner of the repo
            repo: name of the repo
            filepath: path of the dir, file, symlink or submodule in the repo
            ref: The name of the commit/branch/tag. Default the repository's default branch (usually master)

        Returns:
            ContentsResponse.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoGetContents
        """
        _query: dict[str, object] = {"ref": ref}

        _response = self._client._request("GET", f"/repos/{owner}/{repo}/contents/{filepath}", params=_query)
        return decode(_response, ContentsResponse)

    def create(
        self,
        owner: str,
        repo: str,
        filepath: str,
        *,
        author: Identity | None = None,
        branch: str | None = None,
        committer: Identity | None = None,
        content: str,
        dates: CommitDateOptions | None = None,
        force_overwrite_new_branch: bool | None = None,
        message: str | None = None,
        new_branch: str | None = None,
        signoff: bool | None = None,
    ) -> FileResponse:
        """
        Create a file in a repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            filepath: path of the file to create
            author:
            branch: branch (optional) to base this file from. if not given, the default branch is used
            committer:
            content: content must be base64 encoded
            dates:
            force_overwrite_new_branch: (optional) will do a force-push if the new branch already exists
            message: message (optional) for the commit of this file. if not supplied, a default message will be used
            new_branch: new_branch (optional) will make a new branch from `branch` before creating the file
            signoff: Add a Signed-off-by trailer by the committer at the end of the commit log message.

        Returns:
            FileResponse.

        Raises:
            ForbiddenError: 403. APIError is error format response.
            NotFoundError: 404. APINotFound is a not found error response.
            ConflictError: 409. APIConflict is a conflict empty response.
            PayloadTooLargeError: 413. QuotaExceeded.
            UnprocessableEntityError: 422. APIError is error format response.
            LockedError: 423. APIRepoArchivedError is an error that is raised when an archived repo should be modified.

        Operation ID: repoCreateFile
        """
        _payload = CreateFileOptions(
            author=author,
            branch=branch,
            committer=committer,
            content=content,
            dates=dates,
            force_overwrite_new_branch=force_overwrite_new_branch,
            message=message,
            new_branch=new_branch,
            signoff=signoff,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = self._client._request("POST", f"/repos/{owner}/{repo}/contents/{filepath}", json=_payload)
        return decode(_response, FileResponse)

    def update(
        self,
        owner: str,
        repo: str,
        filepath: str,
        *,
        author: Identity | None = None,
        branch: str | None = None,
        committer: Identity | None = None,
        content: str,
        dates: CommitDateOptions | None = None,
        force_overwrite_new_branch: bool | None = None,
        from_path: str | None = None,
        message: str | None = None,
        new_branch: str | None = None,
        sha: str,
        signoff: bool | None = None,
    ) -> FileResponse:
        """
        Update a file in a repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            filepath: path of the file to update
            author:
            branch: branch (optional) to base this file from. if not given, the default branch is used
            committer:
            content: content must be base64 encoded
            dates:
            force_overwrite_new_branch: (optional) will do a force-push if the new branch already exists
            from_path: from_path (optional) is the path of the original file which will be moved/renamed to the path in
                the URL
            message: message (optional) for the commit of this file. if not supplied, a default message will be used
            new_branch: new_branch (optional) will make a new branch from `branch` before creating the file
            sha: sha is the SHA for the file that already exists
            signoff: Add a Signed-off-by trailer by the committer at the end of the commit log message.

        Returns:
            FileResponse.

        Raises:
            ForbiddenError: 403. APIError is error format response.
            NotFoundError: 404. APINotFound is a not found error response.
            ConflictError: 409. APIConflict is a conflict empty response.
            PayloadTooLargeError: 413. QuotaExceeded.
            UnprocessableEntityError: 422. APIError is error format response.
            LockedError: 423. APIRepoArchivedError is an error that is raised when an archived repo should be modified.

        Operation ID: repoUpdateFile
        """
        _payload = UpdateFileOptions(
            author=author,
            branch=branch,
            committer=committer,
            content=content,
            dates=dates,
            force_overwrite_new_branch=force_overwrite_new_branch,
            from_path=from_path,
            message=message,
            new_branch=new_branch,
            sha=sha,
            signoff=signoff,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = self._client._request("PUT", f"/repos/{owner}/{repo}/contents/{filepath}", json=_payload)
        return decode(_response, FileResponse)

    def delete(
        self,
        owner: str,
        repo: str,
        filepath: str,
        *,
        author: Identity | None = None,
        branch: str | None = None,
        committer: Identity | None = None,
        dates: CommitDateOptions | None = None,
        force_overwrite_new_branch: bool | None = None,
        message: str | None = None,
        new_branch: str | None = None,
        sha: str,
        signoff: bool | None = None,
    ) -> FileDeleteResponse:
        """
        Delete a file in a repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            filepath: path of the file to delete
            author:
            branch: branch (optional) to base this file from. if not given, the default branch is used
            committer:
            dates:
            force_overwrite_new_branch: (optional) will do a force-push if the new branch already exists
            message: message (optional) for the commit of this file. if not supplied, a default message will be used
            new_branch: new_branch (optional) will make a new branch from `branch` before creating the file
            sha: sha is the SHA for the file that already exists
            signoff: Add a Signed-off-by trailer by the committer at the end of the commit log message.

        Returns:
            FileDeleteResponse.

        Raises:
            BadRequestError: 400. APIError is error format response.
            ForbiddenError: 403. APIError is error format response.
            NotFoundError: 404. APIError is error format response.
            PayloadTooLargeError: 413. QuotaExceeded.
            LockedError: 423. APIRepoArchivedError is an error that is raised when an archived repo should be modified.

        Operation ID: repoDeleteFile
        """
        _payload = DeleteFileOptions(
            author=author,
            branch=branch,
            committer=committer,
            dates=dates,
            force_overwrite_new_branch=force_overwrite_new_branch,
            message=message,
            new_branch=new_branch,
            sha=sha,
            signoff=signoff,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = self._client._request("DELETE", f"/repos/{owner}/{repo}/contents/{filepath}", json=_payload)
        return decode(_response, FileDeleteResponse)


class AsyncReposContents:
    """The ``repos.contents`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def list(self, owner: str, repo: str, *, ref: str | None = None) -> builtins.list[ContentsResponse]:
        """
        Gets the metadata of all the entries of the root dir.

        Args:
            owner: owner of the repo
            repo: name of the repo
            ref: The name of the commit/branch/tag. Default the repository's default branch (usually master)

        Returns:
            ContentsListResponse.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoGetContentsList
        """
        _query: dict[str, object] = {"ref": ref}

        _response = await self._client._request("GET", f"/repos/{owner}/{repo}/contents", params=_query)
        return decode(_response, list[ContentsResponse])

    async def change_files(
        self,
        owner: str,
        repo: str,
        *,
        author: Identity | None = None,
        branch: str | None = None,
        committer: Identity | None = None,
        dates: CommitDateOptions | None = None,
        files: builtins.list[ChangeFileOperation],
        force_overwrite_new_branch: bool | None = None,
        message: str | None = None,
        new_branch: str | None = None,
        signoff: bool | None = None,
    ) -> FilesResponse:
        """
        Modify multiple files in a repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            author:
            branch: branch (optional) to base this file from. if not given, the default branch is used
            committer:
            dates:
            files: list of file operations
            force_overwrite_new_branch: (optional) will do a force-push if the new branch already exists
            message: message (optional) for the commit of this file. if not supplied, a default message will be used
            new_branch: new_branch (optional) will make a new branch from `branch` before creating the file
            signoff: Add a Signed-off-by trailer by the committer at the end of the commit log message.

        Returns:
            FilesResponse.

        Raises:
            ForbiddenError: 403. APIError is error format response.
            NotFoundError: 404. APINotFound is a not found error response.
            ConflictError: 409. APIConflict is a conflict empty response.
            PayloadTooLargeError: 413. QuotaExceeded.
            UnprocessableEntityError: 422. APIError is error format response.
            LockedError: 423. APIRepoArchivedError is an error that is raised when an archived repo should be modified.

        Operation ID: repoChangeFiles
        """
        _payload = ChangeFilesOptions(
            author=author,
            branch=branch,
            committer=committer,
            dates=dates,
            files=files,
            force_overwrite_new_branch=force_overwrite_new_branch,
            message=message,
            new_branch=new_branch,
            signoff=signoff,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = await self._client._request("POST", f"/repos/{owner}/{repo}/contents", json=_payload)
        return decode(_response, FilesResponse)

    async def get(self, owner: str, repo: str, filepath: str, *, ref: str | None = None) -> ContentsResponse:
        """
        Gets the metadata and contents (if a file) of an entry in a repository, or a list of entries if a dir.

        Args:
            owner: owner of the repo
            repo: name of the repo
            filepath: path of the dir, file, symlink or submodule in the repo
            ref: The name of the commit/branch/tag. Default the repository's default branch (usually master)

        Returns:
            ContentsResponse.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoGetContents
        """
        _query: dict[str, object] = {"ref": ref}

        _response = await self._client._request("GET", f"/repos/{owner}/{repo}/contents/{filepath}", params=_query)
        return decode(_response, ContentsResponse)

    async def create(
        self,
        owner: str,
        repo: str,
        filepath: str,
        *,
        author: Identity | None = None,
        branch: str | None = None,
        committer: Identity | None = None,
        content: str,
        dates: CommitDateOptions | None = None,
        force_overwrite_new_branch: bool | None = None,
        message: str | None = None,
        new_branch: str | None = None,
        signoff: bool | None = None,
    ) -> FileResponse:
        """
        Create a file in a repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            filepath: path of the file to create
            author:
            branch: branch (optional) to base this file from. if not given, the default branch is used
            committer:
            content: content must be base64 encoded
            dates:
            force_overwrite_new_branch: (optional) will do a force-push if the new branch already exists
            message: message (optional) for the commit of this file. if not supplied, a default message will be used
            new_branch: new_branch (optional) will make a new branch from `branch` before creating the file
            signoff: Add a Signed-off-by trailer by the committer at the end of the commit log message.

        Returns:
            FileResponse.

        Raises:
            ForbiddenError: 403. APIError is error format response.
            NotFoundError: 404. APINotFound is a not found error response.
            ConflictError: 409. APIConflict is a conflict empty response.
            PayloadTooLargeError: 413. QuotaExceeded.
            UnprocessableEntityError: 422. APIError is error format response.
            LockedError: 423. APIRepoArchivedError is an error that is raised when an archived repo should be modified.

        Operation ID: repoCreateFile
        """
        _payload = CreateFileOptions(
            author=author,
            branch=branch,
            committer=committer,
            content=content,
            dates=dates,
            force_overwrite_new_branch=force_overwrite_new_branch,
            message=message,
            new_branch=new_branch,
            signoff=signoff,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = await self._client._request("POST", f"/repos/{owner}/{repo}/contents/{filepath}", json=_payload)
        return decode(_response, FileResponse)

    async def update(
        self,
        owner: str,
        repo: str,
        filepath: str,
        *,
        author: Identity | None = None,
        branch: str | None = None,
        committer: Identity | None = None,
        content: str,
        dates: CommitDateOptions | None = None,
        force_overwrite_new_branch: bool | None = None,
        from_path: str | None = None,
        message: str | None = None,
        new_branch: str | None = None,
        sha: str,
        signoff: bool | None = None,
    ) -> FileResponse:
        """
        Update a file in a repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            filepath: path of the file to update
            author:
            branch: branch (optional) to base this file from. if not given, the default branch is used
            committer:
            content: content must be base64 encoded
            dates:
            force_overwrite_new_branch: (optional) will do a force-push if the new branch already exists
            from_path: from_path (optional) is the path of the original file which will be moved/renamed to the path in
                the URL
            message: message (optional) for the commit of this file. if not supplied, a default message will be used
            new_branch: new_branch (optional) will make a new branch from `branch` before creating the file
            sha: sha is the SHA for the file that already exists
            signoff: Add a Signed-off-by trailer by the committer at the end of the commit log message.

        Returns:
            FileResponse.

        Raises:
            ForbiddenError: 403. APIError is error format response.
            NotFoundError: 404. APINotFound is a not found error response.
            ConflictError: 409. APIConflict is a conflict empty response.
            PayloadTooLargeError: 413. QuotaExceeded.
            UnprocessableEntityError: 422. APIError is error format response.
            LockedError: 423. APIRepoArchivedError is an error that is raised when an archived repo should be modified.

        Operation ID: repoUpdateFile
        """
        _payload = UpdateFileOptions(
            author=author,
            branch=branch,
            committer=committer,
            content=content,
            dates=dates,
            force_overwrite_new_branch=force_overwrite_new_branch,
            from_path=from_path,
            message=message,
            new_branch=new_branch,
            sha=sha,
            signoff=signoff,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = await self._client._request("PUT", f"/repos/{owner}/{repo}/contents/{filepath}", json=_payload)
        return decode(_response, FileResponse)

    async def delete(
        self,
        owner: str,
        repo: str,
        filepath: str,
        *,
        author: Identity | None = None,
        branch: str | None = None,
        committer: Identity | None = None,
        dates: CommitDateOptions | None = None,
        force_overwrite_new_branch: bool | None = None,
        message: str | None = None,
        new_branch: str | None = None,
        sha: str,
        signoff: bool | None = None,
    ) -> FileDeleteResponse:
        """
        Delete a file in a repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            filepath: path of the file to delete
            author:
            branch: branch (optional) to base this file from. if not given, the default branch is used
            committer:
            dates:
            force_overwrite_new_branch: (optional) will do a force-push if the new branch already exists
            message: message (optional) for the commit of this file. if not supplied, a default message will be used
            new_branch: new_branch (optional) will make a new branch from `branch` before creating the file
            sha: sha is the SHA for the file that already exists
            signoff: Add a Signed-off-by trailer by the committer at the end of the commit log message.

        Returns:
            FileDeleteResponse.

        Raises:
            BadRequestError: 400. APIError is error format response.
            ForbiddenError: 403. APIError is error format response.
            NotFoundError: 404. APIError is error format response.
            PayloadTooLargeError: 413. QuotaExceeded.
            LockedError: 423. APIRepoArchivedError is an error that is raised when an archived repo should be modified.

        Operation ID: repoDeleteFile
        """
        _payload = DeleteFileOptions(
            author=author,
            branch=branch,
            committer=committer,
            dates=dates,
            force_overwrite_new_branch=force_overwrite_new_branch,
            message=message,
            new_branch=new_branch,
            sha=sha,
            signoff=signoff,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = await self._client._request("DELETE", f"/repos/{owner}/{repo}/contents/{filepath}", json=_payload)
        return decode(_response, FileDeleteResponse)


class ReposEditorconfig:
    """The ``repos.editorconfig`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def get(self, owner: str, repo: str, filepath: str, *, ref: str | None = None) -> dict[str, str]:
        """
        Get the EditorConfig definitions of a file in a repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            filepath: filepath of file to get
            ref: The name of the commit/branch/tag. Default the repository's default branch (usually master)

        Returns:
            definitions.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoGetEditorConfig
        """
        _query: dict[str, object] = {"ref": ref}

        _response = self._client._request("GET", f"/repos/{owner}/{repo}/editorconfig/{filepath}", params=_query)
        return decode(_response, dict[str, str])


class AsyncReposEditorconfig:
    """The ``repos.editorconfig`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def get(self, owner: str, repo: str, filepath: str, *, ref: str | None = None) -> dict[str, str]:
        """
        Get the EditorConfig definitions of a file in a repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            filepath: filepath of file to get
            ref: The name of the commit/branch/tag. Default the repository's default branch (usually master)

        Returns:
            definitions.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoGetEditorConfig
        """
        _query: dict[str, object] = {"ref": ref}

        _response = await self._client._request("GET", f"/repos/{owner}/{repo}/editorconfig/{filepath}", params=_query)
        return decode(_response, dict[str, str])


class ReposFlags:
    """The ``repos.flags`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def list(self, owner: str, repo: str) -> builtins.list[str]:
        """
        List a repository's flags.

        Args:
            owner: owner of the repo
            repo: name of the repo

        Returns:
            StringSlice.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoListFlags
        """
        _response = self._client._request("GET", f"/repos/{owner}/{repo}/flags")
        return decode(_response, list[str])

    def update(self, owner: str, repo: str, *, flags: builtins.list[str] | None = None) -> None:
        """
        Replace all flags of a repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            flags:

        Returns:
            No content.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoReplaceAllFlags
        """
        if flags is not None:
            _payload = ReplaceFlagsOption(flags=flags).model_dump(mode="json", by_alias=True, exclude_none=True)
        else:
            _payload = None

        _response = self._client._request("PUT", f"/repos/{owner}/{repo}/flags", json=_payload)
        return decode(_response, None)

    def delete_all(self, owner: str, repo: str) -> None:
        """
        Remove all flags from a repository.

        Args:
            owner: owner of the repo
            repo: name of the repo

        Returns:
            No content.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoDeleteAllFlags
        """
        _response = self._client._request("DELETE", f"/repos/{owner}/{repo}/flags")
        return decode(_response, None)

    def get(self, owner: str, repo: str, flag: str) -> None:
        """
        Check if a repository has a given flag.

        Args:
            owner: owner of the repo
            repo: name of the repo
            flag: name of the flag

        Returns:
            No content.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoCheckFlag
        """
        _response = self._client._request("GET", f"/repos/{owner}/{repo}/flags/{flag}")
        return decode(_response, None)

    def add(self, owner: str, repo: str, flag: str) -> None:
        """
        Add a flag to a repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            flag: name of the flag

        Returns:
            No content.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoAddFlag
        """
        _response = self._client._request("PUT", f"/repos/{owner}/{repo}/flags/{flag}")
        return decode(_response, None)

    def remove(self, owner: str, repo: str, flag: str) -> None:
        """
        Remove a flag from a repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            flag: name of the flag

        Returns:
            No content.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoDeleteFlag
        """
        _response = self._client._request("DELETE", f"/repos/{owner}/{repo}/flags/{flag}")
        return decode(_response, None)


class AsyncReposFlags:
    """The ``repos.flags`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def list(self, owner: str, repo: str) -> builtins.list[str]:
        """
        List a repository's flags.

        Args:
            owner: owner of the repo
            repo: name of the repo

        Returns:
            StringSlice.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoListFlags
        """
        _response = await self._client._request("GET", f"/repos/{owner}/{repo}/flags")
        return decode(_response, list[str])

    async def update(self, owner: str, repo: str, *, flags: builtins.list[str] | None = None) -> None:
        """
        Replace all flags of a repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            flags:

        Returns:
            No content.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoReplaceAllFlags
        """
        if flags is not None:
            _payload = ReplaceFlagsOption(flags=flags).model_dump(mode="json", by_alias=True, exclude_none=True)
        else:
            _payload = None

        _response = await self._client._request("PUT", f"/repos/{owner}/{repo}/flags", json=_payload)
        return decode(_response, None)

    async def delete_all(self, owner: str, repo: str) -> None:
        """
        Remove all flags from a repository.

        Args:
            owner: owner of the repo
            repo: name of the repo

        Returns:
            No content.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoDeleteAllFlags
        """
        _response = await self._client._request("DELETE", f"/repos/{owner}/{repo}/flags")
        return decode(_response, None)

    async def get(self, owner: str, repo: str, flag: str) -> None:
        """
        Check if a repository has a given flag.

        Args:
            owner: owner of the repo
            repo: name of the repo
            flag: name of the flag

        Returns:
            No content.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoCheckFlag
        """
        _response = await self._client._request("GET", f"/repos/{owner}/{repo}/flags/{flag}")
        return decode(_response, None)

    async def add(self, owner: str, repo: str, flag: str) -> None:
        """
        Add a flag to a repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            flag: name of the flag

        Returns:
            No content.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoAddFlag
        """
        _response = await self._client._request("PUT", f"/repos/{owner}/{repo}/flags/{flag}")
        return decode(_response, None)

    async def remove(self, owner: str, repo: str, flag: str) -> None:
        """
        Remove a flag from a repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            flag: name of the flag

        Returns:
            No content.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoDeleteFlag
        """
        _response = await self._client._request("DELETE", f"/repos/{owner}/{repo}/flags/{flag}")
        return decode(_response, None)


class ReposForks:
    """The ``repos.forks`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def list(
        self,
        owner: str,
        repo: str,
        *,
        page: int | None = None,
        limit: int | None = None,
    ) -> Paginated[Repository]:
        """
        List a repository's forks.

        Args:
            owner: owner of the repo
            repo: name of the repo
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            RepositoryList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: listForks
        """
        return self._client._paginate("GET", f"/repos/{owner}/{repo}/forks", model=Repository, page=page, limit=limit)

    def create(self, owner: str, repo: str, *, name: str | None = None, organization: str | None = None) -> Repository:
        """
        Fork a repository.

        Args:
            owner: owner of the repo to fork
            repo: name of the repo to fork
            name: name of the forked repository
            organization: organization name, if forking into an organization

        Returns:
            Repository.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.
            ConflictError: 409. The repository with the same name already exists.
            PayloadTooLargeError: 413. QuotaExceeded.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: createFork
        """
        if name is not None or organization is not None:
            _payload = CreateForkOption(name=name, organization=organization).model_dump(
                mode="json", by_alias=True, exclude_none=True
            )
        else:
            _payload = None

        _response = self._client._request("POST", f"/repos/{owner}/{repo}/forks", json=_payload)
        return decode(_response, Repository)


class AsyncReposForks:
    """The ``repos.forks`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def list(
        self,
        owner: str,
        repo: str,
        *,
        page: int | None = None,
        limit: int | None = None,
    ) -> AsyncPaginated[Repository]:
        """
        List a repository's forks.

        Args:
            owner: owner of the repo
            repo: name of the repo
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            RepositoryList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: listForks
        """
        return await self._client._paginate(
            "GET", f"/repos/{owner}/{repo}/forks", model=Repository, page=page, limit=limit
        )

    async def create(
        self,
        owner: str,
        repo: str,
        *,
        name: str | None = None,
        organization: str | None = None,
    ) -> Repository:
        """
        Fork a repository.

        Args:
            owner: owner of the repo to fork
            repo: name of the repo to fork
            name: name of the forked repository
            organization: organization name, if forking into an organization

        Returns:
            Repository.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.
            ConflictError: 409. The repository with the same name already exists.
            PayloadTooLargeError: 413. QuotaExceeded.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: createFork
        """
        if name is not None or organization is not None:
            _payload = CreateForkOption(name=name, organization=organization).model_dump(
                mode="json", by_alias=True, exclude_none=True
            )
        else:
            _payload = None

        _response = await self._client._request("POST", f"/repos/{owner}/{repo}/forks", json=_payload)
        return decode(_response, Repository)


class ReposGit:
    """The ``repos.git`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client
        self.blobs: ReposGitBlobs = ReposGitBlobs(client)
        self.commits: ReposGitCommits = ReposGitCommits(client)
        self.notes: ReposGitNotes = ReposGitNotes(client)
        self.refs: ReposGitRefs = ReposGitRefs(client)
        self.tags: ReposGitTags = ReposGitTags(client)
        self.trees: ReposGitTrees = ReposGitTrees(client)


class AsyncReposGit:
    """The ``repos.git`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client
        self.blobs: AsyncReposGitBlobs = AsyncReposGitBlobs(client)
        self.commits: AsyncReposGitCommits = AsyncReposGitCommits(client)
        self.notes: AsyncReposGitNotes = AsyncReposGitNotes(client)
        self.refs: AsyncReposGitRefs = AsyncReposGitRefs(client)
        self.tags: AsyncReposGitTags = AsyncReposGitTags(client)
        self.trees: AsyncReposGitTrees = AsyncReposGitTrees(client)


class ReposGitBlobs:
    """The ``repos.git.blobs`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def list(self, owner: str, repo: str, *, shas: str) -> builtins.list[GitBlob]:
        """
        Gets multiple blobs of a repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            shas: a comma separated list of blob-sha (mind the overall URL-length limit of ~2,083 chars)

        Returns:
            GitBlobList.

        Raises:
            BadRequestError: 400. APIError is error format response.

        Operation ID: GetBlobs
        """
        _query: dict[str, object] = {"shas": shas}

        _response = self._client._request("GET", f"/repos/{owner}/{repo}/git/blobs", params=_query)
        return decode(_response, list[GitBlob])

    def get(self, owner: str, repo: str, sha: str) -> GitBlob:
        """
        Gets the blob of a repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            sha: sha of the blob to retrieve

        Returns:
            GitBlob.

        Raises:
            BadRequestError: 400. APIError is error format response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: GetBlob
        """
        _response = self._client._request("GET", f"/repos/{owner}/{repo}/git/blobs/{sha}")
        return decode(_response, GitBlob)


class AsyncReposGitBlobs:
    """The ``repos.git.blobs`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def list(self, owner: str, repo: str, *, shas: str) -> builtins.list[GitBlob]:
        """
        Gets multiple blobs of a repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            shas: a comma separated list of blob-sha (mind the overall URL-length limit of ~2,083 chars)

        Returns:
            GitBlobList.

        Raises:
            BadRequestError: 400. APIError is error format response.

        Operation ID: GetBlobs
        """
        _query: dict[str, object] = {"shas": shas}

        _response = await self._client._request("GET", f"/repos/{owner}/{repo}/git/blobs", params=_query)
        return decode(_response, list[GitBlob])

    async def get(self, owner: str, repo: str, sha: str) -> GitBlob:
        """
        Gets the blob of a repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            sha: sha of the blob to retrieve

        Returns:
            GitBlob.

        Raises:
            BadRequestError: 400. APIError is error format response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: GetBlob
        """
        _response = await self._client._request("GET", f"/repos/{owner}/{repo}/git/blobs/{sha}")
        return decode(_response, GitBlob)


class ReposGitCommits:
    """The ``repos.git.commits`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def get(
        self,
        owner: str,
        repo: str,
        sha: str,
        *,
        stat: bool | None = None,
        verification: bool | None = None,
        files: bool | None = None,
    ) -> Commit:
        """
        Get a single commit from a repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            sha: a git ref or commit sha
            stat: include diff stats for every commit (disable for speedup, default 'true')
            verification: include verification for every commit (disable for speedup, default 'true')
            files: include a list of affected files for every commit (disable for speedup, default 'true')

        Returns:
            Commit.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: repoGetSingleCommit
        """
        _query: dict[str, object] = {"stat": stat, "verification": verification, "files": files}

        _response = self._client._request("GET", f"/repos/{owner}/{repo}/git/commits/{sha}", params=_query)
        return decode(_response, Commit)

    def download(self, owner: str, repo: str, sha: str, diff_type: Literal["diff", "patch"]) -> str:
        """
        Get a commit's diff or patch.

        Args:
            owner: owner of the repo
            repo: name of the repo
            sha: SHA of the commit to get
            diff_type: whether the output is diff or patch

        Returns:
            APIString is a string response.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoDownloadCommitDiffOrPatch
        """
        _response = self._client._request("GET", f"/repos/{owner}/{repo}/git/commits/{sha}.{diff_type}")
        return decode(_response, str)


class AsyncReposGitCommits:
    """The ``repos.git.commits`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def get(
        self,
        owner: str,
        repo: str,
        sha: str,
        *,
        stat: bool | None = None,
        verification: bool | None = None,
        files: bool | None = None,
    ) -> Commit:
        """
        Get a single commit from a repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            sha: a git ref or commit sha
            stat: include diff stats for every commit (disable for speedup, default 'true')
            verification: include verification for every commit (disable for speedup, default 'true')
            files: include a list of affected files for every commit (disable for speedup, default 'true')

        Returns:
            Commit.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: repoGetSingleCommit
        """
        _query: dict[str, object] = {"stat": stat, "verification": verification, "files": files}

        _response = await self._client._request("GET", f"/repos/{owner}/{repo}/git/commits/{sha}", params=_query)
        return decode(_response, Commit)

    async def download(self, owner: str, repo: str, sha: str, diff_type: Literal["diff", "patch"]) -> str:
        """
        Get a commit's diff or patch.

        Args:
            owner: owner of the repo
            repo: name of the repo
            sha: SHA of the commit to get
            diff_type: whether the output is diff or patch

        Returns:
            APIString is a string response.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoDownloadCommitDiffOrPatch
        """
        _response = await self._client._request("GET", f"/repos/{owner}/{repo}/git/commits/{sha}.{diff_type}")
        return decode(_response, str)


class ReposGitNotes:
    """The ``repos.git.notes`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def get(
        self,
        owner: str,
        repo: str,
        sha: str,
        *,
        verification: bool | None = None,
        files: bool | None = None,
    ) -> Note:
        """
        Get a note corresponding to a single commit from a repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            sha: a git ref or commit sha
            verification: include verification for every commit (disable for speedup, default 'true')
            files: include a list of affected files for every commit (disable for speedup, default 'true')

        Returns:
            Note.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: repoGetNote
        """
        _query: dict[str, object] = {"verification": verification, "files": files}

        _response = self._client._request("GET", f"/repos/{owner}/{repo}/git/notes/{sha}", params=_query)
        return decode(_response, Note)

    def set(self, owner: str, repo: str, sha: str, *, message: str | None = None) -> Note:
        """
        Set a note corresponding to a single commit from a repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            sha: a git ref or commit sha
            message:

        Returns:
            Note.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: repoSetNote
        """
        if message is not None:
            _payload = NoteOptions(message=message).model_dump(mode="json", by_alias=True, exclude_none=True)
        else:
            _payload = None

        _response = self._client._request("POST", f"/repos/{owner}/{repo}/git/notes/{sha}", json=_payload)
        return decode(_response, Note)

    def delete(self, owner: str, repo: str, sha: str) -> None:
        """
        Removes a note corresponding to a single commit from a repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            sha: a git ref or commit sha

        Returns:
            No content.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: repoRemoveNote
        """
        _response = self._client._request("DELETE", f"/repos/{owner}/{repo}/git/notes/{sha}")
        return decode(_response, None)


class AsyncReposGitNotes:
    """The ``repos.git.notes`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def get(
        self,
        owner: str,
        repo: str,
        sha: str,
        *,
        verification: bool | None = None,
        files: bool | None = None,
    ) -> Note:
        """
        Get a note corresponding to a single commit from a repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            sha: a git ref or commit sha
            verification: include verification for every commit (disable for speedup, default 'true')
            files: include a list of affected files for every commit (disable for speedup, default 'true')

        Returns:
            Note.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: repoGetNote
        """
        _query: dict[str, object] = {"verification": verification, "files": files}

        _response = await self._client._request("GET", f"/repos/{owner}/{repo}/git/notes/{sha}", params=_query)
        return decode(_response, Note)

    async def set(self, owner: str, repo: str, sha: str, *, message: str | None = None) -> Note:
        """
        Set a note corresponding to a single commit from a repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            sha: a git ref or commit sha
            message:

        Returns:
            Note.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: repoSetNote
        """
        if message is not None:
            _payload = NoteOptions(message=message).model_dump(mode="json", by_alias=True, exclude_none=True)
        else:
            _payload = None

        _response = await self._client._request("POST", f"/repos/{owner}/{repo}/git/notes/{sha}", json=_payload)
        return decode(_response, Note)

    async def delete(self, owner: str, repo: str, sha: str) -> None:
        """
        Removes a note corresponding to a single commit from a repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            sha: a git ref or commit sha

        Returns:
            No content.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: repoRemoveNote
        """
        _response = await self._client._request("DELETE", f"/repos/{owner}/{repo}/git/notes/{sha}")
        return decode(_response, None)


class ReposGitRefs:
    """The ``repos.git.refs`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def list(self, owner: str, repo: str) -> builtins.list[Reference]:
        """
        Get specified ref or filtered repository's refs.

        Args:
            owner: owner of the repo
            repo: name of the repo

        Returns:
            ReferenceList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoListAllGitRefs
        """
        _response = self._client._request("GET", f"/repos/{owner}/{repo}/git/refs")
        return decode(_response, list[Reference])

    def get(self, owner: str, repo: str, ref: str) -> builtins.list[Reference]:
        """
        Get specified ref or filtered repository's refs.

        Args:
            owner: owner of the repo
            repo: name of the repo
            ref: part or full name of the ref

        Returns:
            ReferenceList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoListGitRefs
        """
        _response = self._client._request("GET", f"/repos/{owner}/{repo}/git/refs/{ref}")
        return decode(_response, list[Reference])


class AsyncReposGitRefs:
    """The ``repos.git.refs`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def list(self, owner: str, repo: str) -> builtins.list[Reference]:
        """
        Get specified ref or filtered repository's refs.

        Args:
            owner: owner of the repo
            repo: name of the repo

        Returns:
            ReferenceList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoListAllGitRefs
        """
        _response = await self._client._request("GET", f"/repos/{owner}/{repo}/git/refs")
        return decode(_response, list[Reference])

    async def get(self, owner: str, repo: str, ref: str) -> builtins.list[Reference]:
        """
        Get specified ref or filtered repository's refs.

        Args:
            owner: owner of the repo
            repo: name of the repo
            ref: part or full name of the ref

        Returns:
            ReferenceList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoListGitRefs
        """
        _response = await self._client._request("GET", f"/repos/{owner}/{repo}/git/refs/{ref}")
        return decode(_response, list[Reference])


class ReposGitTags:
    """The ``repos.git.tags`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def get(self, owner: str, repo: str, sha: str) -> AnnotatedTag:
        """
        Gets the tag object of an annotated tag (not lightweight tags).

        Args:
            owner: owner of the repo
            repo: name of the repo
            sha: sha of the tag. The Git tags API only supports annotated tag objects, not lightweight tags.

        Returns:
            AnnotatedTag.

        Raises:
            BadRequestError: 400. APIError is error format response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: GetAnnotatedTag
        """
        _response = self._client._request("GET", f"/repos/{owner}/{repo}/git/tags/{sha}")
        return decode(_response, AnnotatedTag)


class AsyncReposGitTags:
    """The ``repos.git.tags`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def get(self, owner: str, repo: str, sha: str) -> AnnotatedTag:
        """
        Gets the tag object of an annotated tag (not lightweight tags).

        Args:
            owner: owner of the repo
            repo: name of the repo
            sha: sha of the tag. The Git tags API only supports annotated tag objects, not lightweight tags.

        Returns:
            AnnotatedTag.

        Raises:
            BadRequestError: 400. APIError is error format response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: GetAnnotatedTag
        """
        _response = await self._client._request("GET", f"/repos/{owner}/{repo}/git/tags/{sha}")
        return decode(_response, AnnotatedTag)


class ReposGitTrees:
    """The ``repos.git.trees`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def get(
        self,
        owner: str,
        repo: str,
        sha: str,
        *,
        recursive: bool | None = None,
        page: int | None = None,
        per_page: int | None = None,
    ) -> GitTreeResponse:
        """
        Gets the tree of a repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            sha: sha of the commit
            recursive: show all directories and files
            page: page number; the 'truncated' field in the response will be true if there are still more items after
                this page, false if the last page
            per_page: number of items per page

        Returns:
            GitTreeResponse.

        Raises:
            BadRequestError: 400. APIError is error format response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: GetTree
        """
        _query: dict[str, object] = {"recursive": recursive, "page": page, "per_page": per_page}

        _response = self._client._request("GET", f"/repos/{owner}/{repo}/git/trees/{sha}", params=_query)
        return decode(_response, GitTreeResponse)


class AsyncReposGitTrees:
    """The ``repos.git.trees`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def get(
        self,
        owner: str,
        repo: str,
        sha: str,
        *,
        recursive: bool | None = None,
        page: int | None = None,
        per_page: int | None = None,
    ) -> GitTreeResponse:
        """
        Gets the tree of a repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            sha: sha of the commit
            recursive: show all directories and files
            page: page number; the 'truncated' field in the response will be true if there are still more items after
                this page, false if the last page
            per_page: number of items per page

        Returns:
            GitTreeResponse.

        Raises:
            BadRequestError: 400. APIError is error format response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: GetTree
        """
        _query: dict[str, object] = {"recursive": recursive, "page": page, "per_page": per_page}

        _response = await self._client._request("GET", f"/repos/{owner}/{repo}/git/trees/{sha}", params=_query)
        return decode(_response, GitTreeResponse)


class ReposHooks:
    """The ``repos.hooks`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client
        self.git: ReposHooksGit = ReposHooksGit(client)

    def list(self, owner: str, repo: str, *, page: int | None = None, limit: int | None = None) -> Paginated[Hook]:
        """
        List the hooks in a repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            HookList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoListHooks
        """
        return self._client._paginate("GET", f"/repos/{owner}/{repo}/hooks", model=Hook, page=page, limit=limit)

    def create(
        self,
        owner: str,
        repo: str,
        *,
        active: bool | None = None,
        authorization_header: str | None = None,
        branch_filter: str | None = None,
        config: CreateHookOptionConfig,
        events: builtins.list[str] | None = None,
        type: CreateHookOptionType,
    ) -> Hook:
        """
        Create a hook.

        Args:
            owner: owner of the repo
            repo: name of the repo
            active:
            authorization_header:
            branch_filter:
            config:
            events:
            type:

        Returns:
            Hook.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoCreateHook
        """
        _payload = CreateHookOption(
            active=active,
            authorization_header=authorization_header,
            branch_filter=branch_filter,
            config=config,
            events=events,
            type=type,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = self._client._request("POST", f"/repos/{owner}/{repo}/hooks", json=_payload)
        return decode(_response, Hook)

    def get(self, owner: str, repo: str, id: int) -> Hook:
        """
        Get a hook.

        Args:
            owner: owner of the repo
            repo: name of the repo
            id: id of the hook to get

        Returns:
            Hook.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoGetHook
        """
        _response = self._client._request("GET", f"/repos/{owner}/{repo}/hooks/{id}")
        return decode(_response, Hook)

    def update(
        self,
        owner: str,
        repo: str,
        id: int,
        *,
        active: bool | None = None,
        authorization_header: str | None = None,
        branch_filter: str | None = None,
        config: dict[str, str] | None = None,
        events: builtins.list[str] | None = None,
    ) -> Hook:
        """
        Edit a hook in a repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            id: index of the hook
            active:
            authorization_header:
            branch_filter:
            config:
            events:

        Returns:
            Hook.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoEditHook
        """
        if (
            active is not None
            or authorization_header is not None
            or branch_filter is not None
            or config is not None
            or events is not None
        ):
            _payload = EditHookOption(
                active=active,
                authorization_header=authorization_header,
                branch_filter=branch_filter,
                config=config,
                events=events,
            ).model_dump(mode="json", by_alias=True, exclude_none=True)
        else:
            _payload = None

        _response = self._client._request("PATCH", f"/repos/{owner}/{repo}/hooks/{id}", json=_payload)
        return decode(_response, Hook)

    def delete(self, owner: str, repo: str, id: int) -> None:
        """
        Delete a hook in a repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            id: id of the hook to delete

        Returns:
            No content.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoDeleteHook
        """
        _response = self._client._request("DELETE", f"/repos/{owner}/{repo}/hooks/{id}")
        return decode(_response, None)

    def test(self, owner: str, repo: str, id: int, *, ref: str | None = None) -> None:
        """
        Test a push webhook.

        Args:
            owner: owner of the repo
            repo: name of the repo
            id: id of the hook to test
            ref: The name of the commit/branch/tag, indicates which commit will be loaded to the webhook payload.

        Returns:
            No content.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoTestHook
        """
        _query: dict[str, object] = {"ref": ref}

        _response = self._client._request("POST", f"/repos/{owner}/{repo}/hooks/{id}/tests", params=_query)
        return decode(_response, None)


class AsyncReposHooks:
    """The ``repos.hooks`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client
        self.git: AsyncReposHooksGit = AsyncReposHooksGit(client)

    async def list(
        self,
        owner: str,
        repo: str,
        *,
        page: int | None = None,
        limit: int | None = None,
    ) -> AsyncPaginated[Hook]:
        """
        List the hooks in a repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            HookList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoListHooks
        """
        return await self._client._paginate("GET", f"/repos/{owner}/{repo}/hooks", model=Hook, page=page, limit=limit)

    async def create(
        self,
        owner: str,
        repo: str,
        *,
        active: bool | None = None,
        authorization_header: str | None = None,
        branch_filter: str | None = None,
        config: CreateHookOptionConfig,
        events: builtins.list[str] | None = None,
        type: CreateHookOptionType,
    ) -> Hook:
        """
        Create a hook.

        Args:
            owner: owner of the repo
            repo: name of the repo
            active:
            authorization_header:
            branch_filter:
            config:
            events:
            type:

        Returns:
            Hook.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoCreateHook
        """
        _payload = CreateHookOption(
            active=active,
            authorization_header=authorization_header,
            branch_filter=branch_filter,
            config=config,
            events=events,
            type=type,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = await self._client._request("POST", f"/repos/{owner}/{repo}/hooks", json=_payload)
        return decode(_response, Hook)

    async def get(self, owner: str, repo: str, id: int) -> Hook:
        """
        Get a hook.

        Args:
            owner: owner of the repo
            repo: name of the repo
            id: id of the hook to get

        Returns:
            Hook.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoGetHook
        """
        _response = await self._client._request("GET", f"/repos/{owner}/{repo}/hooks/{id}")
        return decode(_response, Hook)

    async def update(
        self,
        owner: str,
        repo: str,
        id: int,
        *,
        active: bool | None = None,
        authorization_header: str | None = None,
        branch_filter: str | None = None,
        config: dict[str, str] | None = None,
        events: builtins.list[str] | None = None,
    ) -> Hook:
        """
        Edit a hook in a repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            id: index of the hook
            active:
            authorization_header:
            branch_filter:
            config:
            events:

        Returns:
            Hook.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoEditHook
        """
        if (
            active is not None
            or authorization_header is not None
            or branch_filter is not None
            or config is not None
            or events is not None
        ):
            _payload = EditHookOption(
                active=active,
                authorization_header=authorization_header,
                branch_filter=branch_filter,
                config=config,
                events=events,
            ).model_dump(mode="json", by_alias=True, exclude_none=True)
        else:
            _payload = None

        _response = await self._client._request("PATCH", f"/repos/{owner}/{repo}/hooks/{id}", json=_payload)
        return decode(_response, Hook)

    async def delete(self, owner: str, repo: str, id: int) -> None:
        """
        Delete a hook in a repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            id: id of the hook to delete

        Returns:
            No content.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoDeleteHook
        """
        _response = await self._client._request("DELETE", f"/repos/{owner}/{repo}/hooks/{id}")
        return decode(_response, None)

    async def test(self, owner: str, repo: str, id: int, *, ref: str | None = None) -> None:
        """
        Test a push webhook.

        Args:
            owner: owner of the repo
            repo: name of the repo
            id: id of the hook to test
            ref: The name of the commit/branch/tag, indicates which commit will be loaded to the webhook payload.

        Returns:
            No content.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoTestHook
        """
        _query: dict[str, object] = {"ref": ref}

        _response = await self._client._request("POST", f"/repos/{owner}/{repo}/hooks/{id}/tests", params=_query)
        return decode(_response, None)


class ReposHooksGit:
    """The ``repos.hooks.git`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def list(self, owner: str, repo: str) -> builtins.list[GitHook]:
        """
        List the Git hooks in a repository.

        Args:
            owner: owner of the repo
            repo: name of the repo

        Returns:
            GitHookList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoListGitHooks
        """
        _response = self._client._request("GET", f"/repos/{owner}/{repo}/hooks/git")
        return decode(_response, list[GitHook])

    def get(self, owner: str, repo: str, id: str) -> GitHook:
        """
        Get a Git hook.

        Args:
            owner: owner of the repo
            repo: name of the repo
            id: id of the hook to get

        Returns:
            GitHook.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoGetGitHook
        """
        _response = self._client._request("GET", f"/repos/{owner}/{repo}/hooks/git/{id}")
        return decode(_response, GitHook)

    def update(self, owner: str, repo: str, id: str, *, content: str | None = None) -> GitHook:
        """
        Edit a Git hook in a repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            id: id of the hook to get
            content:

        Returns:
            GitHook.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoEditGitHook
        """
        if content is not None:
            _payload = EditGitHookOption(content=content).model_dump(mode="json", by_alias=True, exclude_none=True)
        else:
            _payload = None

        _response = self._client._request("PATCH", f"/repos/{owner}/{repo}/hooks/git/{id}", json=_payload)
        return decode(_response, GitHook)

    def delete(self, owner: str, repo: str, id: str) -> None:
        """
        Delete a Git hook in a repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            id: id of the hook to get

        Returns:
            No content.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoDeleteGitHook
        """
        _response = self._client._request("DELETE", f"/repos/{owner}/{repo}/hooks/git/{id}")
        return decode(_response, None)


class AsyncReposHooksGit:
    """The ``repos.hooks.git`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def list(self, owner: str, repo: str) -> builtins.list[GitHook]:
        """
        List the Git hooks in a repository.

        Args:
            owner: owner of the repo
            repo: name of the repo

        Returns:
            GitHookList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoListGitHooks
        """
        _response = await self._client._request("GET", f"/repos/{owner}/{repo}/hooks/git")
        return decode(_response, list[GitHook])

    async def get(self, owner: str, repo: str, id: str) -> GitHook:
        """
        Get a Git hook.

        Args:
            owner: owner of the repo
            repo: name of the repo
            id: id of the hook to get

        Returns:
            GitHook.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoGetGitHook
        """
        _response = await self._client._request("GET", f"/repos/{owner}/{repo}/hooks/git/{id}")
        return decode(_response, GitHook)

    async def update(self, owner: str, repo: str, id: str, *, content: str | None = None) -> GitHook:
        """
        Edit a Git hook in a repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            id: id of the hook to get
            content:

        Returns:
            GitHook.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoEditGitHook
        """
        if content is not None:
            _payload = EditGitHookOption(content=content).model_dump(mode="json", by_alias=True, exclude_none=True)
        else:
            _payload = None

        _response = await self._client._request("PATCH", f"/repos/{owner}/{repo}/hooks/git/{id}", json=_payload)
        return decode(_response, GitHook)

    async def delete(self, owner: str, repo: str, id: str) -> None:
        """
        Delete a Git hook in a repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            id: id of the hook to get

        Returns:
            No content.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoDeleteGitHook
        """
        _response = await self._client._request("DELETE", f"/repos/{owner}/{repo}/hooks/git/{id}")
        return decode(_response, None)


class ReposIssueConfig:
    """The ``repos.issue_config`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def get(self, owner: str, repo: str) -> IssueConfig:
        """
        Returns the issue config for a repo.

        Args:
            owner: owner of the repo
            repo: name of the repo

        Returns:
            RepoIssueConfig.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoGetIssueConfig
        """
        _response = self._client._request("GET", f"/repos/{owner}/{repo}/issue_config")
        return decode(_response, IssueConfig)

    def validate(self, owner: str, repo: str) -> IssueConfigValidation:
        """
        Returns the validation information for a issue config.

        Args:
            owner: owner of the repo
            repo: name of the repo

        Returns:
            RepoIssueConfigValidation.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoValidateIssueConfig
        """
        _response = self._client._request("GET", f"/repos/{owner}/{repo}/issue_config/validate")
        return decode(_response, IssueConfigValidation)


class AsyncReposIssueConfig:
    """The ``repos.issue_config`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def get(self, owner: str, repo: str) -> IssueConfig:
        """
        Returns the issue config for a repo.

        Args:
            owner: owner of the repo
            repo: name of the repo

        Returns:
            RepoIssueConfig.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoGetIssueConfig
        """
        _response = await self._client._request("GET", f"/repos/{owner}/{repo}/issue_config")
        return decode(_response, IssueConfig)

    async def validate(self, owner: str, repo: str) -> IssueConfigValidation:
        """
        Returns the validation information for a issue config.

        Args:
            owner: owner of the repo
            repo: name of the repo

        Returns:
            RepoIssueConfigValidation.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoValidateIssueConfig
        """
        _response = await self._client._request("GET", f"/repos/{owner}/{repo}/issue_config/validate")
        return decode(_response, IssueConfigValidation)


class ReposIssues:
    """The ``repos.issues`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client
        self.assets: ReposIssuesAssets = ReposIssuesAssets(client)
        self.blocks: ReposIssuesBlocks = ReposIssuesBlocks(client)
        self.comments: ReposIssuesComments = ReposIssuesComments(client)
        self.dependencies: ReposIssuesDependencies = ReposIssuesDependencies(client)
        self.labels: ReposIssuesLabels = ReposIssuesLabels(client)
        self.reactions: ReposIssuesReactions = ReposIssuesReactions(client)
        self.stopwatch: ReposIssuesStopwatch = ReposIssuesStopwatch(client)
        self.subscriptions: ReposIssuesSubscriptions = ReposIssuesSubscriptions(client)
        self.times: ReposIssuesTimes = ReposIssuesTimes(client)

    def search(
        self,
        *,
        state: Literal["open", "closed", "all"] | None = None,
        labels: str | None = None,
        milestones: str | None = None,
        q: str | None = None,
        priority_repo_id: int | None = None,
        type: Literal["issues", "pulls"] | None = None,
        since: datetime | None = None,
        before: datetime | None = None,
        assigned: bool | None = None,
        created: bool | None = None,
        mentioned: bool | None = None,
        review_requested: bool | None = None,
        reviewed: bool | None = None,
        owner: str | None = None,
        team: str | None = None,
        sort: Literal[
            "relevance",
            "latest",
            "oldest",
            "recentupdate",
            "leastupdate",
            "mostcomment",
            "leastcomment",
            "nearduedate",
            "farduedate",
        ]
        | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> Paginated[Issue]:
        """
        Search for issues across the repositories that the user has access to.

        Args:
            state: State of the issue
            labels: Comma-separated list of label names. Fetch only issues that have any of these labels. Non existent
                labels are discarded.
            milestones: Comma-separated list of milestone names. Fetch only issues that have any of these milestones.
                Non existent milestones are discarded.
            q: Search string
            priority_repo_id: Repository ID to prioritize in the results
            type: Filter by issue type
            since: Only show issues updated after the given time (RFC 3339 format)
            before: Only show issues updated before the given time (RFC 3339 format)
            assigned: Filter issues or pulls assigned to the authenticated user
            created: Filter issues or pulls created by the authenticated user
            mentioned: Filter issues or pulls mentioning the authenticated user
            review_requested: Filter pull requests where the authenticated user's review was requested
            reviewed: Filter pull requests reviewed by the authenticated user
            owner: Filter by repository owner
            team: Filter by team (requires organization owner parameter)
            sort: Type of sort
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            IssueList.

        Raises:
            BadRequestError: 400. APIError is error format response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: issueSearchIssues
        """
        _query: dict[str, object] = {
            "state": state,
            "labels": labels,
            "milestones": milestones,
            "q": q,
            "priority_repo_id": priority_repo_id,
            "type": type,
            "since": None if since is None else since.isoformat(),
            "before": None if before is None else before.isoformat(),
            "assigned": assigned,
            "created": created,
            "mentioned": mentioned,
            "review_requested": review_requested,
            "reviewed": reviewed,
            "owner": owner,
            "team": team,
            "sort": sort,
        }

        return self._client._paginate("GET", "/repos/issues/search", model=Issue, params=_query, page=page, limit=limit)

    def list(
        self,
        owner: str,
        repo: str,
        *,
        state: Literal["closed", "open", "all"] | None = None,
        labels: str | None = None,
        q: str | None = None,
        type: Literal["issues", "pulls"] | None = None,
        milestones: str | None = None,
        since: datetime | None = None,
        before: datetime | None = None,
        created_by: str | None = None,
        assigned_by: str | None = None,
        mentioned_by: str | None = None,
        sort: Literal[
            "relevance",
            "latest",
            "oldest",
            "recentupdate",
            "leastupdate",
            "mostcomment",
            "leastcomment",
            "nearduedate",
            "farduedate",
        ]
        | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> Paginated[Issue]:
        """
        List a repository's issues.

        Args:
            owner: owner of the repo
            repo: name of the repo
            state: whether issue is open or closed
            labels: comma separated list of labels. Fetch only issues that have any of this labels. Non existent labels
                are discarded
            q: search string
            type: filter by type (issues / pulls) if set
            milestones: comma separated list of milestone names or ids. It uses names and fall back to ids. Fetch only
                issues that have any of this milestones. Non existent milestones are discarded
            since: Only show items updated after the given time. This is a timestamp in RFC 3339 format
            before: Only show items updated before the given time. This is a timestamp in RFC 3339 format
            created_by: Only show items which were created by the given user
            assigned_by: Only show items for which the given user is assigned
            mentioned_by: Only show items in which the given user was mentioned
            sort: Type of sort
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            IssueList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: issueListIssues
        """
        _query: dict[str, object] = {
            "state": state,
            "labels": labels,
            "q": q,
            "type": type,
            "milestones": milestones,
            "since": None if since is None else since.isoformat(),
            "before": None if before is None else before.isoformat(),
            "created_by": created_by,
            "assigned_by": assigned_by,
            "mentioned_by": mentioned_by,
            "sort": sort,
        }

        return self._client._paginate(
            "GET", f"/repos/{owner}/{repo}/issues", model=Issue, params=_query, page=page, limit=limit
        )

    def create(
        self,
        owner: str,
        repo: str,
        *,
        assignee: str | None = None,
        assignees: builtins.list[str] | None = None,
        body: str | None = None,
        closed: bool | None = None,
        due_date: datetime | None = None,
        labels: builtins.list[int] | None = None,
        milestone: int | None = None,
        ref: str | None = None,
        title: str,
    ) -> Issue:
        """
        Create an issue. If using deadline only the date will be taken into account, and time of day ignored.

        Args:
            owner: owner of the repo
            repo: name of the repo
            assignee: deprecated
            assignees:
            body:
            closed:
            due_date:
            labels: list of label ids
            milestone: milestone id
            ref:
            title:

        Returns:
            Issue.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.
            PreconditionFailedError: 412. APIError is error format response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.
            LockedError: 423. APIRepoArchivedError is an error that is raised when an archived repo should be modified.

        Operation ID: issueCreateIssue
        """
        _payload = CreateIssueOption(
            assignee=assignee,
            assignees=assignees,
            body=body,
            closed=closed,
            due_date=due_date,
            labels=labels,
            milestone=milestone,
            ref=ref,
            title=title,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = self._client._request("POST", f"/repos/{owner}/{repo}/issues", json=_payload)
        return decode(_response, Issue)

    def pinned(self, owner: str, repo: str) -> builtins.list[Issue]:
        """
        List a repo's pinned issues.

        Args:
            owner: owner of the repo
            repo: name of the repo

        Returns:
            IssueListWithoutPagination - Issues without pagination headers (used for pinned issues, dependencies, etc.).

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoListPinnedIssues
        """
        _response = self._client._request("GET", f"/repos/{owner}/{repo}/issues/pinned")
        return decode(_response, list[Issue])

    def get(self, owner: str, repo: str, index: int) -> Issue:
        """
        Get an issue.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the issue to get

        Returns:
            Issue.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: issueGetIssue
        """
        _response = self._client._request("GET", f"/repos/{owner}/{repo}/issues/{index}")
        return decode(_response, Issue)

    def update(
        self,
        owner: str,
        repo: str,
        index: int,
        *,
        assignee: str | None = None,
        assignees: builtins.list[str] | None = None,
        body: str | None = None,
        due_date: datetime | None = None,
        milestone: int | None = None,
        ref: str | None = None,
        state: str | None = None,
        title: str | None = None,
        unset_due_date: bool | None = None,
        updated_at: datetime | None = None,
    ) -> Issue:
        """
        Edit an issue. If using deadline only the date will be taken into account, and time of day ignored.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the issue to edit
            assignee: deprecated
            assignees:
            body:
            due_date:
            milestone:
            ref:
            state:
            title:
            unset_due_date:
            updated_at:

        Returns:
            Issue.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.
            PreconditionFailedError: 412. APIError is error format response.

        Operation ID: issueEditIssue
        """
        if (
            assignee is not None
            or assignees is not None
            or body is not None
            or due_date is not None
            or milestone is not None
            or ref is not None
            or state is not None
            or title is not None
            or unset_due_date is not None
            or updated_at is not None
        ):
            _payload = EditIssueOption(
                assignee=assignee,
                assignees=assignees,
                body=body,
                due_date=due_date,
                milestone=milestone,
                ref=ref,
                state=state,
                title=title,
                unset_due_date=unset_due_date,
                updated_at=updated_at,
            ).model_dump(mode="json", by_alias=True, exclude_none=True)
        else:
            _payload = None

        _response = self._client._request("PATCH", f"/repos/{owner}/{repo}/issues/{index}", json=_payload)
        return decode(_response, Issue)

    def delete(self, owner: str, repo: str, index: int) -> None:
        """
        Delete an issue.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of issue to delete

        Returns:
            No content.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: issueDelete
        """
        _response = self._client._request("DELETE", f"/repos/{owner}/{repo}/issues/{index}")
        return decode(_response, None)

    def deadline(self, owner: str, repo: str, index: int, *, due_date: datetime) -> IssueDeadline:
        """
        Set an issue deadline. If set to null, the deadline is deleted. If using deadline only the date will be taken
        into account, and time of day ignored.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the issue to create or update a deadline on
            due_date:

        Returns:
            IssueDeadline.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: issueEditIssueDeadline
        """
        _payload = EditDeadlineOption(
            due_date=due_date,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = self._client._request("POST", f"/repos/{owner}/{repo}/issues/{index}/deadline", json=_payload)
        return decode(_response, IssueDeadline)

    def pin(self, owner: str, repo: str, index: int) -> None:
        """
        Pin an Issue.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of issue to pin

        Returns:
            No content.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: pinIssue
        """
        _response = self._client._request("POST", f"/repos/{owner}/{repo}/issues/{index}/pin")
        return decode(_response, None)

    def unpin(self, owner: str, repo: str, index: int) -> None:
        """
        Unpin an Issue.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of issue to unpin

        Returns:
            No content.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: unpinIssue
        """
        _response = self._client._request("DELETE", f"/repos/{owner}/{repo}/issues/{index}/pin")
        return decode(_response, None)

    def move(self, owner: str, repo: str, index: int, position: int) -> None:
        """
        Moves the Pin to the given Position.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of issue
            position: the new position

        Returns:
            No content.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: moveIssuePin
        """
        _response = self._client._request("PATCH", f"/repos/{owner}/{repo}/issues/{index}/pin/{position}")
        return decode(_response, None)

    def timeline(
        self,
        owner: str,
        repo: str,
        index: int,
        *,
        since: datetime | None = None,
        before: datetime | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> Paginated[TimelineComment]:
        """
        List all comments and events on an issue.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the issue
            since: if provided, only comments updated since the specified time are returned.
            before: if provided, only comments updated before the provided time are returned.
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            TimelineList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.
            ServerError: 500. APIInternalServerError is an error that is raised when an internal server error occurs.

        Operation ID: issueGetCommentsAndTimeline
        """
        _query: dict[str, object] = {
            "since": None if since is None else since.isoformat(),
            "before": None if before is None else before.isoformat(),
        }

        return self._client._paginate(
            "GET",
            f"/repos/{owner}/{repo}/issues/{index}/timeline",
            model=TimelineComment,
            params=_query,
            page=page,
            limit=limit,
        )


class AsyncReposIssues:
    """The ``repos.issues`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client
        self.assets: AsyncReposIssuesAssets = AsyncReposIssuesAssets(client)
        self.blocks: AsyncReposIssuesBlocks = AsyncReposIssuesBlocks(client)
        self.comments: AsyncReposIssuesComments = AsyncReposIssuesComments(client)
        self.dependencies: AsyncReposIssuesDependencies = AsyncReposIssuesDependencies(client)
        self.labels: AsyncReposIssuesLabels = AsyncReposIssuesLabels(client)
        self.reactions: AsyncReposIssuesReactions = AsyncReposIssuesReactions(client)
        self.stopwatch: AsyncReposIssuesStopwatch = AsyncReposIssuesStopwatch(client)
        self.subscriptions: AsyncReposIssuesSubscriptions = AsyncReposIssuesSubscriptions(client)
        self.times: AsyncReposIssuesTimes = AsyncReposIssuesTimes(client)

    async def search(
        self,
        *,
        state: Literal["open", "closed", "all"] | None = None,
        labels: str | None = None,
        milestones: str | None = None,
        q: str | None = None,
        priority_repo_id: int | None = None,
        type: Literal["issues", "pulls"] | None = None,
        since: datetime | None = None,
        before: datetime | None = None,
        assigned: bool | None = None,
        created: bool | None = None,
        mentioned: bool | None = None,
        review_requested: bool | None = None,
        reviewed: bool | None = None,
        owner: str | None = None,
        team: str | None = None,
        sort: Literal[
            "relevance",
            "latest",
            "oldest",
            "recentupdate",
            "leastupdate",
            "mostcomment",
            "leastcomment",
            "nearduedate",
            "farduedate",
        ]
        | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> AsyncPaginated[Issue]:
        """
        Search for issues across the repositories that the user has access to.

        Args:
            state: State of the issue
            labels: Comma-separated list of label names. Fetch only issues that have any of these labels. Non existent
                labels are discarded.
            milestones: Comma-separated list of milestone names. Fetch only issues that have any of these milestones.
                Non existent milestones are discarded.
            q: Search string
            priority_repo_id: Repository ID to prioritize in the results
            type: Filter by issue type
            since: Only show issues updated after the given time (RFC 3339 format)
            before: Only show issues updated before the given time (RFC 3339 format)
            assigned: Filter issues or pulls assigned to the authenticated user
            created: Filter issues or pulls created by the authenticated user
            mentioned: Filter issues or pulls mentioning the authenticated user
            review_requested: Filter pull requests where the authenticated user's review was requested
            reviewed: Filter pull requests reviewed by the authenticated user
            owner: Filter by repository owner
            team: Filter by team (requires organization owner parameter)
            sort: Type of sort
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            IssueList.

        Raises:
            BadRequestError: 400. APIError is error format response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: issueSearchIssues
        """
        _query: dict[str, object] = {
            "state": state,
            "labels": labels,
            "milestones": milestones,
            "q": q,
            "priority_repo_id": priority_repo_id,
            "type": type,
            "since": None if since is None else since.isoformat(),
            "before": None if before is None else before.isoformat(),
            "assigned": assigned,
            "created": created,
            "mentioned": mentioned,
            "review_requested": review_requested,
            "reviewed": reviewed,
            "owner": owner,
            "team": team,
            "sort": sort,
        }

        return await self._client._paginate(
            "GET", "/repos/issues/search", model=Issue, params=_query, page=page, limit=limit
        )

    async def list(
        self,
        owner: str,
        repo: str,
        *,
        state: Literal["closed", "open", "all"] | None = None,
        labels: str | None = None,
        q: str | None = None,
        type: Literal["issues", "pulls"] | None = None,
        milestones: str | None = None,
        since: datetime | None = None,
        before: datetime | None = None,
        created_by: str | None = None,
        assigned_by: str | None = None,
        mentioned_by: str | None = None,
        sort: Literal[
            "relevance",
            "latest",
            "oldest",
            "recentupdate",
            "leastupdate",
            "mostcomment",
            "leastcomment",
            "nearduedate",
            "farduedate",
        ]
        | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> AsyncPaginated[Issue]:
        """
        List a repository's issues.

        Args:
            owner: owner of the repo
            repo: name of the repo
            state: whether issue is open or closed
            labels: comma separated list of labels. Fetch only issues that have any of this labels. Non existent labels
                are discarded
            q: search string
            type: filter by type (issues / pulls) if set
            milestones: comma separated list of milestone names or ids. It uses names and fall back to ids. Fetch only
                issues that have any of this milestones. Non existent milestones are discarded
            since: Only show items updated after the given time. This is a timestamp in RFC 3339 format
            before: Only show items updated before the given time. This is a timestamp in RFC 3339 format
            created_by: Only show items which were created by the given user
            assigned_by: Only show items for which the given user is assigned
            mentioned_by: Only show items in which the given user was mentioned
            sort: Type of sort
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            IssueList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: issueListIssues
        """
        _query: dict[str, object] = {
            "state": state,
            "labels": labels,
            "q": q,
            "type": type,
            "milestones": milestones,
            "since": None if since is None else since.isoformat(),
            "before": None if before is None else before.isoformat(),
            "created_by": created_by,
            "assigned_by": assigned_by,
            "mentioned_by": mentioned_by,
            "sort": sort,
        }

        return await self._client._paginate(
            "GET", f"/repos/{owner}/{repo}/issues", model=Issue, params=_query, page=page, limit=limit
        )

    async def create(
        self,
        owner: str,
        repo: str,
        *,
        assignee: str | None = None,
        assignees: builtins.list[str] | None = None,
        body: str | None = None,
        closed: bool | None = None,
        due_date: datetime | None = None,
        labels: builtins.list[int] | None = None,
        milestone: int | None = None,
        ref: str | None = None,
        title: str,
    ) -> Issue:
        """
        Create an issue. If using deadline only the date will be taken into account, and time of day ignored.

        Args:
            owner: owner of the repo
            repo: name of the repo
            assignee: deprecated
            assignees:
            body:
            closed:
            due_date:
            labels: list of label ids
            milestone: milestone id
            ref:
            title:

        Returns:
            Issue.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.
            PreconditionFailedError: 412. APIError is error format response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.
            LockedError: 423. APIRepoArchivedError is an error that is raised when an archived repo should be modified.

        Operation ID: issueCreateIssue
        """
        _payload = CreateIssueOption(
            assignee=assignee,
            assignees=assignees,
            body=body,
            closed=closed,
            due_date=due_date,
            labels=labels,
            milestone=milestone,
            ref=ref,
            title=title,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = await self._client._request("POST", f"/repos/{owner}/{repo}/issues", json=_payload)
        return decode(_response, Issue)

    async def pinned(self, owner: str, repo: str) -> builtins.list[Issue]:
        """
        List a repo's pinned issues.

        Args:
            owner: owner of the repo
            repo: name of the repo

        Returns:
            IssueListWithoutPagination - Issues without pagination headers (used for pinned issues, dependencies, etc.).

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoListPinnedIssues
        """
        _response = await self._client._request("GET", f"/repos/{owner}/{repo}/issues/pinned")
        return decode(_response, list[Issue])

    async def get(self, owner: str, repo: str, index: int) -> Issue:
        """
        Get an issue.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the issue to get

        Returns:
            Issue.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: issueGetIssue
        """
        _response = await self._client._request("GET", f"/repos/{owner}/{repo}/issues/{index}")
        return decode(_response, Issue)

    async def update(
        self,
        owner: str,
        repo: str,
        index: int,
        *,
        assignee: str | None = None,
        assignees: builtins.list[str] | None = None,
        body: str | None = None,
        due_date: datetime | None = None,
        milestone: int | None = None,
        ref: str | None = None,
        state: str | None = None,
        title: str | None = None,
        unset_due_date: bool | None = None,
        updated_at: datetime | None = None,
    ) -> Issue:
        """
        Edit an issue. If using deadline only the date will be taken into account, and time of day ignored.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the issue to edit
            assignee: deprecated
            assignees:
            body:
            due_date:
            milestone:
            ref:
            state:
            title:
            unset_due_date:
            updated_at:

        Returns:
            Issue.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.
            PreconditionFailedError: 412. APIError is error format response.

        Operation ID: issueEditIssue
        """
        if (
            assignee is not None
            or assignees is not None
            or body is not None
            or due_date is not None
            or milestone is not None
            or ref is not None
            or state is not None
            or title is not None
            or unset_due_date is not None
            or updated_at is not None
        ):
            _payload = EditIssueOption(
                assignee=assignee,
                assignees=assignees,
                body=body,
                due_date=due_date,
                milestone=milestone,
                ref=ref,
                state=state,
                title=title,
                unset_due_date=unset_due_date,
                updated_at=updated_at,
            ).model_dump(mode="json", by_alias=True, exclude_none=True)
        else:
            _payload = None

        _response = await self._client._request("PATCH", f"/repos/{owner}/{repo}/issues/{index}", json=_payload)
        return decode(_response, Issue)

    async def delete(self, owner: str, repo: str, index: int) -> None:
        """
        Delete an issue.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of issue to delete

        Returns:
            No content.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: issueDelete
        """
        _response = await self._client._request("DELETE", f"/repos/{owner}/{repo}/issues/{index}")
        return decode(_response, None)

    async def deadline(self, owner: str, repo: str, index: int, *, due_date: datetime) -> IssueDeadline:
        """
        Set an issue deadline. If set to null, the deadline is deleted. If using deadline only the date will be taken
        into account, and time of day ignored.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the issue to create or update a deadline on
            due_date:

        Returns:
            IssueDeadline.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: issueEditIssueDeadline
        """
        _payload = EditDeadlineOption(
            due_date=due_date,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = await self._client._request("POST", f"/repos/{owner}/{repo}/issues/{index}/deadline", json=_payload)
        return decode(_response, IssueDeadline)

    async def pin(self, owner: str, repo: str, index: int) -> None:
        """
        Pin an Issue.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of issue to pin

        Returns:
            No content.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: pinIssue
        """
        _response = await self._client._request("POST", f"/repos/{owner}/{repo}/issues/{index}/pin")
        return decode(_response, None)

    async def unpin(self, owner: str, repo: str, index: int) -> None:
        """
        Unpin an Issue.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of issue to unpin

        Returns:
            No content.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: unpinIssue
        """
        _response = await self._client._request("DELETE", f"/repos/{owner}/{repo}/issues/{index}/pin")
        return decode(_response, None)

    async def move(self, owner: str, repo: str, index: int, position: int) -> None:
        """
        Moves the Pin to the given Position.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of issue
            position: the new position

        Returns:
            No content.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: moveIssuePin
        """
        _response = await self._client._request("PATCH", f"/repos/{owner}/{repo}/issues/{index}/pin/{position}")
        return decode(_response, None)

    async def timeline(
        self,
        owner: str,
        repo: str,
        index: int,
        *,
        since: datetime | None = None,
        before: datetime | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> AsyncPaginated[TimelineComment]:
        """
        List all comments and events on an issue.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the issue
            since: if provided, only comments updated since the specified time are returned.
            before: if provided, only comments updated before the provided time are returned.
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            TimelineList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.
            ServerError: 500. APIInternalServerError is an error that is raised when an internal server error occurs.

        Operation ID: issueGetCommentsAndTimeline
        """
        _query: dict[str, object] = {
            "since": None if since is None else since.isoformat(),
            "before": None if before is None else before.isoformat(),
        }

        return await self._client._paginate(
            "GET",
            f"/repos/{owner}/{repo}/issues/{index}/timeline",
            model=TimelineComment,
            params=_query,
            page=page,
            limit=limit,
        )


class ReposIssuesAssets:
    """The ``repos.issues.assets`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def list(self, owner: str, repo: str, index: int) -> builtins.list[Attachment]:
        """
        List issue's attachments.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the issue

        Returns:
            AttachmentList.

        Raises:
            NotFoundError: 404. APIError is error format response.

        Operation ID: issueListIssueAttachments
        """
        _response = self._client._request("GET", f"/repos/{owner}/{repo}/issues/{index}/assets")
        return decode(_response, list[Attachment])

    def create(
        self,
        owner: str,
        repo: str,
        index: int,
        *,
        name: str | None = None,
        updated_at: datetime | None = None,
        attachment: FilePart,
    ) -> Attachment:
        """
        Create an issue attachment.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the issue
            name: name of the attachment
            updated_at: time of the attachment's creation. This is a timestamp in RFC 3339 format
            attachment: attachment to upload

        Returns:
            Attachment.

        Raises:
            BadRequestError: 400. APIError is error format response.
            NotFoundError: 404. APIError is error format response.
            PayloadTooLargeError: 413. QuotaExceeded.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.
            LockedError: 423. APIRepoArchivedError is an error that is raised when an archived repo should be modified.

        Operation ID: issueCreateIssueAttachment
        """
        _query: dict[str, object] = {"name": name, "updated_at": None if updated_at is None else updated_at.isoformat()}

        _files: dict[str, object] = {}
        _files["attachment"] = attachment

        _response = self._client._request(
            "POST", f"/repos/{owner}/{repo}/issues/{index}/assets", params=_query, files=_files
        )
        return decode(_response, Attachment)

    def get(self, owner: str, repo: str, index: int, attachment_id: int) -> Attachment:
        """
        Get an issue attachment.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the issue
            attachment_id: id of the attachment to get

        Returns:
            Attachment.

        Raises:
            NotFoundError: 404. APIError is error format response.

        Operation ID: issueGetIssueAttachment
        """
        _response = self._client._request("GET", f"/repos/{owner}/{repo}/issues/{index}/assets/{attachment_id}")
        return decode(_response, Attachment)

    def update(
        self,
        owner: str,
        repo: str,
        index: int,
        attachment_id: int,
        *,
        browser_download_url: str | None = None,
        name: str | None = None,
    ) -> Attachment:
        """
        Edit an issue attachment.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the issue
            attachment_id: id of the attachment to edit
            browser_download_url: (Can only be set if existing attachment is of external type)
            name:

        Returns:
            Attachment.

        Raises:
            NotFoundError: 404. APIError is error format response.
            PayloadTooLargeError: 413. QuotaExceeded.
            LockedError: 423. APIRepoArchivedError is an error that is raised when an archived repo should be modified.

        Operation ID: issueEditIssueAttachment
        """
        if browser_download_url is not None or name is not None:
            _payload = EditAttachmentOptions(browser_download_url=browser_download_url, name=name).model_dump(
                mode="json", by_alias=True, exclude_none=True
            )
        else:
            _payload = None

        _response = self._client._request(
            "PATCH", f"/repos/{owner}/{repo}/issues/{index}/assets/{attachment_id}", json=_payload
        )
        return decode(_response, Attachment)

    def delete(self, owner: str, repo: str, index: int, attachment_id: int) -> None:
        """
        Delete an issue attachment.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the issue
            attachment_id: id of the attachment to delete

        Returns:
            No content.

        Raises:
            NotFoundError: 404. APIError is error format response.
            LockedError: 423. APIRepoArchivedError is an error that is raised when an archived repo should be modified.

        Operation ID: issueDeleteIssueAttachment
        """
        _response = self._client._request("DELETE", f"/repos/{owner}/{repo}/issues/{index}/assets/{attachment_id}")
        return decode(_response, None)


class AsyncReposIssuesAssets:
    """The ``repos.issues.assets`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def list(self, owner: str, repo: str, index: int) -> builtins.list[Attachment]:
        """
        List issue's attachments.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the issue

        Returns:
            AttachmentList.

        Raises:
            NotFoundError: 404. APIError is error format response.

        Operation ID: issueListIssueAttachments
        """
        _response = await self._client._request("GET", f"/repos/{owner}/{repo}/issues/{index}/assets")
        return decode(_response, list[Attachment])

    async def create(
        self,
        owner: str,
        repo: str,
        index: int,
        *,
        name: str | None = None,
        updated_at: datetime | None = None,
        attachment: FilePart,
    ) -> Attachment:
        """
        Create an issue attachment.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the issue
            name: name of the attachment
            updated_at: time of the attachment's creation. This is a timestamp in RFC 3339 format
            attachment: attachment to upload

        Returns:
            Attachment.

        Raises:
            BadRequestError: 400. APIError is error format response.
            NotFoundError: 404. APIError is error format response.
            PayloadTooLargeError: 413. QuotaExceeded.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.
            LockedError: 423. APIRepoArchivedError is an error that is raised when an archived repo should be modified.

        Operation ID: issueCreateIssueAttachment
        """
        _query: dict[str, object] = {"name": name, "updated_at": None if updated_at is None else updated_at.isoformat()}

        _files: dict[str, object] = {}
        _files["attachment"] = attachment

        _response = await self._client._request(
            "POST", f"/repos/{owner}/{repo}/issues/{index}/assets", params=_query, files=_files
        )
        return decode(_response, Attachment)

    async def get(self, owner: str, repo: str, index: int, attachment_id: int) -> Attachment:
        """
        Get an issue attachment.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the issue
            attachment_id: id of the attachment to get

        Returns:
            Attachment.

        Raises:
            NotFoundError: 404. APIError is error format response.

        Operation ID: issueGetIssueAttachment
        """
        _response = await self._client._request("GET", f"/repos/{owner}/{repo}/issues/{index}/assets/{attachment_id}")
        return decode(_response, Attachment)

    async def update(
        self,
        owner: str,
        repo: str,
        index: int,
        attachment_id: int,
        *,
        browser_download_url: str | None = None,
        name: str | None = None,
    ) -> Attachment:
        """
        Edit an issue attachment.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the issue
            attachment_id: id of the attachment to edit
            browser_download_url: (Can only be set if existing attachment is of external type)
            name:

        Returns:
            Attachment.

        Raises:
            NotFoundError: 404. APIError is error format response.
            PayloadTooLargeError: 413. QuotaExceeded.
            LockedError: 423. APIRepoArchivedError is an error that is raised when an archived repo should be modified.

        Operation ID: issueEditIssueAttachment
        """
        if browser_download_url is not None or name is not None:
            _payload = EditAttachmentOptions(browser_download_url=browser_download_url, name=name).model_dump(
                mode="json", by_alias=True, exclude_none=True
            )
        else:
            _payload = None

        _response = await self._client._request(
            "PATCH", f"/repos/{owner}/{repo}/issues/{index}/assets/{attachment_id}", json=_payload
        )
        return decode(_response, Attachment)

    async def delete(self, owner: str, repo: str, index: int, attachment_id: int) -> None:
        """
        Delete an issue attachment.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the issue
            attachment_id: id of the attachment to delete

        Returns:
            No content.

        Raises:
            NotFoundError: 404. APIError is error format response.
            LockedError: 423. APIRepoArchivedError is an error that is raised when an archived repo should be modified.

        Operation ID: issueDeleteIssueAttachment
        """
        _response = await self._client._request(
            "DELETE", f"/repos/{owner}/{repo}/issues/{index}/assets/{attachment_id}"
        )
        return decode(_response, None)


class ReposIssuesBlocks:
    """The ``repos.issues.blocks`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def list(
        self,
        owner: str,
        repo: str,
        index: int,
        *,
        page: int | None = None,
        limit: int | None = None,
    ) -> Paginated[Issue]:
        """
        List issues that are blocked by this issue.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the issue
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            IssueListWithoutPagination - Issues without pagination headers (used for pinned issues, dependencies, etc.).

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: issueListBlocks
        """
        return self._client._paginate(
            "GET", f"/repos/{owner}/{repo}/issues/{index}/blocks", model=Issue, page=page, limit=limit
        )

    def create(
        self,
        owner: str,
        repo: str,
        index: int,
        *,
        body_index: int,
        body_owner: str,
        body_repo: str,
    ) -> Issue:
        """
        Block the issue given in the body by the issue in path.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the issue
            body_index: Wire field ``index``.
            body_owner: Wire field ``owner``.
            body_repo: Wire field ``repo``.

        Returns:
            Issue.

        Raises:
            NotFoundError: 404. the issue does not exist.

        Operation ID: issueCreateIssueBlocking
        """
        _payload = IssueMeta(
            index=body_index,
            owner=body_owner,
            repo=body_repo,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = self._client._request("POST", f"/repos/{owner}/{repo}/issues/{index}/blocks", json=_payload)
        return decode(_response, Issue)

    def delete(
        self,
        owner: str,
        repo: str,
        index: int,
        *,
        body_index: int,
        body_owner: str,
        body_repo: str,
    ) -> Issue:
        """
        Unblock the issue given in the body by the issue in path.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the issue
            body_index: Wire field ``index``.
            body_owner: Wire field ``owner``.
            body_repo: Wire field ``repo``.

        Returns:
            Issue.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: issueRemoveIssueBlocking
        """
        _payload = IssueMeta(
            index=body_index,
            owner=body_owner,
            repo=body_repo,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = self._client._request("DELETE", f"/repos/{owner}/{repo}/issues/{index}/blocks", json=_payload)
        return decode(_response, Issue)


class AsyncReposIssuesBlocks:
    """The ``repos.issues.blocks`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def list(
        self,
        owner: str,
        repo: str,
        index: int,
        *,
        page: int | None = None,
        limit: int | None = None,
    ) -> AsyncPaginated[Issue]:
        """
        List issues that are blocked by this issue.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the issue
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            IssueListWithoutPagination - Issues without pagination headers (used for pinned issues, dependencies, etc.).

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: issueListBlocks
        """
        return await self._client._paginate(
            "GET", f"/repos/{owner}/{repo}/issues/{index}/blocks", model=Issue, page=page, limit=limit
        )

    async def create(
        self,
        owner: str,
        repo: str,
        index: int,
        *,
        body_index: int,
        body_owner: str,
        body_repo: str,
    ) -> Issue:
        """
        Block the issue given in the body by the issue in path.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the issue
            body_index: Wire field ``index``.
            body_owner: Wire field ``owner``.
            body_repo: Wire field ``repo``.

        Returns:
            Issue.

        Raises:
            NotFoundError: 404. the issue does not exist.

        Operation ID: issueCreateIssueBlocking
        """
        _payload = IssueMeta(
            index=body_index,
            owner=body_owner,
            repo=body_repo,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = await self._client._request("POST", f"/repos/{owner}/{repo}/issues/{index}/blocks", json=_payload)
        return decode(_response, Issue)

    async def delete(
        self,
        owner: str,
        repo: str,
        index: int,
        *,
        body_index: int,
        body_owner: str,
        body_repo: str,
    ) -> Issue:
        """
        Unblock the issue given in the body by the issue in path.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the issue
            body_index: Wire field ``index``.
            body_owner: Wire field ``owner``.
            body_repo: Wire field ``repo``.

        Returns:
            Issue.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: issueRemoveIssueBlocking
        """
        _payload = IssueMeta(
            index=body_index,
            owner=body_owner,
            repo=body_repo,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = await self._client._request("DELETE", f"/repos/{owner}/{repo}/issues/{index}/blocks", json=_payload)
        return decode(_response, Issue)


class ReposIssuesComments:
    """The ``repos.issues.comments`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client
        self.assets: ReposIssuesCommentsAssets = ReposIssuesCommentsAssets(client)
        self.reactions: ReposIssuesCommentsReactions = ReposIssuesCommentsReactions(client)

    def list_all(
        self,
        owner: str,
        repo: str,
        *,
        since: datetime | None = None,
        before: datetime | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> Paginated[Comment]:
        """
        List all comments in a repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            since: if provided, only comments updated since the provided time are returned.
            before: if provided, only comments updated before the provided time are returned.
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            CommentList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.
            ServerError: 500. APIInternalServerError is an error that is raised when an internal server error occurs.

        Operation ID: issueGetRepoComments
        """
        _query: dict[str, object] = {
            "since": None if since is None else since.isoformat(),
            "before": None if before is None else before.isoformat(),
        }

        return self._client._paginate(
            "GET", f"/repos/{owner}/{repo}/issues/comments", model=Comment, params=_query, page=page, limit=limit
        )

    def get(self, owner: str, repo: str, id: int) -> Comment | None:
        """
        Get a comment.

        Args:
            owner: owner of the repo
            repo: name of the repo
            id: id of the comment

        Returns:
            Comment.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.
            ServerError: 500. APIInternalServerError is an error that is raised when an internal server error occurs.

        Operation ID: issueGetComment
        """
        _response = self._client._request("GET", f"/repos/{owner}/{repo}/issues/comments/{id}")
        return decode(_response, Comment)

    def update(
        self,
        owner: str,
        repo: str,
        id: int,
        *,
        body: str,
        updated_at: datetime | None = None,
    ) -> Comment | None:
        """
        Edit a comment.

        Args:
            owner: owner of the repo
            repo: name of the repo
            id: id of the comment to edit
            body: The body of the comment
            updated_at: The time of the comment's update, needs admin or repository owner permission

        Returns:
            Comment.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.
            LockedError: 423. APIRepoArchivedError is an error that is raised when an archived repo should be modified.
            ServerError: 500. APIInternalServerError is an error that is raised when an internal server error occurs.

        Operation ID: issueEditComment
        """
        _payload = EditIssueCommentOption(
            body=body,
            updated_at=updated_at,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = self._client._request("PATCH", f"/repos/{owner}/{repo}/issues/comments/{id}", json=_payload)
        return decode(_response, Comment)

    def delete(self, owner: str, repo: str, id: int) -> None:
        """
        Delete a comment.

        Args:
            owner: owner of the repo
            repo: name of the repo
            id: id of comment to delete

        Returns:
            No content.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            ServerError: 500. APIInternalServerError is an error that is raised when an internal server error occurs.

        Operation ID: issueDeleteComment
        """
        _response = self._client._request("DELETE", f"/repos/{owner}/{repo}/issues/comments/{id}")
        return decode(_response, None)

    def list(
        self,
        owner: str,
        repo: str,
        index: int,
        *,
        since: datetime | None = None,
        before: datetime | None = None,
    ) -> builtins.list[Comment]:
        """
        List all comments on an issue.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the issue
            since: if provided, only comments updated since the specified time are returned.
            before: if provided, only comments updated before the provided time are returned.

        Returns:
            CommentList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.
            ServerError: 500. APIInternalServerError is an error that is raised when an internal server error occurs.

        Operation ID: issueGetComments
        """
        _query: dict[str, object] = {
            "since": None if since is None else since.isoformat(),
            "before": None if before is None else before.isoformat(),
        }

        _response = self._client._request("GET", f"/repos/{owner}/{repo}/issues/{index}/comments", params=_query)
        return decode(_response, list[Comment])

    def create(self, owner: str, repo: str, index: int, *, body: str, updated_at: datetime | None = None) -> Comment:
        """
        Add a comment to an issue.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the issue
            body: The body of the comment
            updated_at: The time of the comment's update, needs admin or repository owner permission

        Returns:
            Comment.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.
            LockedError: 423. APIRepoArchivedError is an error that is raised when an archived repo should be modified.
            ServerError: 500. APIInternalServerError is an error that is raised when an internal server error occurs.

        Operation ID: issueCreateComment
        """
        _payload = CreateIssueCommentOption(
            body=body,
            updated_at=updated_at,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = self._client._request("POST", f"/repos/{owner}/{repo}/issues/{index}/comments", json=_payload)
        return decode(_response, Comment)

    def update_for_issue(
        self,
        owner: str,
        repo: str,
        index: int,
        id: int,
        *,
        body: str,
        updated_at: datetime | None = None,
    ) -> Comment | None:
        """
        Edit a comment.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: this parameter is ignored
            id: id of the comment to edit
            body: The body of the comment
            updated_at: The time of the comment's update, needs admin or repository owner permission

        Returns:
            Comment.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.
            ServerError: 500. APIInternalServerError is an error that is raised when an internal server error occurs.

        Deprecated:
            Deprecated in the vendored Spec; generated for compatibility.

        Operation ID: issueEditCommentDeprecated
        """
        _payload = EditIssueCommentOption(
            body=body,
            updated_at=updated_at,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = self._client._request("PATCH", f"/repos/{owner}/{repo}/issues/{index}/comments/{id}", json=_payload)
        return decode(_response, Comment)

    def delete_for_issue(self, owner: str, repo: str, index: int, id: int) -> None:
        """
        Delete a comment.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: this parameter is ignored
            id: id of comment to delete

        Returns:
            No content.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            ServerError: 500. APIInternalServerError is an error that is raised when an internal server error occurs.

        Deprecated:
            Deprecated in the vendored Spec; generated for compatibility.

        Operation ID: issueDeleteCommentDeprecated
        """
        _response = self._client._request("DELETE", f"/repos/{owner}/{repo}/issues/{index}/comments/{id}")
        return decode(_response, None)


class AsyncReposIssuesComments:
    """The ``repos.issues.comments`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client
        self.assets: AsyncReposIssuesCommentsAssets = AsyncReposIssuesCommentsAssets(client)
        self.reactions: AsyncReposIssuesCommentsReactions = AsyncReposIssuesCommentsReactions(client)

    async def list_all(
        self,
        owner: str,
        repo: str,
        *,
        since: datetime | None = None,
        before: datetime | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> AsyncPaginated[Comment]:
        """
        List all comments in a repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            since: if provided, only comments updated since the provided time are returned.
            before: if provided, only comments updated before the provided time are returned.
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            CommentList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.
            ServerError: 500. APIInternalServerError is an error that is raised when an internal server error occurs.

        Operation ID: issueGetRepoComments
        """
        _query: dict[str, object] = {
            "since": None if since is None else since.isoformat(),
            "before": None if before is None else before.isoformat(),
        }

        return await self._client._paginate(
            "GET", f"/repos/{owner}/{repo}/issues/comments", model=Comment, params=_query, page=page, limit=limit
        )

    async def get(self, owner: str, repo: str, id: int) -> Comment | None:
        """
        Get a comment.

        Args:
            owner: owner of the repo
            repo: name of the repo
            id: id of the comment

        Returns:
            Comment.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.
            ServerError: 500. APIInternalServerError is an error that is raised when an internal server error occurs.

        Operation ID: issueGetComment
        """
        _response = await self._client._request("GET", f"/repos/{owner}/{repo}/issues/comments/{id}")
        return decode(_response, Comment)

    async def update(
        self,
        owner: str,
        repo: str,
        id: int,
        *,
        body: str,
        updated_at: datetime | None = None,
    ) -> Comment | None:
        """
        Edit a comment.

        Args:
            owner: owner of the repo
            repo: name of the repo
            id: id of the comment to edit
            body: The body of the comment
            updated_at: The time of the comment's update, needs admin or repository owner permission

        Returns:
            Comment.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.
            LockedError: 423. APIRepoArchivedError is an error that is raised when an archived repo should be modified.
            ServerError: 500. APIInternalServerError is an error that is raised when an internal server error occurs.

        Operation ID: issueEditComment
        """
        _payload = EditIssueCommentOption(
            body=body,
            updated_at=updated_at,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = await self._client._request("PATCH", f"/repos/{owner}/{repo}/issues/comments/{id}", json=_payload)
        return decode(_response, Comment)

    async def delete(self, owner: str, repo: str, id: int) -> None:
        """
        Delete a comment.

        Args:
            owner: owner of the repo
            repo: name of the repo
            id: id of comment to delete

        Returns:
            No content.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            ServerError: 500. APIInternalServerError is an error that is raised when an internal server error occurs.

        Operation ID: issueDeleteComment
        """
        _response = await self._client._request("DELETE", f"/repos/{owner}/{repo}/issues/comments/{id}")
        return decode(_response, None)

    async def list(
        self,
        owner: str,
        repo: str,
        index: int,
        *,
        since: datetime | None = None,
        before: datetime | None = None,
    ) -> builtins.list[Comment]:
        """
        List all comments on an issue.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the issue
            since: if provided, only comments updated since the specified time are returned.
            before: if provided, only comments updated before the provided time are returned.

        Returns:
            CommentList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.
            ServerError: 500. APIInternalServerError is an error that is raised when an internal server error occurs.

        Operation ID: issueGetComments
        """
        _query: dict[str, object] = {
            "since": None if since is None else since.isoformat(),
            "before": None if before is None else before.isoformat(),
        }

        _response = await self._client._request("GET", f"/repos/{owner}/{repo}/issues/{index}/comments", params=_query)
        return decode(_response, list[Comment])

    async def create(
        self,
        owner: str,
        repo: str,
        index: int,
        *,
        body: str,
        updated_at: datetime | None = None,
    ) -> Comment:
        """
        Add a comment to an issue.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the issue
            body: The body of the comment
            updated_at: The time of the comment's update, needs admin or repository owner permission

        Returns:
            Comment.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.
            LockedError: 423. APIRepoArchivedError is an error that is raised when an archived repo should be modified.
            ServerError: 500. APIInternalServerError is an error that is raised when an internal server error occurs.

        Operation ID: issueCreateComment
        """
        _payload = CreateIssueCommentOption(
            body=body,
            updated_at=updated_at,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = await self._client._request("POST", f"/repos/{owner}/{repo}/issues/{index}/comments", json=_payload)
        return decode(_response, Comment)

    async def update_for_issue(
        self,
        owner: str,
        repo: str,
        index: int,
        id: int,
        *,
        body: str,
        updated_at: datetime | None = None,
    ) -> Comment | None:
        """
        Edit a comment.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: this parameter is ignored
            id: id of the comment to edit
            body: The body of the comment
            updated_at: The time of the comment's update, needs admin or repository owner permission

        Returns:
            Comment.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.
            ServerError: 500. APIInternalServerError is an error that is raised when an internal server error occurs.

        Deprecated:
            Deprecated in the vendored Spec; generated for compatibility.

        Operation ID: issueEditCommentDeprecated
        """
        _payload = EditIssueCommentOption(
            body=body,
            updated_at=updated_at,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = await self._client._request(
            "PATCH", f"/repos/{owner}/{repo}/issues/{index}/comments/{id}", json=_payload
        )
        return decode(_response, Comment)

    async def delete_for_issue(self, owner: str, repo: str, index: int, id: int) -> None:
        """
        Delete a comment.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: this parameter is ignored
            id: id of comment to delete

        Returns:
            No content.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            ServerError: 500. APIInternalServerError is an error that is raised when an internal server error occurs.

        Deprecated:
            Deprecated in the vendored Spec; generated for compatibility.

        Operation ID: issueDeleteCommentDeprecated
        """
        _response = await self._client._request("DELETE", f"/repos/{owner}/{repo}/issues/{index}/comments/{id}")
        return decode(_response, None)


class ReposIssuesCommentsAssets:
    """The ``repos.issues.comments.assets`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def list(self, owner: str, repo: str, id: int) -> builtins.list[Attachment]:
        """
        List comment's attachments.

        Args:
            owner: owner of the repo
            repo: name of the repo
            id: id of the comment

        Returns:
            AttachmentList.

        Raises:
            NotFoundError: 404. APIError is error format response.

        Operation ID: issueListIssueCommentAttachments
        """
        _response = self._client._request("GET", f"/repos/{owner}/{repo}/issues/comments/{id}/assets")
        return decode(_response, list[Attachment])

    def create(
        self,
        owner: str,
        repo: str,
        id: int,
        *,
        name: str | None = None,
        updated_at: datetime | None = None,
        attachment: FilePart,
    ) -> Attachment:
        """
        Create a comment attachment.

        Args:
            owner: owner of the repo
            repo: name of the repo
            id: id of the comment
            name: name of the attachment
            updated_at: time of the attachment's creation. This is a timestamp in RFC 3339 format
            attachment: attachment to upload

        Returns:
            Attachment.

        Raises:
            BadRequestError: 400. APIError is error format response.
            NotFoundError: 404. APIError is error format response.
            PayloadTooLargeError: 413. QuotaExceeded.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.
            LockedError: 423. APIRepoArchivedError is an error that is raised when an archived repo should be modified.

        Operation ID: issueCreateIssueCommentAttachment
        """
        _query: dict[str, object] = {"name": name, "updated_at": None if updated_at is None else updated_at.isoformat()}

        _files: dict[str, object] = {}
        _files["attachment"] = attachment

        _response = self._client._request(
            "POST", f"/repos/{owner}/{repo}/issues/comments/{id}/assets", params=_query, files=_files
        )
        return decode(_response, Attachment)

    def get(self, owner: str, repo: str, id: int, attachment_id: int) -> Attachment:
        """
        Get a comment attachment.

        Args:
            owner: owner of the repo
            repo: name of the repo
            id: id of the comment
            attachment_id: id of the attachment to get

        Returns:
            Attachment.

        Raises:
            NotFoundError: 404. APIError is error format response.

        Operation ID: issueGetIssueCommentAttachment
        """
        _response = self._client._request("GET", f"/repos/{owner}/{repo}/issues/comments/{id}/assets/{attachment_id}")
        return decode(_response, Attachment)

    def update(
        self,
        owner: str,
        repo: str,
        id: int,
        attachment_id: int,
        *,
        browser_download_url: str | None = None,
        name: str | None = None,
    ) -> Attachment:
        """
        Edit a comment attachment.

        Args:
            owner: owner of the repo
            repo: name of the repo
            id: id of the comment
            attachment_id: id of the attachment to edit
            browser_download_url: (Can only be set if existing attachment is of external type)
            name:

        Returns:
            Attachment.

        Raises:
            NotFoundError: 404. APIError is error format response.
            PayloadTooLargeError: 413. QuotaExceeded.
            LockedError: 423. APIRepoArchivedError is an error that is raised when an archived repo should be modified.

        Operation ID: issueEditIssueCommentAttachment
        """
        if browser_download_url is not None or name is not None:
            _payload = EditAttachmentOptions(browser_download_url=browser_download_url, name=name).model_dump(
                mode="json", by_alias=True, exclude_none=True
            )
        else:
            _payload = None

        _response = self._client._request(
            "PATCH", f"/repos/{owner}/{repo}/issues/comments/{id}/assets/{attachment_id}", json=_payload
        )
        return decode(_response, Attachment)

    def delete(self, owner: str, repo: str, id: int, attachment_id: int) -> None:
        """
        Delete a comment attachment.

        Args:
            owner: owner of the repo
            repo: name of the repo
            id: id of the comment
            attachment_id: id of the attachment to delete

        Returns:
            No content.

        Raises:
            NotFoundError: 404. APIError is error format response.
            LockedError: 423. APIRepoArchivedError is an error that is raised when an archived repo should be modified.

        Operation ID: issueDeleteIssueCommentAttachment
        """
        _response = self._client._request(
            "DELETE", f"/repos/{owner}/{repo}/issues/comments/{id}/assets/{attachment_id}"
        )
        return decode(_response, None)


class AsyncReposIssuesCommentsAssets:
    """The ``repos.issues.comments.assets`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def list(self, owner: str, repo: str, id: int) -> builtins.list[Attachment]:
        """
        List comment's attachments.

        Args:
            owner: owner of the repo
            repo: name of the repo
            id: id of the comment

        Returns:
            AttachmentList.

        Raises:
            NotFoundError: 404. APIError is error format response.

        Operation ID: issueListIssueCommentAttachments
        """
        _response = await self._client._request("GET", f"/repos/{owner}/{repo}/issues/comments/{id}/assets")
        return decode(_response, list[Attachment])

    async def create(
        self,
        owner: str,
        repo: str,
        id: int,
        *,
        name: str | None = None,
        updated_at: datetime | None = None,
        attachment: FilePart,
    ) -> Attachment:
        """
        Create a comment attachment.

        Args:
            owner: owner of the repo
            repo: name of the repo
            id: id of the comment
            name: name of the attachment
            updated_at: time of the attachment's creation. This is a timestamp in RFC 3339 format
            attachment: attachment to upload

        Returns:
            Attachment.

        Raises:
            BadRequestError: 400. APIError is error format response.
            NotFoundError: 404. APIError is error format response.
            PayloadTooLargeError: 413. QuotaExceeded.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.
            LockedError: 423. APIRepoArchivedError is an error that is raised when an archived repo should be modified.

        Operation ID: issueCreateIssueCommentAttachment
        """
        _query: dict[str, object] = {"name": name, "updated_at": None if updated_at is None else updated_at.isoformat()}

        _files: dict[str, object] = {}
        _files["attachment"] = attachment

        _response = await self._client._request(
            "POST", f"/repos/{owner}/{repo}/issues/comments/{id}/assets", params=_query, files=_files
        )
        return decode(_response, Attachment)

    async def get(self, owner: str, repo: str, id: int, attachment_id: int) -> Attachment:
        """
        Get a comment attachment.

        Args:
            owner: owner of the repo
            repo: name of the repo
            id: id of the comment
            attachment_id: id of the attachment to get

        Returns:
            Attachment.

        Raises:
            NotFoundError: 404. APIError is error format response.

        Operation ID: issueGetIssueCommentAttachment
        """
        _response = await self._client._request(
            "GET", f"/repos/{owner}/{repo}/issues/comments/{id}/assets/{attachment_id}"
        )
        return decode(_response, Attachment)

    async def update(
        self,
        owner: str,
        repo: str,
        id: int,
        attachment_id: int,
        *,
        browser_download_url: str | None = None,
        name: str | None = None,
    ) -> Attachment:
        """
        Edit a comment attachment.

        Args:
            owner: owner of the repo
            repo: name of the repo
            id: id of the comment
            attachment_id: id of the attachment to edit
            browser_download_url: (Can only be set if existing attachment is of external type)
            name:

        Returns:
            Attachment.

        Raises:
            NotFoundError: 404. APIError is error format response.
            PayloadTooLargeError: 413. QuotaExceeded.
            LockedError: 423. APIRepoArchivedError is an error that is raised when an archived repo should be modified.

        Operation ID: issueEditIssueCommentAttachment
        """
        if browser_download_url is not None or name is not None:
            _payload = EditAttachmentOptions(browser_download_url=browser_download_url, name=name).model_dump(
                mode="json", by_alias=True, exclude_none=True
            )
        else:
            _payload = None

        _response = await self._client._request(
            "PATCH", f"/repos/{owner}/{repo}/issues/comments/{id}/assets/{attachment_id}", json=_payload
        )
        return decode(_response, Attachment)

    async def delete(self, owner: str, repo: str, id: int, attachment_id: int) -> None:
        """
        Delete a comment attachment.

        Args:
            owner: owner of the repo
            repo: name of the repo
            id: id of the comment
            attachment_id: id of the attachment to delete

        Returns:
            No content.

        Raises:
            NotFoundError: 404. APIError is error format response.
            LockedError: 423. APIRepoArchivedError is an error that is raised when an archived repo should be modified.

        Operation ID: issueDeleteIssueCommentAttachment
        """
        _response = await self._client._request(
            "DELETE", f"/repos/{owner}/{repo}/issues/comments/{id}/assets/{attachment_id}"
        )
        return decode(_response, None)


class ReposIssuesCommentsReactions:
    """The ``repos.issues.comments.reactions`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def list(self, owner: str, repo: str, id: int) -> builtins.list[Reaction]:
        """
        Get a list of reactions from a comment of an issue.

        Args:
            owner: owner of the repo
            repo: name of the repo
            id: id of the comment to edit

        Returns:
            ReactionListWithoutPagination - Reactions for a specific comment (no pagination headers).

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: issueGetCommentReactions
        """
        _response = self._client._request("GET", f"/repos/{owner}/{repo}/issues/comments/{id}/reactions")
        return decode(_response, list[Reaction])

    def create(self, owner: str, repo: str, id: int, *, content: str | None = None) -> Reaction:
        """
        Add a reaction to a comment of an issue.

        Args:
            owner: owner of the repo
            repo: name of the repo
            id: id of the comment to edit
            content:

        Returns:
            Reaction.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: issuePostCommentReaction
        """
        if content is not None:
            _payload = EditReactionOption(content=content).model_dump(mode="json", by_alias=True, exclude_none=True)
        else:
            _payload = None

        _response = self._client._request(
            "POST", f"/repos/{owner}/{repo}/issues/comments/{id}/reactions", json=_payload
        )
        return decode(_response, Reaction)

    def delete(self, owner: str, repo: str, id: int, *, content: str | None = None) -> None:
        """
        Remove a reaction from a comment of an issue.

        Args:
            owner: owner of the repo
            repo: name of the repo
            id: id of the comment to edit
            content:

        Returns:
            No content.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: issueDeleteCommentReaction
        """
        if content is not None:
            _payload = EditReactionOption(content=content).model_dump(mode="json", by_alias=True, exclude_none=True)
        else:
            _payload = None

        _response = self._client._request(
            "DELETE", f"/repos/{owner}/{repo}/issues/comments/{id}/reactions", json=_payload
        )
        return decode(_response, None)


class AsyncReposIssuesCommentsReactions:
    """The ``repos.issues.comments.reactions`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def list(self, owner: str, repo: str, id: int) -> builtins.list[Reaction]:
        """
        Get a list of reactions from a comment of an issue.

        Args:
            owner: owner of the repo
            repo: name of the repo
            id: id of the comment to edit

        Returns:
            ReactionListWithoutPagination - Reactions for a specific comment (no pagination headers).

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: issueGetCommentReactions
        """
        _response = await self._client._request("GET", f"/repos/{owner}/{repo}/issues/comments/{id}/reactions")
        return decode(_response, list[Reaction])

    async def create(self, owner: str, repo: str, id: int, *, content: str | None = None) -> Reaction:
        """
        Add a reaction to a comment of an issue.

        Args:
            owner: owner of the repo
            repo: name of the repo
            id: id of the comment to edit
            content:

        Returns:
            Reaction.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: issuePostCommentReaction
        """
        if content is not None:
            _payload = EditReactionOption(content=content).model_dump(mode="json", by_alias=True, exclude_none=True)
        else:
            _payload = None

        _response = await self._client._request(
            "POST", f"/repos/{owner}/{repo}/issues/comments/{id}/reactions", json=_payload
        )
        return decode(_response, Reaction)

    async def delete(self, owner: str, repo: str, id: int, *, content: str | None = None) -> None:
        """
        Remove a reaction from a comment of an issue.

        Args:
            owner: owner of the repo
            repo: name of the repo
            id: id of the comment to edit
            content:

        Returns:
            No content.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: issueDeleteCommentReaction
        """
        if content is not None:
            _payload = EditReactionOption(content=content).model_dump(mode="json", by_alias=True, exclude_none=True)
        else:
            _payload = None

        _response = await self._client._request(
            "DELETE", f"/repos/{owner}/{repo}/issues/comments/{id}/reactions", json=_payload
        )
        return decode(_response, None)


class ReposIssuesDependencies:
    """The ``repos.issues.dependencies`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def list(
        self,
        owner: str,
        repo: str,
        index: int,
        *,
        page: int | None = None,
        limit: int | None = None,
    ) -> Paginated[Issue]:
        """
        List an issue's dependencies, i.e all issues that block this issue.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the issue
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            IssueListWithoutPagination - Issues without pagination headers (used for pinned issues, dependencies, etc.).

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: issueListIssueDependencies
        """
        return self._client._paginate(
            "GET", f"/repos/{owner}/{repo}/issues/{index}/dependencies", model=Issue, page=page, limit=limit
        )

    def create(
        self,
        owner: str,
        repo: str,
        index: int,
        *,
        body_index: int,
        body_owner: str,
        body_repo: str,
    ) -> Issue:
        """
        Make the issue in the url depend on the issue in the form.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the issue
            body_index: Wire field ``index``.
            body_owner: Wire field ``owner``.
            body_repo: Wire field ``repo``.

        Returns:
            Issue.

        Raises:
            NotFoundError: 404. the issue does not exist.
            LockedError: 423. APIRepoArchivedError is an error that is raised when an archived repo should be modified.

        Operation ID: issueCreateIssueDependencies
        """
        _payload = IssueMeta(
            index=body_index,
            owner=body_owner,
            repo=body_repo,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = self._client._request("POST", f"/repos/{owner}/{repo}/issues/{index}/dependencies", json=_payload)
        return decode(_response, Issue)

    def delete(
        self,
        owner: str,
        repo: str,
        index: int,
        *,
        body_index: int,
        body_owner: str,
        body_repo: str,
    ) -> Issue:
        """
        Remove an issue dependency.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the issue
            body_index: Wire field ``index``.
            body_owner: Wire field ``owner``.
            body_repo: Wire field ``repo``.

        Returns:
            Issue.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.
            LockedError: 423. APIRepoArchivedError is an error that is raised when an archived repo should be modified.

        Operation ID: issueRemoveIssueDependencies
        """
        _payload = IssueMeta(
            index=body_index,
            owner=body_owner,
            repo=body_repo,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = self._client._request("DELETE", f"/repos/{owner}/{repo}/issues/{index}/dependencies", json=_payload)
        return decode(_response, Issue)


class AsyncReposIssuesDependencies:
    """The ``repos.issues.dependencies`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def list(
        self,
        owner: str,
        repo: str,
        index: int,
        *,
        page: int | None = None,
        limit: int | None = None,
    ) -> AsyncPaginated[Issue]:
        """
        List an issue's dependencies, i.e all issues that block this issue.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the issue
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            IssueListWithoutPagination - Issues without pagination headers (used for pinned issues, dependencies, etc.).

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: issueListIssueDependencies
        """
        return await self._client._paginate(
            "GET", f"/repos/{owner}/{repo}/issues/{index}/dependencies", model=Issue, page=page, limit=limit
        )

    async def create(
        self,
        owner: str,
        repo: str,
        index: int,
        *,
        body_index: int,
        body_owner: str,
        body_repo: str,
    ) -> Issue:
        """
        Make the issue in the url depend on the issue in the form.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the issue
            body_index: Wire field ``index``.
            body_owner: Wire field ``owner``.
            body_repo: Wire field ``repo``.

        Returns:
            Issue.

        Raises:
            NotFoundError: 404. the issue does not exist.
            LockedError: 423. APIRepoArchivedError is an error that is raised when an archived repo should be modified.

        Operation ID: issueCreateIssueDependencies
        """
        _payload = IssueMeta(
            index=body_index,
            owner=body_owner,
            repo=body_repo,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = await self._client._request(
            "POST", f"/repos/{owner}/{repo}/issues/{index}/dependencies", json=_payload
        )
        return decode(_response, Issue)

    async def delete(
        self,
        owner: str,
        repo: str,
        index: int,
        *,
        body_index: int,
        body_owner: str,
        body_repo: str,
    ) -> Issue:
        """
        Remove an issue dependency.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the issue
            body_index: Wire field ``index``.
            body_owner: Wire field ``owner``.
            body_repo: Wire field ``repo``.

        Returns:
            Issue.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.
            LockedError: 423. APIRepoArchivedError is an error that is raised when an archived repo should be modified.

        Operation ID: issueRemoveIssueDependencies
        """
        _payload = IssueMeta(
            index=body_index,
            owner=body_owner,
            repo=body_repo,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = await self._client._request(
            "DELETE", f"/repos/{owner}/{repo}/issues/{index}/dependencies", json=_payload
        )
        return decode(_response, Issue)


class ReposIssuesLabels:
    """The ``repos.issues.labels`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def list(self, owner: str, repo: str, index: int) -> builtins.list[Label]:
        """
        Get an issue's labels.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the issue

        Returns:
            LabelListWithoutPagination - Labels for a specific issue (no pagination headers).

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: issueGetLabels
        """
        _response = self._client._request("GET", f"/repos/{owner}/{repo}/issues/{index}/labels")
        return decode(_response, list[Label])

    def add(
        self,
        owner: str,
        repo: str,
        index: int,
        *,
        labels: builtins.list[object] | None = None,
        updated_at: datetime | None = None,
    ) -> builtins.list[Label]:
        """
        Add a label to an issue.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the issue
            labels: Labels can be a list of integers representing label IDs or a list of strings representing label
                names
            updated_at:

        Returns:
            LabelListWithoutPagination - Labels for a specific issue (no pagination headers).

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: issueAddLabel
        """
        if labels is not None or updated_at is not None:
            _payload = IssueLabelsOption(labels=labels, updated_at=updated_at).model_dump(
                mode="json", by_alias=True, exclude_none=True
            )
        else:
            _payload = None

        _response = self._client._request("POST", f"/repos/{owner}/{repo}/issues/{index}/labels", json=_payload)
        return decode(_response, list[Label])

    def update(
        self,
        owner: str,
        repo: str,
        index: int,
        *,
        labels: builtins.list[object] | None = None,
        updated_at: datetime | None = None,
    ) -> builtins.list[Label]:
        """
        Replace an issue's labels.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the issue
            labels: Labels can be a list of integers representing label IDs or a list of strings representing label
                names
            updated_at:

        Returns:
            LabelListWithoutPagination - Labels for a specific issue (no pagination headers).

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: issueReplaceLabels
        """
        if labels is not None or updated_at is not None:
            _payload = IssueLabelsOption(labels=labels, updated_at=updated_at).model_dump(
                mode="json", by_alias=True, exclude_none=True
            )
        else:
            _payload = None

        _response = self._client._request("PUT", f"/repos/{owner}/{repo}/issues/{index}/labels", json=_payload)
        return decode(_response, list[Label])

    def clear(self, owner: str, repo: str, index: int, *, updated_at: datetime | None = None) -> None:
        """
        Remove all labels from an issue.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the issue
            updated_at:

        Returns:
            No content.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: issueClearLabels
        """
        if updated_at is not None:
            _payload = DeleteLabelsOption(updated_at=updated_at).model_dump(
                mode="json", by_alias=True, exclude_none=True
            )
        else:
            _payload = None

        _response = self._client._request("DELETE", f"/repos/{owner}/{repo}/issues/{index}/labels", json=_payload)
        return decode(_response, None)

    def delete(self, owner: str, repo: str, index: int, identifier: str, *, updated_at: datetime | None = None) -> None:
        """
        Remove a label from an issue.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the issue
            identifier: name or id of the label to remove
            updated_at:

        Returns:
            No content.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: issueRemoveLabel
        """
        if updated_at is not None:
            _payload = DeleteLabelsOption(updated_at=updated_at).model_dump(
                mode="json", by_alias=True, exclude_none=True
            )
        else:
            _payload = None

        _response = self._client._request(
            "DELETE", f"/repos/{owner}/{repo}/issues/{index}/labels/{identifier}", json=_payload
        )
        return decode(_response, None)


class AsyncReposIssuesLabels:
    """The ``repos.issues.labels`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def list(self, owner: str, repo: str, index: int) -> builtins.list[Label]:
        """
        Get an issue's labels.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the issue

        Returns:
            LabelListWithoutPagination - Labels for a specific issue (no pagination headers).

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: issueGetLabels
        """
        _response = await self._client._request("GET", f"/repos/{owner}/{repo}/issues/{index}/labels")
        return decode(_response, list[Label])

    async def add(
        self,
        owner: str,
        repo: str,
        index: int,
        *,
        labels: builtins.list[object] | None = None,
        updated_at: datetime | None = None,
    ) -> builtins.list[Label]:
        """
        Add a label to an issue.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the issue
            labels: Labels can be a list of integers representing label IDs or a list of strings representing label
                names
            updated_at:

        Returns:
            LabelListWithoutPagination - Labels for a specific issue (no pagination headers).

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: issueAddLabel
        """
        if labels is not None or updated_at is not None:
            _payload = IssueLabelsOption(labels=labels, updated_at=updated_at).model_dump(
                mode="json", by_alias=True, exclude_none=True
            )
        else:
            _payload = None

        _response = await self._client._request("POST", f"/repos/{owner}/{repo}/issues/{index}/labels", json=_payload)
        return decode(_response, list[Label])

    async def update(
        self,
        owner: str,
        repo: str,
        index: int,
        *,
        labels: builtins.list[object] | None = None,
        updated_at: datetime | None = None,
    ) -> builtins.list[Label]:
        """
        Replace an issue's labels.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the issue
            labels: Labels can be a list of integers representing label IDs or a list of strings representing label
                names
            updated_at:

        Returns:
            LabelListWithoutPagination - Labels for a specific issue (no pagination headers).

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: issueReplaceLabels
        """
        if labels is not None or updated_at is not None:
            _payload = IssueLabelsOption(labels=labels, updated_at=updated_at).model_dump(
                mode="json", by_alias=True, exclude_none=True
            )
        else:
            _payload = None

        _response = await self._client._request("PUT", f"/repos/{owner}/{repo}/issues/{index}/labels", json=_payload)
        return decode(_response, list[Label])

    async def clear(self, owner: str, repo: str, index: int, *, updated_at: datetime | None = None) -> None:
        """
        Remove all labels from an issue.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the issue
            updated_at:

        Returns:
            No content.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: issueClearLabels
        """
        if updated_at is not None:
            _payload = DeleteLabelsOption(updated_at=updated_at).model_dump(
                mode="json", by_alias=True, exclude_none=True
            )
        else:
            _payload = None

        _response = await self._client._request("DELETE", f"/repos/{owner}/{repo}/issues/{index}/labels", json=_payload)
        return decode(_response, None)

    async def delete(
        self,
        owner: str,
        repo: str,
        index: int,
        identifier: str,
        *,
        updated_at: datetime | None = None,
    ) -> None:
        """
        Remove a label from an issue.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the issue
            identifier: name or id of the label to remove
            updated_at:

        Returns:
            No content.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: issueRemoveLabel
        """
        if updated_at is not None:
            _payload = DeleteLabelsOption(updated_at=updated_at).model_dump(
                mode="json", by_alias=True, exclude_none=True
            )
        else:
            _payload = None

        _response = await self._client._request(
            "DELETE", f"/repos/{owner}/{repo}/issues/{index}/labels/{identifier}", json=_payload
        )
        return decode(_response, None)


class ReposIssuesReactions:
    """The ``repos.issues.reactions`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def list(
        self,
        owner: str,
        repo: str,
        index: int,
        *,
        page: int | None = None,
        limit: int | None = None,
    ) -> Paginated[Reaction]:
        """
        Get a list reactions of an issue.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the issue
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            ReactionList.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: issueGetIssueReactions
        """
        return self._client._paginate(
            "GET", f"/repos/{owner}/{repo}/issues/{index}/reactions", model=Reaction, page=page, limit=limit
        )

    def create(self, owner: str, repo: str, index: int, *, content: str | None = None) -> Reaction:
        """
        Add a reaction to an issue.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the issue
            content:

        Returns:
            Reaction.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: issuePostIssueReaction
        """
        if content is not None:
            _payload = EditReactionOption(content=content).model_dump(mode="json", by_alias=True, exclude_none=True)
        else:
            _payload = None

        _response = self._client._request("POST", f"/repos/{owner}/{repo}/issues/{index}/reactions", json=_payload)
        return decode(_response, Reaction)

    def delete(self, owner: str, repo: str, index: int, *, content: str | None = None) -> None:
        """
        Remove a reaction from an issue.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the issue
            content:

        Returns:
            No content.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: issueDeleteIssueReaction
        """
        if content is not None:
            _payload = EditReactionOption(content=content).model_dump(mode="json", by_alias=True, exclude_none=True)
        else:
            _payload = None

        _response = self._client._request("DELETE", f"/repos/{owner}/{repo}/issues/{index}/reactions", json=_payload)
        return decode(_response, None)


class AsyncReposIssuesReactions:
    """The ``repos.issues.reactions`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def list(
        self,
        owner: str,
        repo: str,
        index: int,
        *,
        page: int | None = None,
        limit: int | None = None,
    ) -> AsyncPaginated[Reaction]:
        """
        Get a list reactions of an issue.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the issue
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            ReactionList.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: issueGetIssueReactions
        """
        return await self._client._paginate(
            "GET", f"/repos/{owner}/{repo}/issues/{index}/reactions", model=Reaction, page=page, limit=limit
        )

    async def create(self, owner: str, repo: str, index: int, *, content: str | None = None) -> Reaction:
        """
        Add a reaction to an issue.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the issue
            content:

        Returns:
            Reaction.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: issuePostIssueReaction
        """
        if content is not None:
            _payload = EditReactionOption(content=content).model_dump(mode="json", by_alias=True, exclude_none=True)
        else:
            _payload = None

        _response = await self._client._request(
            "POST", f"/repos/{owner}/{repo}/issues/{index}/reactions", json=_payload
        )
        return decode(_response, Reaction)

    async def delete(self, owner: str, repo: str, index: int, *, content: str | None = None) -> None:
        """
        Remove a reaction from an issue.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the issue
            content:

        Returns:
            No content.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: issueDeleteIssueReaction
        """
        if content is not None:
            _payload = EditReactionOption(content=content).model_dump(mode="json", by_alias=True, exclude_none=True)
        else:
            _payload = None

        _response = await self._client._request(
            "DELETE", f"/repos/{owner}/{repo}/issues/{index}/reactions", json=_payload
        )
        return decode(_response, None)


class ReposIssuesStopwatch:
    """The ``repos.issues.stopwatch`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def delete(self, owner: str, repo: str, index: int) -> None:
        """
        Delete an issue's existing stopwatch.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the issue to stop the stopwatch on

        Returns:
            No content.

        Raises:
            ForbiddenError: 403. Not repo writer, user does not have rights to toggle stopwatch.
            NotFoundError: 404. APINotFound is a not found error response.
            ConflictError: 409. Cannot cancel a non existent stopwatch.

        Operation ID: issueDeleteStopWatch
        """
        _response = self._client._request("DELETE", f"/repos/{owner}/{repo}/issues/{index}/stopwatch/delete")
        return decode(_response, None)

    def start(self, owner: str, repo: str, index: int) -> None:
        """
        Start stopwatch on an issue.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the issue to create the stopwatch on

        Returns:
            No content.

        Raises:
            ForbiddenError: 403. Not repo writer, user does not have rights to toggle stopwatch.
            NotFoundError: 404. APINotFound is a not found error response.
            ConflictError: 409. Cannot start a stopwatch again if it already exists.

        Operation ID: issueStartStopWatch
        """
        _response = self._client._request("POST", f"/repos/{owner}/{repo}/issues/{index}/stopwatch/start")
        return decode(_response, None)

    def stop(self, owner: str, repo: str, index: int) -> None:
        """
        Stop an issue's existing stopwatch.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the issue to stop the stopwatch on

        Returns:
            No content.

        Raises:
            ForbiddenError: 403. Not repo writer, user does not have rights to toggle stopwatch.
            NotFoundError: 404. APINotFound is a not found error response.
            ConflictError: 409. Cannot stop a non existent stopwatch.

        Operation ID: issueStopStopWatch
        """
        _response = self._client._request("POST", f"/repos/{owner}/{repo}/issues/{index}/stopwatch/stop")
        return decode(_response, None)


class AsyncReposIssuesStopwatch:
    """The ``repos.issues.stopwatch`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def delete(self, owner: str, repo: str, index: int) -> None:
        """
        Delete an issue's existing stopwatch.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the issue to stop the stopwatch on

        Returns:
            No content.

        Raises:
            ForbiddenError: 403. Not repo writer, user does not have rights to toggle stopwatch.
            NotFoundError: 404. APINotFound is a not found error response.
            ConflictError: 409. Cannot cancel a non existent stopwatch.

        Operation ID: issueDeleteStopWatch
        """
        _response = await self._client._request("DELETE", f"/repos/{owner}/{repo}/issues/{index}/stopwatch/delete")
        return decode(_response, None)

    async def start(self, owner: str, repo: str, index: int) -> None:
        """
        Start stopwatch on an issue.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the issue to create the stopwatch on

        Returns:
            No content.

        Raises:
            ForbiddenError: 403. Not repo writer, user does not have rights to toggle stopwatch.
            NotFoundError: 404. APINotFound is a not found error response.
            ConflictError: 409. Cannot start a stopwatch again if it already exists.

        Operation ID: issueStartStopWatch
        """
        _response = await self._client._request("POST", f"/repos/{owner}/{repo}/issues/{index}/stopwatch/start")
        return decode(_response, None)

    async def stop(self, owner: str, repo: str, index: int) -> None:
        """
        Stop an issue's existing stopwatch.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the issue to stop the stopwatch on

        Returns:
            No content.

        Raises:
            ForbiddenError: 403. Not repo writer, user does not have rights to toggle stopwatch.
            NotFoundError: 404. APINotFound is a not found error response.
            ConflictError: 409. Cannot stop a non existent stopwatch.

        Operation ID: issueStopStopWatch
        """
        _response = await self._client._request("POST", f"/repos/{owner}/{repo}/issues/{index}/stopwatch/stop")
        return decode(_response, None)


class ReposIssuesSubscriptions:
    """The ``repos.issues.subscriptions`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def list(
        self,
        owner: str,
        repo: str,
        index: int,
        *,
        page: int | None = None,
        limit: int | None = None,
    ) -> Paginated[User]:
        """
        Get users who subscribed on an issue.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the issue
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            UserList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: issueSubscriptions
        """
        return self._client._paginate(
            "GET", f"/repos/{owner}/{repo}/issues/{index}/subscriptions", model=User, page=page, limit=limit
        )

    def check(self, owner: str, repo: str, index: int) -> WatchInfo:
        """
        Check if user is subscribed to an issue.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the issue

        Returns:
            WatchInfo.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: issueCheckSubscription
        """
        _response = self._client._request("GET", f"/repos/{owner}/{repo}/issues/{index}/subscriptions/check")
        return decode(_response, WatchInfo)

    def add(self, owner: str, repo: str, index: int, user: str) -> None:
        """
        Subscribe user to issue.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the issue
            user: user to subscribe

        Returns:
            No content.

        Raises:
            APIError: 304. User can only subscribe itself if he is no admin.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: issueAddSubscription
        """
        _response = self._client._request("PUT", f"/repos/{owner}/{repo}/issues/{index}/subscriptions/{user}")
        return decode(_response, None)

    def remove(self, owner: str, repo: str, index: int, user: str) -> None:
        """
        Unsubscribe user from issue.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the issue
            user: user witch unsubscribe

        Returns:
            No content.

        Raises:
            APIError: 304. User can only subscribe itself if he is no admin.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: issueDeleteSubscription
        """
        _response = self._client._request("DELETE", f"/repos/{owner}/{repo}/issues/{index}/subscriptions/{user}")
        return decode(_response, None)


class AsyncReposIssuesSubscriptions:
    """The ``repos.issues.subscriptions`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def list(
        self,
        owner: str,
        repo: str,
        index: int,
        *,
        page: int | None = None,
        limit: int | None = None,
    ) -> AsyncPaginated[User]:
        """
        Get users who subscribed on an issue.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the issue
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            UserList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: issueSubscriptions
        """
        return await self._client._paginate(
            "GET", f"/repos/{owner}/{repo}/issues/{index}/subscriptions", model=User, page=page, limit=limit
        )

    async def check(self, owner: str, repo: str, index: int) -> WatchInfo:
        """
        Check if user is subscribed to an issue.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the issue

        Returns:
            WatchInfo.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: issueCheckSubscription
        """
        _response = await self._client._request("GET", f"/repos/{owner}/{repo}/issues/{index}/subscriptions/check")
        return decode(_response, WatchInfo)

    async def add(self, owner: str, repo: str, index: int, user: str) -> None:
        """
        Subscribe user to issue.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the issue
            user: user to subscribe

        Returns:
            No content.

        Raises:
            APIError: 304. User can only subscribe itself if he is no admin.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: issueAddSubscription
        """
        _response = await self._client._request("PUT", f"/repos/{owner}/{repo}/issues/{index}/subscriptions/{user}")
        return decode(_response, None)

    async def remove(self, owner: str, repo: str, index: int, user: str) -> None:
        """
        Unsubscribe user from issue.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the issue
            user: user witch unsubscribe

        Returns:
            No content.

        Raises:
            APIError: 304. User can only subscribe itself if he is no admin.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: issueDeleteSubscription
        """
        _response = await self._client._request("DELETE", f"/repos/{owner}/{repo}/issues/{index}/subscriptions/{user}")
        return decode(_response, None)


class ReposIssuesTimes:
    """The ``repos.issues.times`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def list(
        self,
        owner: str,
        repo: str,
        index: int,
        *,
        user: str | None = None,
        since: datetime | None = None,
        before: datetime | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> Paginated[TrackedTime]:
        """
        List an issue's tracked times.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the issue
            user: optional filter by user (available for issue managers)
            since: Only show times updated after the given time. This is a timestamp in RFC 3339 format
            before: Only show times updated before the given time. This is a timestamp in RFC 3339 format
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            TrackedTimeList.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: issueTrackedTimes
        """
        _query: dict[str, object] = {
            "user": user,
            "since": None if since is None else since.isoformat(),
            "before": None if before is None else before.isoformat(),
        }

        return self._client._paginate(
            "GET",
            f"/repos/{owner}/{repo}/issues/{index}/times",
            model=TrackedTime,
            params=_query,
            page=page,
            limit=limit,
        )

    def add(
        self,
        owner: str,
        repo: str,
        index: int,
        *,
        created: datetime | None = None,
        time: int,
        user_name: str | None = None,
    ) -> TrackedTime:
        """
        Add tracked time to a issue.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the issue
            created:
            time: time in seconds
            user_name: User who spent the time (optional)

        Returns:
            TrackedTime.

        Raises:
            BadRequestError: 400. APIError is error format response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: issueAddTime
        """
        _payload = AddTimeOption(
            created=created,
            time=time,
            user_name=user_name,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = self._client._request("POST", f"/repos/{owner}/{repo}/issues/{index}/times", json=_payload)
        return decode(_response, TrackedTime)

    def reset(self, owner: str, repo: str, index: int) -> None:
        """
        Reset a tracked time of an issue.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the issue to add tracked time to

        Returns:
            No content.

        Raises:
            BadRequestError: 400. APIError is error format response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: issueResetTime
        """
        _response = self._client._request("DELETE", f"/repos/{owner}/{repo}/issues/{index}/times")
        return decode(_response, None)

    def delete(self, owner: str, repo: str, index: int, id: int) -> None:
        """
        Delete specific tracked time.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the issue
            id: id of time to delete

        Returns:
            No content.

        Raises:
            BadRequestError: 400. APIError is error format response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: issueDeleteTime
        """
        _response = self._client._request("DELETE", f"/repos/{owner}/{repo}/issues/{index}/times/{id}")
        return decode(_response, None)


class AsyncReposIssuesTimes:
    """The ``repos.issues.times`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def list(
        self,
        owner: str,
        repo: str,
        index: int,
        *,
        user: str | None = None,
        since: datetime | None = None,
        before: datetime | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> AsyncPaginated[TrackedTime]:
        """
        List an issue's tracked times.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the issue
            user: optional filter by user (available for issue managers)
            since: Only show times updated after the given time. This is a timestamp in RFC 3339 format
            before: Only show times updated before the given time. This is a timestamp in RFC 3339 format
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            TrackedTimeList.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: issueTrackedTimes
        """
        _query: dict[str, object] = {
            "user": user,
            "since": None if since is None else since.isoformat(),
            "before": None if before is None else before.isoformat(),
        }

        return await self._client._paginate(
            "GET",
            f"/repos/{owner}/{repo}/issues/{index}/times",
            model=TrackedTime,
            params=_query,
            page=page,
            limit=limit,
        )

    async def add(
        self,
        owner: str,
        repo: str,
        index: int,
        *,
        created: datetime | None = None,
        time: int,
        user_name: str | None = None,
    ) -> TrackedTime:
        """
        Add tracked time to a issue.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the issue
            created:
            time: time in seconds
            user_name: User who spent the time (optional)

        Returns:
            TrackedTime.

        Raises:
            BadRequestError: 400. APIError is error format response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: issueAddTime
        """
        _payload = AddTimeOption(
            created=created,
            time=time,
            user_name=user_name,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = await self._client._request("POST", f"/repos/{owner}/{repo}/issues/{index}/times", json=_payload)
        return decode(_response, TrackedTime)

    async def reset(self, owner: str, repo: str, index: int) -> None:
        """
        Reset a tracked time of an issue.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the issue to add tracked time to

        Returns:
            No content.

        Raises:
            BadRequestError: 400. APIError is error format response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: issueResetTime
        """
        _response = await self._client._request("DELETE", f"/repos/{owner}/{repo}/issues/{index}/times")
        return decode(_response, None)

    async def delete(self, owner: str, repo: str, index: int, id: int) -> None:
        """
        Delete specific tracked time.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the issue
            id: id of time to delete

        Returns:
            No content.

        Raises:
            BadRequestError: 400. APIError is error format response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: issueDeleteTime
        """
        _response = await self._client._request("DELETE", f"/repos/{owner}/{repo}/issues/{index}/times/{id}")
        return decode(_response, None)


class ReposKeys:
    """The ``repos.keys`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def list(
        self,
        owner: str,
        repo: str,
        *,
        key_id: int | None = None,
        fingerprint: str | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> Paginated[DeployKey]:
        """
        List a repository's keys.

        Args:
            owner: owner of the repo
            repo: name of the repo
            key_id: the key_id to search for
            fingerprint: fingerprint of the key
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            DeployKeyList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoListKeys
        """
        _query: dict[str, object] = {"key_id": key_id, "fingerprint": fingerprint}

        return self._client._paginate(
            "GET", f"/repos/{owner}/{repo}/keys", model=DeployKey, params=_query, page=page, limit=limit
        )

    def create(self, owner: str, repo: str, *, key: str, read_only: bool | None = None, title: str) -> DeployKey:
        """
        Add a key to a repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            key: An armored SSH key to add
            read_only: Describe if the key has only read access or read/write
            title: Title of the key to add

        Returns:
            DeployKey.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: repoCreateKey
        """
        _payload = CreateKeyOption(
            key=key,
            read_only=read_only,
            title=title,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = self._client._request("POST", f"/repos/{owner}/{repo}/keys", json=_payload)
        return decode(_response, DeployKey)

    def get(self, owner: str, repo: str, id: int) -> DeployKey:
        """
        Get a repository's key by id.

        Args:
            owner: owner of the repo
            repo: name of the repo
            id: id of the key to get

        Returns:
            DeployKey.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoGetKey
        """
        _response = self._client._request("GET", f"/repos/{owner}/{repo}/keys/{id}")
        return decode(_response, DeployKey)

    def delete(self, owner: str, repo: str, id: int) -> None:
        """
        Delete a key from a repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            id: id of the key to delete

        Returns:
            No content.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoDeleteKey
        """
        _response = self._client._request("DELETE", f"/repos/{owner}/{repo}/keys/{id}")
        return decode(_response, None)


class AsyncReposKeys:
    """The ``repos.keys`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def list(
        self,
        owner: str,
        repo: str,
        *,
        key_id: int | None = None,
        fingerprint: str | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> AsyncPaginated[DeployKey]:
        """
        List a repository's keys.

        Args:
            owner: owner of the repo
            repo: name of the repo
            key_id: the key_id to search for
            fingerprint: fingerprint of the key
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            DeployKeyList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoListKeys
        """
        _query: dict[str, object] = {"key_id": key_id, "fingerprint": fingerprint}

        return await self._client._paginate(
            "GET", f"/repos/{owner}/{repo}/keys", model=DeployKey, params=_query, page=page, limit=limit
        )

    async def create(self, owner: str, repo: str, *, key: str, read_only: bool | None = None, title: str) -> DeployKey:
        """
        Add a key to a repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            key: An armored SSH key to add
            read_only: Describe if the key has only read access or read/write
            title: Title of the key to add

        Returns:
            DeployKey.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: repoCreateKey
        """
        _payload = CreateKeyOption(
            key=key,
            read_only=read_only,
            title=title,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = await self._client._request("POST", f"/repos/{owner}/{repo}/keys", json=_payload)
        return decode(_response, DeployKey)

    async def get(self, owner: str, repo: str, id: int) -> DeployKey:
        """
        Get a repository's key by id.

        Args:
            owner: owner of the repo
            repo: name of the repo
            id: id of the key to get

        Returns:
            DeployKey.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoGetKey
        """
        _response = await self._client._request("GET", f"/repos/{owner}/{repo}/keys/{id}")
        return decode(_response, DeployKey)

    async def delete(self, owner: str, repo: str, id: int) -> None:
        """
        Delete a key from a repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            id: id of the key to delete

        Returns:
            No content.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoDeleteKey
        """
        _response = await self._client._request("DELETE", f"/repos/{owner}/{repo}/keys/{id}")
        return decode(_response, None)


class ReposLabels:
    """The ``repos.labels`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def list(
        self,
        owner: str,
        repo: str,
        *,
        sort: Literal["mostissues", "leastissues", "reversealphabetically"] | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> Paginated[Label]:
        """
        Get all of a repository's labels.

        Args:
            owner: owner of the repo
            repo: name of the repo
            sort: Specifies the sorting method: mostissues, leastissues, or reversealphabetically.
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            LabelList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: issueListLabels
        """
        _query: dict[str, object] = {"sort": sort}

        return self._client._paginate(
            "GET", f"/repos/{owner}/{repo}/labels", model=Label, params=_query, page=page, limit=limit
        )

    def create(
        self,
        owner: str,
        repo: str,
        *,
        color: str,
        description: str | None = None,
        exclusive: bool | None = None,
        is_archived: bool | None = None,
        name: str,
    ) -> Label:
        """
        Create a label.

        Args:
            owner: owner of the repo
            repo: name of the repo
            color:
            description:
            exclusive:
            is_archived:
            name:

        Returns:
            Label.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: issueCreateLabel
        """
        _payload = CreateLabelOption(
            color=color,
            description=description,
            exclusive=exclusive,
            is_archived=is_archived,
            name=name,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = self._client._request("POST", f"/repos/{owner}/{repo}/labels", json=_payload)
        return decode(_response, Label)

    def get(self, owner: str, repo: str, id: int) -> Label:
        """
        Get a single label.

        Args:
            owner: owner of the repo
            repo: name of the repo
            id: id of the label to get

        Returns:
            Label.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: issueGetLabel
        """
        _response = self._client._request("GET", f"/repos/{owner}/{repo}/labels/{id}")
        return decode(_response, Label)

    def update(
        self,
        owner: str,
        repo: str,
        id: int,
        *,
        color: str | None = None,
        description: str | None = None,
        exclusive: bool | None = None,
        is_archived: bool | None = None,
        name: str | None = None,
    ) -> Label:
        """
        Update a label.

        Args:
            owner: owner of the repo
            repo: name of the repo
            id: id of the label to edit
            color:
            description:
            exclusive:
            is_archived:
            name:

        Returns:
            Label.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: issueEditLabel
        """
        if (
            color is not None
            or description is not None
            or exclusive is not None
            or is_archived is not None
            or name is not None
        ):
            _payload = EditLabelOption(
                color=color, description=description, exclusive=exclusive, is_archived=is_archived, name=name
            ).model_dump(mode="json", by_alias=True, exclude_none=True)
        else:
            _payload = None

        _response = self._client._request("PATCH", f"/repos/{owner}/{repo}/labels/{id}", json=_payload)
        return decode(_response, Label)

    def delete(self, owner: str, repo: str, id: int) -> None:
        """
        Delete a label.

        Args:
            owner: owner of the repo
            repo: name of the repo
            id: id of the label to delete

        Returns:
            No content.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: issueDeleteLabel
        """
        _response = self._client._request("DELETE", f"/repos/{owner}/{repo}/labels/{id}")
        return decode(_response, None)


class AsyncReposLabels:
    """The ``repos.labels`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def list(
        self,
        owner: str,
        repo: str,
        *,
        sort: Literal["mostissues", "leastissues", "reversealphabetically"] | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> AsyncPaginated[Label]:
        """
        Get all of a repository's labels.

        Args:
            owner: owner of the repo
            repo: name of the repo
            sort: Specifies the sorting method: mostissues, leastissues, or reversealphabetically.
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            LabelList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: issueListLabels
        """
        _query: dict[str, object] = {"sort": sort}

        return await self._client._paginate(
            "GET", f"/repos/{owner}/{repo}/labels", model=Label, params=_query, page=page, limit=limit
        )

    async def create(
        self,
        owner: str,
        repo: str,
        *,
        color: str,
        description: str | None = None,
        exclusive: bool | None = None,
        is_archived: bool | None = None,
        name: str,
    ) -> Label:
        """
        Create a label.

        Args:
            owner: owner of the repo
            repo: name of the repo
            color:
            description:
            exclusive:
            is_archived:
            name:

        Returns:
            Label.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: issueCreateLabel
        """
        _payload = CreateLabelOption(
            color=color,
            description=description,
            exclusive=exclusive,
            is_archived=is_archived,
            name=name,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = await self._client._request("POST", f"/repos/{owner}/{repo}/labels", json=_payload)
        return decode(_response, Label)

    async def get(self, owner: str, repo: str, id: int) -> Label:
        """
        Get a single label.

        Args:
            owner: owner of the repo
            repo: name of the repo
            id: id of the label to get

        Returns:
            Label.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: issueGetLabel
        """
        _response = await self._client._request("GET", f"/repos/{owner}/{repo}/labels/{id}")
        return decode(_response, Label)

    async def update(
        self,
        owner: str,
        repo: str,
        id: int,
        *,
        color: str | None = None,
        description: str | None = None,
        exclusive: bool | None = None,
        is_archived: bool | None = None,
        name: str | None = None,
    ) -> Label:
        """
        Update a label.

        Args:
            owner: owner of the repo
            repo: name of the repo
            id: id of the label to edit
            color:
            description:
            exclusive:
            is_archived:
            name:

        Returns:
            Label.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: issueEditLabel
        """
        if (
            color is not None
            or description is not None
            or exclusive is not None
            or is_archived is not None
            or name is not None
        ):
            _payload = EditLabelOption(
                color=color, description=description, exclusive=exclusive, is_archived=is_archived, name=name
            ).model_dump(mode="json", by_alias=True, exclude_none=True)
        else:
            _payload = None

        _response = await self._client._request("PATCH", f"/repos/{owner}/{repo}/labels/{id}", json=_payload)
        return decode(_response, Label)

    async def delete(self, owner: str, repo: str, id: int) -> None:
        """
        Delete a label.

        Args:
            owner: owner of the repo
            repo: name of the repo
            id: id of the label to delete

        Returns:
            No content.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: issueDeleteLabel
        """
        _response = await self._client._request("DELETE", f"/repos/{owner}/{repo}/labels/{id}")
        return decode(_response, None)


class ReposMedia:
    """The ``repos.media`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def get(self, owner: str, repo: str, filepath: str, *, ref: str | None = None) -> bytes:
        """
        Get a file or it's LFS object from a repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            filepath: filepath of the file to get
            ref: The name of the commit/branch/tag. Default the repository's default branch (usually master)

        Returns:
            Returns raw file content.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoGetRawFileOrLFS
        """
        _query: dict[str, object] = {"ref": ref}

        _response = self._client._request("GET", f"/repos/{owner}/{repo}/media/{filepath}", params=_query)
        return decode(_response, bytes)


class AsyncReposMedia:
    """The ``repos.media`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def get(self, owner: str, repo: str, filepath: str, *, ref: str | None = None) -> bytes:
        """
        Get a file or it's LFS object from a repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            filepath: filepath of the file to get
            ref: The name of the commit/branch/tag. Default the repository's default branch (usually master)

        Returns:
            Returns raw file content.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoGetRawFileOrLFS
        """
        _query: dict[str, object] = {"ref": ref}

        _response = await self._client._request("GET", f"/repos/{owner}/{repo}/media/{filepath}", params=_query)
        return decode(_response, bytes)


class ReposMilestones:
    """The ``repos.milestones`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def list(
        self,
        owner: str,
        repo: str,
        *,
        state: str | None = None,
        name: str | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> Paginated[Milestone]:
        """
        Get all of a repository's opened milestones.

        Args:
            owner: owner of the repo
            repo: name of the repo
            state: Milestone state, Recognized values are open, closed and all. Defaults to "open"
            name: filter by milestone name
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            MilestoneList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: issueGetMilestonesList
        """
        _query: dict[str, object] = {"state": state, "name": name}

        return self._client._paginate(
            "GET", f"/repos/{owner}/{repo}/milestones", model=Milestone, params=_query, page=page, limit=limit
        )

    def create(
        self,
        owner: str,
        repo: str,
        *,
        description: str | None = None,
        due_on: datetime | None = None,
        state: CreateMilestoneOptionState | None = None,
        title: str | None = None,
    ) -> Milestone:
        """
        Create a milestone.

        Args:
            owner: owner of the repo
            repo: name of the repo
            description:
            due_on:
            state:
            title:

        Returns:
            Milestone.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: issueCreateMilestone
        """
        if description is not None or due_on is not None or state is not None or title is not None:
            _payload = CreateMilestoneOption(
                description=description, due_on=due_on, state=state, title=title
            ).model_dump(mode="json", by_alias=True, exclude_none=True)
        else:
            _payload = None

        _response = self._client._request("POST", f"/repos/{owner}/{repo}/milestones", json=_payload)
        return decode(_response, Milestone)

    def get(self, owner: str, repo: str, id: int) -> Milestone:
        """
        Get a milestone.

        Args:
            owner: owner of the repo
            repo: name of the repo
            id: the milestone to get, identified by ID and if not available by name

        Returns:
            Milestone.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: issueGetMilestone
        """
        _response = self._client._request("GET", f"/repos/{owner}/{repo}/milestones/{id}")
        return decode(_response, Milestone)

    def update(
        self,
        owner: str,
        repo: str,
        id: int,
        *,
        description: str | None = None,
        due_on: datetime | None = None,
        state: str | None = None,
        title: str | None = None,
    ) -> Milestone:
        """
        Update a milestone.

        Args:
            owner: owner of the repo
            repo: name of the repo
            id: the milestone to edit, identified by ID and if not available by name
            description:
            due_on:
            state:
            title:

        Returns:
            Milestone.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: issueEditMilestone
        """
        if description is not None or due_on is not None or state is not None or title is not None:
            _payload = EditMilestoneOption(description=description, due_on=due_on, state=state, title=title).model_dump(
                mode="json", by_alias=True, exclude_none=True
            )
        else:
            _payload = None

        _response = self._client._request("PATCH", f"/repos/{owner}/{repo}/milestones/{id}", json=_payload)
        return decode(_response, Milestone)

    def delete(self, owner: str, repo: str, id: int) -> None:
        """
        Delete a milestone.

        Args:
            owner: owner of the repo
            repo: name of the repo
            id: the milestone to delete, identified by ID and if not available by name

        Returns:
            No content.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: issueDeleteMilestone
        """
        _response = self._client._request("DELETE", f"/repos/{owner}/{repo}/milestones/{id}")
        return decode(_response, None)


class AsyncReposMilestones:
    """The ``repos.milestones`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def list(
        self,
        owner: str,
        repo: str,
        *,
        state: str | None = None,
        name: str | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> AsyncPaginated[Milestone]:
        """
        Get all of a repository's opened milestones.

        Args:
            owner: owner of the repo
            repo: name of the repo
            state: Milestone state, Recognized values are open, closed and all. Defaults to "open"
            name: filter by milestone name
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            MilestoneList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: issueGetMilestonesList
        """
        _query: dict[str, object] = {"state": state, "name": name}

        return await self._client._paginate(
            "GET", f"/repos/{owner}/{repo}/milestones", model=Milestone, params=_query, page=page, limit=limit
        )

    async def create(
        self,
        owner: str,
        repo: str,
        *,
        description: str | None = None,
        due_on: datetime | None = None,
        state: CreateMilestoneOptionState | None = None,
        title: str | None = None,
    ) -> Milestone:
        """
        Create a milestone.

        Args:
            owner: owner of the repo
            repo: name of the repo
            description:
            due_on:
            state:
            title:

        Returns:
            Milestone.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: issueCreateMilestone
        """
        if description is not None or due_on is not None or state is not None or title is not None:
            _payload = CreateMilestoneOption(
                description=description, due_on=due_on, state=state, title=title
            ).model_dump(mode="json", by_alias=True, exclude_none=True)
        else:
            _payload = None

        _response = await self._client._request("POST", f"/repos/{owner}/{repo}/milestones", json=_payload)
        return decode(_response, Milestone)

    async def get(self, owner: str, repo: str, id: int) -> Milestone:
        """
        Get a milestone.

        Args:
            owner: owner of the repo
            repo: name of the repo
            id: the milestone to get, identified by ID and if not available by name

        Returns:
            Milestone.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: issueGetMilestone
        """
        _response = await self._client._request("GET", f"/repos/{owner}/{repo}/milestones/{id}")
        return decode(_response, Milestone)

    async def update(
        self,
        owner: str,
        repo: str,
        id: int,
        *,
        description: str | None = None,
        due_on: datetime | None = None,
        state: str | None = None,
        title: str | None = None,
    ) -> Milestone:
        """
        Update a milestone.

        Args:
            owner: owner of the repo
            repo: name of the repo
            id: the milestone to edit, identified by ID and if not available by name
            description:
            due_on:
            state:
            title:

        Returns:
            Milestone.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: issueEditMilestone
        """
        if description is not None or due_on is not None or state is not None or title is not None:
            _payload = EditMilestoneOption(description=description, due_on=due_on, state=state, title=title).model_dump(
                mode="json", by_alias=True, exclude_none=True
            )
        else:
            _payload = None

        _response = await self._client._request("PATCH", f"/repos/{owner}/{repo}/milestones/{id}", json=_payload)
        return decode(_response, Milestone)

    async def delete(self, owner: str, repo: str, id: int) -> None:
        """
        Delete a milestone.

        Args:
            owner: owner of the repo
            repo: name of the repo
            id: the milestone to delete, identified by ID and if not available by name

        Returns:
            No content.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: issueDeleteMilestone
        """
        _response = await self._client._request("DELETE", f"/repos/{owner}/{repo}/milestones/{id}")
        return decode(_response, None)


class ReposNotifications:
    """The ``repos.notifications`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def list(
        self,
        owner: str,
        repo: str,
        *,
        all: bool | None = None,
        status_types: builtins.list[str] | None = None,
        subject_type: builtins.list[Literal["issue", "pull", "repository"]] | None = None,
        since: datetime | None = None,
        before: datetime | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> Paginated[NotificationThread]:
        """
        List users's notification threads on a specific repo.

        Args:
            owner: owner of the repo
            repo: name of the repo
            all: If true, show notifications marked as read. Default value is false
            status_types: Show notifications with the provided status types. Options are: unread, read and/or pinned.
                Defaults to unread & pinned
            subject_type: filter notifications by subject type
            since: Only show notifications updated after the given time. This is a timestamp in RFC 3339 format
            before: Only show notifications updated before the given time. This is a timestamp in RFC 3339 format
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            NotificationThreadList.

        Operation ID: notifyGetRepoList
        """
        _query: dict[str, object] = {
            "all": all,
            "status-types": status_types,
            "subject-type": subject_type,
            "since": None if since is None else since.isoformat(),
            "before": None if before is None else before.isoformat(),
        }

        return self._client._paginate(
            "GET",
            f"/repos/{owner}/{repo}/notifications",
            model=NotificationThread,
            params=_query,
            page=page,
            limit=limit,
        )

    def update(
        self,
        owner: str,
        repo: str,
        *,
        all: bool | None = None,
        status_types: builtins.list[str] | None = None,
        to_status: str | None = None,
        last_read_at: datetime | None = None,
    ) -> None:
        """
        Mark notification threads as read, pinned or unread on a specific repo.

        Args:
            owner: owner of the repo
            repo: name of the repo
            all: If true, mark all notifications on this repo. Default value is false
            status_types: Mark notifications with the provided status types. Options are: unread, read and/or pinned.
                Defaults to unread.
            to_status: Status to mark notifications as. Defaults to read.
            last_read_at: Describes the last point that notifications were checked. Anything updated since this time
                will not be updated.

        Returns:
            No content.

        Operation ID: notifyReadRepoList
        """
        _query: dict[str, object] = {
            "all": all,
            "status-types": status_types,
            "to-status": to_status,
            "last_read_at": None if last_read_at is None else last_read_at.isoformat(),
        }

        _response = self._client._request("PUT", f"/repos/{owner}/{repo}/notifications", params=_query)
        return decode(_response, None)


class AsyncReposNotifications:
    """The ``repos.notifications`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def list(
        self,
        owner: str,
        repo: str,
        *,
        all: bool | None = None,
        status_types: builtins.list[str] | None = None,
        subject_type: builtins.list[Literal["issue", "pull", "repository"]] | None = None,
        since: datetime | None = None,
        before: datetime | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> AsyncPaginated[NotificationThread]:
        """
        List users's notification threads on a specific repo.

        Args:
            owner: owner of the repo
            repo: name of the repo
            all: If true, show notifications marked as read. Default value is false
            status_types: Show notifications with the provided status types. Options are: unread, read and/or pinned.
                Defaults to unread & pinned
            subject_type: filter notifications by subject type
            since: Only show notifications updated after the given time. This is a timestamp in RFC 3339 format
            before: Only show notifications updated before the given time. This is a timestamp in RFC 3339 format
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            NotificationThreadList.

        Operation ID: notifyGetRepoList
        """
        _query: dict[str, object] = {
            "all": all,
            "status-types": status_types,
            "subject-type": subject_type,
            "since": None if since is None else since.isoformat(),
            "before": None if before is None else before.isoformat(),
        }

        return await self._client._paginate(
            "GET",
            f"/repos/{owner}/{repo}/notifications",
            model=NotificationThread,
            params=_query,
            page=page,
            limit=limit,
        )

    async def update(
        self,
        owner: str,
        repo: str,
        *,
        all: bool | None = None,
        status_types: builtins.list[str] | None = None,
        to_status: str | None = None,
        last_read_at: datetime | None = None,
    ) -> None:
        """
        Mark notification threads as read, pinned or unread on a specific repo.

        Args:
            owner: owner of the repo
            repo: name of the repo
            all: If true, mark all notifications on this repo. Default value is false
            status_types: Mark notifications with the provided status types. Options are: unread, read and/or pinned.
                Defaults to unread.
            to_status: Status to mark notifications as. Defaults to read.
            last_read_at: Describes the last point that notifications were checked. Anything updated since this time
                will not be updated.

        Returns:
            No content.

        Operation ID: notifyReadRepoList
        """
        _query: dict[str, object] = {
            "all": all,
            "status-types": status_types,
            "to-status": to_status,
            "last_read_at": None if last_read_at is None else last_read_at.isoformat(),
        }

        _response = await self._client._request("PUT", f"/repos/{owner}/{repo}/notifications", params=_query)
        return decode(_response, None)


class ReposPulls:
    """The ``repos.pulls`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client
        self.requested_reviewers: ReposPullsRequestedReviewers = ReposPullsRequestedReviewers(client)
        self.reviews: ReposPullsReviews = ReposPullsReviews(client)

    def list(
        self,
        owner: str,
        repo: str,
        *,
        state: Literal["open", "closed", "all"] | None = None,
        sort: Literal["oldest", "recentupdate", "recentclose", "leastupdate", "mostcomment", "leastcomment", "priority"]
        | None = None,
        milestone: int | None = None,
        labels: builtins.list[int] | None = None,
        poster: str | None = None,
        base: str | None = None,
        head: str | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> Paginated[PullRequest]:
        """
        List a repo's pull requests. If a pull request is selected but fails to be retrieved for any reason, it will be
        a null value in the list of results.

        Args:
            owner: Owner of the repo
            repo: Name of the repo
            state: State of pull request
            sort: Type of sort
            milestone: ID of the milestone
            labels: Label IDs
            poster: Filter by pull request author
            base: Filter by base branch name
            head: Filter by head branch name
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            PullRequestList.

        Raises:
            BadRequestError: 400. APIError is error format response.
            NotFoundError: 404. APINotFound is a not found error response.
            ServerError: 500. APIError is error format response.

        Operation ID: repoListPullRequests
        """
        _query: dict[str, object] = {
            "state": state,
            "sort": sort,
            "milestone": milestone,
            "labels": labels,
            "poster": poster,
            "base": base,
            "head": head,
        }

        return self._client._paginate(
            "GET", f"/repos/{owner}/{repo}/pulls", model=PullRequest, params=_query, page=page, limit=limit
        )

    def create(
        self,
        owner: str,
        repo: str,
        *,
        assignee: str | None = None,
        assignees: builtins.list[str] | None = None,
        base: str | None = None,
        body: str | None = None,
        due_date: datetime | None = None,
        head: str | None = None,
        labels: builtins.list[int] | None = None,
        milestone: int | None = None,
        title: str | None = None,
    ) -> PullRequest:
        """
        Create a pull request.

        Args:
            owner: owner of the repo
            repo: name of the repo
            assignee:
            assignees:
            base:
            body:
            due_date:
            head:
            labels:
            milestone:
            title:

        Returns:
            PullRequest.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.
            ConflictError: 409. APIError is error format response.
            PayloadTooLargeError: 413. QuotaExceeded.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.
            LockedError: 423. APIRepoArchivedError is an error that is raised when an archived repo should be modified.

        Operation ID: repoCreatePullRequest
        """
        if (
            assignee is not None
            or assignees is not None
            or base is not None
            or body is not None
            or due_date is not None
            or head is not None
            or labels is not None
            or milestone is not None
            or title is not None
        ):
            _payload = CreatePullRequestOption(
                assignee=assignee,
                assignees=assignees,
                base=base,
                body=body,
                due_date=due_date,
                head=head,
                labels=labels,
                milestone=milestone,
                title=title,
            ).model_dump(mode="json", by_alias=True, exclude_none=True)
        else:
            _payload = None

        _response = self._client._request("POST", f"/repos/{owner}/{repo}/pulls", json=_payload)
        return decode(_response, PullRequest)

    def pinned(self, owner: str, repo: str) -> builtins.list[PullRequest]:
        """
        List a repo's pinned pull requests.

        Args:
            owner: owner of the repo
            repo: name of the repo

        Returns:
            PullRequestList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoListPinnedPullRequests
        """
        _response = self._client._request("GET", f"/repos/{owner}/{repo}/pulls/pinned")
        return decode(_response, list[PullRequest])

    def get_by_base_head(self, owner: str, repo: str, base: str, head: str) -> PullRequest:
        """
        Get a pull request by base and head.

        Args:
            owner: owner of the repo
            repo: name of the repo
            base: base of the pull request to get
            head: head of the pull request to get

        Returns:
            PullRequest.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoGetPullRequestByBaseHead
        """
        _response = self._client._request("GET", f"/repos/{owner}/{repo}/pulls/{base}/{head}")
        return decode(_response, PullRequest)

    def get(self, owner: str, repo: str, index: int) -> PullRequest:
        """
        Get a pull request.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the pull request to get

        Returns:
            PullRequest.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoGetPullRequest
        """
        _response = self._client._request("GET", f"/repos/{owner}/{repo}/pulls/{index}")
        return decode(_response, PullRequest)

    def update(
        self,
        owner: str,
        repo: str,
        index: int,
        *,
        allow_maintainer_edit: bool | None = None,
        assignee: str | None = None,
        assignees: builtins.list[str] | None = None,
        base: str | None = None,
        body: str | None = None,
        due_date: datetime | None = None,
        labels: builtins.list[int] | None = None,
        milestone: int | None = None,
        state: str | None = None,
        title: str | None = None,
        unset_due_date: bool | None = None,
    ) -> PullRequest:
        """
        Update a pull request. If using deadline only the date will be taken into account, and time of day ignored.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the pull request to edit
            allow_maintainer_edit:
            assignee:
            assignees:
            base:
            body:
            due_date:
            labels:
            milestone:
            state:
            title:
            unset_due_date:

        Returns:
            PullRequest.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.
            ConflictError: 409. APIError is error format response.
            PreconditionFailedError: 412. APIError is error format response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: repoEditPullRequest
        """
        if (
            allow_maintainer_edit is not None
            or assignee is not None
            or assignees is not None
            or base is not None
            or body is not None
            or due_date is not None
            or labels is not None
            or milestone is not None
            or state is not None
            or title is not None
            or unset_due_date is not None
        ):
            _payload = EditPullRequestOption(
                allow_maintainer_edit=allow_maintainer_edit,
                assignee=assignee,
                assignees=assignees,
                base=base,
                body=body,
                due_date=due_date,
                labels=labels,
                milestone=milestone,
                state=state,
                title=title,
                unset_due_date=unset_due_date,
            ).model_dump(mode="json", by_alias=True, exclude_none=True)
        else:
            _payload = None

        _response = self._client._request("PATCH", f"/repos/{owner}/{repo}/pulls/{index}", json=_payload)
        return decode(_response, PullRequest)

    def download(
        self,
        owner: str,
        repo: str,
        index: int,
        diff_type: Literal["diff", "patch"],
        *,
        binary: bool | None = None,
    ) -> str:
        """
        Get a pull request diff or patch.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the pull request to get
            diff_type: whether the output is diff or patch
            binary: whether to include binary file changes. if true, the diff is applicable with `git apply`

        Returns:
            APIString is a string response.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoDownloadPullDiffOrPatch
        """
        _query: dict[str, object] = {"binary": binary}

        _response = self._client._request("GET", f"/repos/{owner}/{repo}/pulls/{index}.{diff_type}", params=_query)
        return decode(_response, str)

    def commits(
        self,
        owner: str,
        repo: str,
        index: int,
        *,
        verification: bool | None = None,
        files: bool | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> Paginated[Commit]:
        """
        Get commits for a pull request.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the pull request to get
            verification: include verification for every commit (disable for speedup, default 'true')
            files: include a list of affected files for every commit (disable for speedup, default 'true')
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            CommitList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoGetPullRequestCommits
        """
        _query: dict[str, object] = {"verification": verification, "files": files}

        return self._client._paginate(
            "GET", f"/repos/{owner}/{repo}/pulls/{index}/commits", model=Commit, params=_query, page=page, limit=limit
        )

    def files(
        self,
        owner: str,
        repo: str,
        index: int,
        *,
        skip_to: str | None = None,
        whitespace: Literal["ignore-all", "ignore-change", "ignore-eol", "show-all"] | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> Paginated[ChangedFile]:
        """
        Get changed files for a pull request.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the pull request to get
            skip_to: skip to given file
            whitespace: whitespace behavior
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            ChangedFileListWithPagination.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoGetPullRequestFiles
        """
        _query: dict[str, object] = {"skip-to": skip_to, "whitespace": whitespace}

        return self._client._paginate(
            "GET",
            f"/repos/{owner}/{repo}/pulls/{index}/files",
            model=ChangedFile,
            params=_query,
            page=page,
            limit=limit,
        )

    def is_merged(self, owner: str, repo: str, index: int) -> None:
        """
        Check if a pull request has been merged.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the pull request

        Returns:
            No content.

        Raises:
            NotFoundError: 404. pull request has not been merged.

        Operation ID: repoPullRequestIsMerged
        """
        _response = self._client._request("GET", f"/repos/{owner}/{repo}/pulls/{index}/merge")
        return decode(_response, None)

    def merge(
        self,
        owner: str,
        repo: str,
        index: int,
        *,
        do: MergePullRequestOptionDo,
        merge_commit_id: str | None = None,
        merge_message_field: str | None = None,
        merge_title_field: str | None = None,
        delete_branch_after_merge: bool | None = None,
        force_merge: bool | None = None,
        head_commit_id: str | None = None,
        merge_when_checks_succeed: bool | None = None,
    ) -> None:
        """
        Merge a pull request.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the pull request to merge
            do:
            merge_commit_id:
            merge_message_field:
            merge_title_field:
            delete_branch_after_merge:
            force_merge:
            head_commit_id:
            merge_when_checks_succeed:

        Returns:
            No content.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.
            MethodNotAllowedError: 405. APIEmpty is an empty response.
            ConflictError: 409. APIError is error format response.
            PayloadTooLargeError: 413. QuotaExceeded.
            LockedError: 423. APIRepoArchivedError is an error that is raised when an archived repo should be modified.

        Operation ID: repoMergePullRequest
        """
        _payload = MergePullRequestOption(
            do=do,
            merge_commit_id=merge_commit_id,
            merge_message_field=merge_message_field,
            merge_title_field=merge_title_field,
            delete_branch_after_merge=delete_branch_after_merge,
            force_merge=force_merge,
            head_commit_id=head_commit_id,
            merge_when_checks_succeed=merge_when_checks_succeed,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = self._client._request("POST", f"/repos/{owner}/{repo}/pulls/{index}/merge", json=_payload)
        return decode(_response, None)

    def cancel_auto_merge(self, owner: str, repo: str, index: int) -> None:
        """
        Cancel the scheduled auto merge for the given pull request.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the pull request to merge

        Returns:
            No content.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.
            LockedError: 423. APIRepoArchivedError is an error that is raised when an archived repo should be modified.

        Operation ID: repoCancelScheduledAutoMerge
        """
        _response = self._client._request("DELETE", f"/repos/{owner}/{repo}/pulls/{index}/merge")
        return decode(_response, None)

    def update_branch(
        self,
        owner: str,
        repo: str,
        index: int,
        *,
        style: Literal["merge", "rebase"] | None = None,
    ) -> None:
        """
        Merge PR's baseBranch into headBranch.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the pull request to get
            style: how to update pull request

        Returns:
            No content.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.
            ConflictError: 409. APIError is error format response.
            PayloadTooLargeError: 413. QuotaExceeded.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: repoUpdatePullRequest
        """
        _query: dict[str, object] = {"style": style}

        _response = self._client._request("POST", f"/repos/{owner}/{repo}/pulls/{index}/update", params=_query)
        return decode(_response, None)


class AsyncReposPulls:
    """The ``repos.pulls`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client
        self.requested_reviewers: AsyncReposPullsRequestedReviewers = AsyncReposPullsRequestedReviewers(client)
        self.reviews: AsyncReposPullsReviews = AsyncReposPullsReviews(client)

    async def list(
        self,
        owner: str,
        repo: str,
        *,
        state: Literal["open", "closed", "all"] | None = None,
        sort: Literal["oldest", "recentupdate", "recentclose", "leastupdate", "mostcomment", "leastcomment", "priority"]
        | None = None,
        milestone: int | None = None,
        labels: builtins.list[int] | None = None,
        poster: str | None = None,
        base: str | None = None,
        head: str | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> AsyncPaginated[PullRequest]:
        """
        List a repo's pull requests. If a pull request is selected but fails to be retrieved for any reason, it will be
        a null value in the list of results.

        Args:
            owner: Owner of the repo
            repo: Name of the repo
            state: State of pull request
            sort: Type of sort
            milestone: ID of the milestone
            labels: Label IDs
            poster: Filter by pull request author
            base: Filter by base branch name
            head: Filter by head branch name
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            PullRequestList.

        Raises:
            BadRequestError: 400. APIError is error format response.
            NotFoundError: 404. APINotFound is a not found error response.
            ServerError: 500. APIError is error format response.

        Operation ID: repoListPullRequests
        """
        _query: dict[str, object] = {
            "state": state,
            "sort": sort,
            "milestone": milestone,
            "labels": labels,
            "poster": poster,
            "base": base,
            "head": head,
        }

        return await self._client._paginate(
            "GET", f"/repos/{owner}/{repo}/pulls", model=PullRequest, params=_query, page=page, limit=limit
        )

    async def create(
        self,
        owner: str,
        repo: str,
        *,
        assignee: str | None = None,
        assignees: builtins.list[str] | None = None,
        base: str | None = None,
        body: str | None = None,
        due_date: datetime | None = None,
        head: str | None = None,
        labels: builtins.list[int] | None = None,
        milestone: int | None = None,
        title: str | None = None,
    ) -> PullRequest:
        """
        Create a pull request.

        Args:
            owner: owner of the repo
            repo: name of the repo
            assignee:
            assignees:
            base:
            body:
            due_date:
            head:
            labels:
            milestone:
            title:

        Returns:
            PullRequest.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.
            ConflictError: 409. APIError is error format response.
            PayloadTooLargeError: 413. QuotaExceeded.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.
            LockedError: 423. APIRepoArchivedError is an error that is raised when an archived repo should be modified.

        Operation ID: repoCreatePullRequest
        """
        if (
            assignee is not None
            or assignees is not None
            or base is not None
            or body is not None
            or due_date is not None
            or head is not None
            or labels is not None
            or milestone is not None
            or title is not None
        ):
            _payload = CreatePullRequestOption(
                assignee=assignee,
                assignees=assignees,
                base=base,
                body=body,
                due_date=due_date,
                head=head,
                labels=labels,
                milestone=milestone,
                title=title,
            ).model_dump(mode="json", by_alias=True, exclude_none=True)
        else:
            _payload = None

        _response = await self._client._request("POST", f"/repos/{owner}/{repo}/pulls", json=_payload)
        return decode(_response, PullRequest)

    async def pinned(self, owner: str, repo: str) -> builtins.list[PullRequest]:
        """
        List a repo's pinned pull requests.

        Args:
            owner: owner of the repo
            repo: name of the repo

        Returns:
            PullRequestList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoListPinnedPullRequests
        """
        _response = await self._client._request("GET", f"/repos/{owner}/{repo}/pulls/pinned")
        return decode(_response, list[PullRequest])

    async def get_by_base_head(self, owner: str, repo: str, base: str, head: str) -> PullRequest:
        """
        Get a pull request by base and head.

        Args:
            owner: owner of the repo
            repo: name of the repo
            base: base of the pull request to get
            head: head of the pull request to get

        Returns:
            PullRequest.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoGetPullRequestByBaseHead
        """
        _response = await self._client._request("GET", f"/repos/{owner}/{repo}/pulls/{base}/{head}")
        return decode(_response, PullRequest)

    async def get(self, owner: str, repo: str, index: int) -> PullRequest:
        """
        Get a pull request.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the pull request to get

        Returns:
            PullRequest.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoGetPullRequest
        """
        _response = await self._client._request("GET", f"/repos/{owner}/{repo}/pulls/{index}")
        return decode(_response, PullRequest)

    async def update(
        self,
        owner: str,
        repo: str,
        index: int,
        *,
        allow_maintainer_edit: bool | None = None,
        assignee: str | None = None,
        assignees: builtins.list[str] | None = None,
        base: str | None = None,
        body: str | None = None,
        due_date: datetime | None = None,
        labels: builtins.list[int] | None = None,
        milestone: int | None = None,
        state: str | None = None,
        title: str | None = None,
        unset_due_date: bool | None = None,
    ) -> PullRequest:
        """
        Update a pull request. If using deadline only the date will be taken into account, and time of day ignored.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the pull request to edit
            allow_maintainer_edit:
            assignee:
            assignees:
            base:
            body:
            due_date:
            labels:
            milestone:
            state:
            title:
            unset_due_date:

        Returns:
            PullRequest.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.
            ConflictError: 409. APIError is error format response.
            PreconditionFailedError: 412. APIError is error format response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: repoEditPullRequest
        """
        if (
            allow_maintainer_edit is not None
            or assignee is not None
            or assignees is not None
            or base is not None
            or body is not None
            or due_date is not None
            or labels is not None
            or milestone is not None
            or state is not None
            or title is not None
            or unset_due_date is not None
        ):
            _payload = EditPullRequestOption(
                allow_maintainer_edit=allow_maintainer_edit,
                assignee=assignee,
                assignees=assignees,
                base=base,
                body=body,
                due_date=due_date,
                labels=labels,
                milestone=milestone,
                state=state,
                title=title,
                unset_due_date=unset_due_date,
            ).model_dump(mode="json", by_alias=True, exclude_none=True)
        else:
            _payload = None

        _response = await self._client._request("PATCH", f"/repos/{owner}/{repo}/pulls/{index}", json=_payload)
        return decode(_response, PullRequest)

    async def download(
        self,
        owner: str,
        repo: str,
        index: int,
        diff_type: Literal["diff", "patch"],
        *,
        binary: bool | None = None,
    ) -> str:
        """
        Get a pull request diff or patch.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the pull request to get
            diff_type: whether the output is diff or patch
            binary: whether to include binary file changes. if true, the diff is applicable with `git apply`

        Returns:
            APIString is a string response.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoDownloadPullDiffOrPatch
        """
        _query: dict[str, object] = {"binary": binary}

        _response = await self._client._request(
            "GET", f"/repos/{owner}/{repo}/pulls/{index}.{diff_type}", params=_query
        )
        return decode(_response, str)

    async def commits(
        self,
        owner: str,
        repo: str,
        index: int,
        *,
        verification: bool | None = None,
        files: bool | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> AsyncPaginated[Commit]:
        """
        Get commits for a pull request.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the pull request to get
            verification: include verification for every commit (disable for speedup, default 'true')
            files: include a list of affected files for every commit (disable for speedup, default 'true')
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            CommitList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoGetPullRequestCommits
        """
        _query: dict[str, object] = {"verification": verification, "files": files}

        return await self._client._paginate(
            "GET", f"/repos/{owner}/{repo}/pulls/{index}/commits", model=Commit, params=_query, page=page, limit=limit
        )

    async def files(
        self,
        owner: str,
        repo: str,
        index: int,
        *,
        skip_to: str | None = None,
        whitespace: Literal["ignore-all", "ignore-change", "ignore-eol", "show-all"] | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> AsyncPaginated[ChangedFile]:
        """
        Get changed files for a pull request.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the pull request to get
            skip_to: skip to given file
            whitespace: whitespace behavior
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            ChangedFileListWithPagination.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoGetPullRequestFiles
        """
        _query: dict[str, object] = {"skip-to": skip_to, "whitespace": whitespace}

        return await self._client._paginate(
            "GET",
            f"/repos/{owner}/{repo}/pulls/{index}/files",
            model=ChangedFile,
            params=_query,
            page=page,
            limit=limit,
        )

    async def is_merged(self, owner: str, repo: str, index: int) -> None:
        """
        Check if a pull request has been merged.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the pull request

        Returns:
            No content.

        Raises:
            NotFoundError: 404. pull request has not been merged.

        Operation ID: repoPullRequestIsMerged
        """
        _response = await self._client._request("GET", f"/repos/{owner}/{repo}/pulls/{index}/merge")
        return decode(_response, None)

    async def merge(
        self,
        owner: str,
        repo: str,
        index: int,
        *,
        do: MergePullRequestOptionDo,
        merge_commit_id: str | None = None,
        merge_message_field: str | None = None,
        merge_title_field: str | None = None,
        delete_branch_after_merge: bool | None = None,
        force_merge: bool | None = None,
        head_commit_id: str | None = None,
        merge_when_checks_succeed: bool | None = None,
    ) -> None:
        """
        Merge a pull request.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the pull request to merge
            do:
            merge_commit_id:
            merge_message_field:
            merge_title_field:
            delete_branch_after_merge:
            force_merge:
            head_commit_id:
            merge_when_checks_succeed:

        Returns:
            No content.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.
            MethodNotAllowedError: 405. APIEmpty is an empty response.
            ConflictError: 409. APIError is error format response.
            PayloadTooLargeError: 413. QuotaExceeded.
            LockedError: 423. APIRepoArchivedError is an error that is raised when an archived repo should be modified.

        Operation ID: repoMergePullRequest
        """
        _payload = MergePullRequestOption(
            do=do,
            merge_commit_id=merge_commit_id,
            merge_message_field=merge_message_field,
            merge_title_field=merge_title_field,
            delete_branch_after_merge=delete_branch_after_merge,
            force_merge=force_merge,
            head_commit_id=head_commit_id,
            merge_when_checks_succeed=merge_when_checks_succeed,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = await self._client._request("POST", f"/repos/{owner}/{repo}/pulls/{index}/merge", json=_payload)
        return decode(_response, None)

    async def cancel_auto_merge(self, owner: str, repo: str, index: int) -> None:
        """
        Cancel the scheduled auto merge for the given pull request.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the pull request to merge

        Returns:
            No content.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.
            LockedError: 423. APIRepoArchivedError is an error that is raised when an archived repo should be modified.

        Operation ID: repoCancelScheduledAutoMerge
        """
        _response = await self._client._request("DELETE", f"/repos/{owner}/{repo}/pulls/{index}/merge")
        return decode(_response, None)

    async def update_branch(
        self,
        owner: str,
        repo: str,
        index: int,
        *,
        style: Literal["merge", "rebase"] | None = None,
    ) -> None:
        """
        Merge PR's baseBranch into headBranch.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the pull request to get
            style: how to update pull request

        Returns:
            No content.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.
            ConflictError: 409. APIError is error format response.
            PayloadTooLargeError: 413. QuotaExceeded.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: repoUpdatePullRequest
        """
        _query: dict[str, object] = {"style": style}

        _response = await self._client._request("POST", f"/repos/{owner}/{repo}/pulls/{index}/update", params=_query)
        return decode(_response, None)


class ReposPullsRequestedReviewers:
    """The ``repos.pulls.requested_reviewers`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def create(
        self,
        owner: str,
        repo: str,
        index: int,
        *,
        reviewers: builtins.list[str] | None = None,
        team_reviewers: builtins.list[str] | None = None,
    ) -> builtins.list[PullReview]:
        """
        Create review requests for a pull request.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the pull request
            reviewers:
            team_reviewers:

        Returns:
            PullReviewListWithoutPagination - Review requests without pagination headers.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: repoCreatePullReviewRequests
        """
        _payload = PullReviewRequestOptions(
            reviewers=reviewers,
            team_reviewers=team_reviewers,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = self._client._request(
            "POST", f"/repos/{owner}/{repo}/pulls/{index}/requested_reviewers", json=_payload
        )
        return decode(_response, list[PullReview])

    def delete(
        self,
        owner: str,
        repo: str,
        index: int,
        *,
        reviewers: builtins.list[str] | None = None,
        team_reviewers: builtins.list[str] | None = None,
    ) -> None:
        """
        Cancel review requests for a pull request.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the pull request
            reviewers:
            team_reviewers:

        Returns:
            No content.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: repoDeletePullReviewRequests
        """
        _payload = PullReviewRequestOptions(
            reviewers=reviewers,
            team_reviewers=team_reviewers,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = self._client._request(
            "DELETE", f"/repos/{owner}/{repo}/pulls/{index}/requested_reviewers", json=_payload
        )
        return decode(_response, None)


class AsyncReposPullsRequestedReviewers:
    """The ``repos.pulls.requested_reviewers`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def create(
        self,
        owner: str,
        repo: str,
        index: int,
        *,
        reviewers: builtins.list[str] | None = None,
        team_reviewers: builtins.list[str] | None = None,
    ) -> builtins.list[PullReview]:
        """
        Create review requests for a pull request.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the pull request
            reviewers:
            team_reviewers:

        Returns:
            PullReviewListWithoutPagination - Review requests without pagination headers.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: repoCreatePullReviewRequests
        """
        _payload = PullReviewRequestOptions(
            reviewers=reviewers,
            team_reviewers=team_reviewers,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = await self._client._request(
            "POST", f"/repos/{owner}/{repo}/pulls/{index}/requested_reviewers", json=_payload
        )
        return decode(_response, list[PullReview])

    async def delete(
        self,
        owner: str,
        repo: str,
        index: int,
        *,
        reviewers: builtins.list[str] | None = None,
        team_reviewers: builtins.list[str] | None = None,
    ) -> None:
        """
        Cancel review requests for a pull request.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the pull request
            reviewers:
            team_reviewers:

        Returns:
            No content.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: repoDeletePullReviewRequests
        """
        _payload = PullReviewRequestOptions(
            reviewers=reviewers,
            team_reviewers=team_reviewers,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = await self._client._request(
            "DELETE", f"/repos/{owner}/{repo}/pulls/{index}/requested_reviewers", json=_payload
        )
        return decode(_response, None)


class ReposPullsReviews:
    """The ``repos.pulls.reviews`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client
        self.comments: ReposPullsReviewsComments = ReposPullsReviewsComments(client)

    def list(
        self,
        owner: str,
        repo: str,
        index: int,
        *,
        page: int | None = None,
        limit: int | None = None,
    ) -> Paginated[PullReview]:
        """
        List all reviews for a pull request.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the pull request
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            PullReviewList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoListPullReviews
        """
        return self._client._paginate(
            "GET", f"/repos/{owner}/{repo}/pulls/{index}/reviews", model=PullReview, page=page, limit=limit
        )

    def create(
        self,
        owner: str,
        repo: str,
        index: int,
        *,
        body: str | None = None,
        comments: builtins.list[CreatePullReviewComment] | None = None,
        commit_id: str | None = None,
        event: str | None = None,
    ) -> PullReview:
        """
        Create a review to an pull request.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the pull request
            body:
            comments:
            commit_id:
            event:

        Returns:
            PullReview.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: repoCreatePullReview
        """
        _payload = CreatePullReviewOptions(
            body=body,
            comments=comments,
            commit_id=commit_id,
            event=event,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = self._client._request("POST", f"/repos/{owner}/{repo}/pulls/{index}/reviews", json=_payload)
        return decode(_response, PullReview)

    def get(self, owner: str, repo: str, index: int, id: int) -> PullReview:
        """
        Get a specific review for a pull request.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the pull request
            id: id of the review

        Returns:
            PullReview.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoGetPullReview
        """
        _response = self._client._request("GET", f"/repos/{owner}/{repo}/pulls/{index}/reviews/{id}")
        return decode(_response, PullReview)

    def submit(
        self,
        owner: str,
        repo: str,
        index: int,
        id: int,
        *,
        body: str | None = None,
        event: str | None = None,
    ) -> PullReview:
        """
        Submit a pending review to an pull request.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the pull request
            id: id of the review
            body:
            event:

        Returns:
            PullReview.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: repoSubmitPullReview
        """
        _payload = SubmitPullReviewOptions(
            body=body,
            event=event,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = self._client._request("POST", f"/repos/{owner}/{repo}/pulls/{index}/reviews/{id}", json=_payload)
        return decode(_response, PullReview)

    def delete(self, owner: str, repo: str, index: int, id: int) -> None:
        """
        Delete a specific review from a pull request.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the pull request
            id: id of the review

        Returns:
            No content.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoDeletePullReview
        """
        _response = self._client._request("DELETE", f"/repos/{owner}/{repo}/pulls/{index}/reviews/{id}")
        return decode(_response, None)

    def dismiss(
        self,
        owner: str,
        repo: str,
        index: int,
        id: int,
        *,
        message: str | None = None,
        priors: bool | None = None,
    ) -> PullReview:
        """
        Dismiss a review for a pull request.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the pull request
            id: id of the review
            message:
            priors:

        Returns:
            PullReview.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: repoDismissPullReview
        """
        _payload = DismissPullReviewOptions(
            message=message,
            priors=priors,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = self._client._request(
            "POST", f"/repos/{owner}/{repo}/pulls/{index}/reviews/{id}/dismissals", json=_payload
        )
        return decode(_response, PullReview)

    def undismiss(self, owner: str, repo: str, index: int, id: int) -> PullReview:
        """
        Cancel to dismiss a review for a pull request.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the pull request
            id: id of the review

        Returns:
            PullReview.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: repoUnDismissPullReview
        """
        _response = self._client._request("POST", f"/repos/{owner}/{repo}/pulls/{index}/reviews/{id}/undismissals")
        return decode(_response, PullReview)


class AsyncReposPullsReviews:
    """The ``repos.pulls.reviews`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client
        self.comments: AsyncReposPullsReviewsComments = AsyncReposPullsReviewsComments(client)

    async def list(
        self,
        owner: str,
        repo: str,
        index: int,
        *,
        page: int | None = None,
        limit: int | None = None,
    ) -> AsyncPaginated[PullReview]:
        """
        List all reviews for a pull request.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the pull request
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            PullReviewList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoListPullReviews
        """
        return await self._client._paginate(
            "GET", f"/repos/{owner}/{repo}/pulls/{index}/reviews", model=PullReview, page=page, limit=limit
        )

    async def create(
        self,
        owner: str,
        repo: str,
        index: int,
        *,
        body: str | None = None,
        comments: builtins.list[CreatePullReviewComment] | None = None,
        commit_id: str | None = None,
        event: str | None = None,
    ) -> PullReview:
        """
        Create a review to an pull request.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the pull request
            body:
            comments:
            commit_id:
            event:

        Returns:
            PullReview.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: repoCreatePullReview
        """
        _payload = CreatePullReviewOptions(
            body=body,
            comments=comments,
            commit_id=commit_id,
            event=event,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = await self._client._request("POST", f"/repos/{owner}/{repo}/pulls/{index}/reviews", json=_payload)
        return decode(_response, PullReview)

    async def get(self, owner: str, repo: str, index: int, id: int) -> PullReview:
        """
        Get a specific review for a pull request.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the pull request
            id: id of the review

        Returns:
            PullReview.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoGetPullReview
        """
        _response = await self._client._request("GET", f"/repos/{owner}/{repo}/pulls/{index}/reviews/{id}")
        return decode(_response, PullReview)

    async def submit(
        self,
        owner: str,
        repo: str,
        index: int,
        id: int,
        *,
        body: str | None = None,
        event: str | None = None,
    ) -> PullReview:
        """
        Submit a pending review to an pull request.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the pull request
            id: id of the review
            body:
            event:

        Returns:
            PullReview.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: repoSubmitPullReview
        """
        _payload = SubmitPullReviewOptions(
            body=body,
            event=event,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = await self._client._request(
            "POST", f"/repos/{owner}/{repo}/pulls/{index}/reviews/{id}", json=_payload
        )
        return decode(_response, PullReview)

    async def delete(self, owner: str, repo: str, index: int, id: int) -> None:
        """
        Delete a specific review from a pull request.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the pull request
            id: id of the review

        Returns:
            No content.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoDeletePullReview
        """
        _response = await self._client._request("DELETE", f"/repos/{owner}/{repo}/pulls/{index}/reviews/{id}")
        return decode(_response, None)

    async def dismiss(
        self,
        owner: str,
        repo: str,
        index: int,
        id: int,
        *,
        message: str | None = None,
        priors: bool | None = None,
    ) -> PullReview:
        """
        Dismiss a review for a pull request.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the pull request
            id: id of the review
            message:
            priors:

        Returns:
            PullReview.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: repoDismissPullReview
        """
        _payload = DismissPullReviewOptions(
            message=message,
            priors=priors,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = await self._client._request(
            "POST", f"/repos/{owner}/{repo}/pulls/{index}/reviews/{id}/dismissals", json=_payload
        )
        return decode(_response, PullReview)

    async def undismiss(self, owner: str, repo: str, index: int, id: int) -> PullReview:
        """
        Cancel to dismiss a review for a pull request.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the pull request
            id: id of the review

        Returns:
            PullReview.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: repoUnDismissPullReview
        """
        _response = await self._client._request(
            "POST", f"/repos/{owner}/{repo}/pulls/{index}/reviews/{id}/undismissals"
        )
        return decode(_response, PullReview)


class ReposPullsReviewsComments:
    """The ``repos.pulls.reviews.comments`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def list(self, owner: str, repo: str, index: int, id: int) -> builtins.list[PullReviewComment]:
        """
        Get a specific review for a pull request.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the pull request
            id: id of the review

        Returns:
            PullCommentList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoGetPullReviewComments
        """
        _response = self._client._request("GET", f"/repos/{owner}/{repo}/pulls/{index}/reviews/{id}/comments")
        return decode(_response, list[PullReviewComment])

    def create(
        self,
        owner: str,
        repo: str,
        index: int,
        id: int,
        *,
        body: str | None = None,
        extra_lines_count: int | None = None,
        new_position: int | None = None,
        old_position: int | None = None,
        path: str | None = None,
    ) -> PullReviewComment:
        """
        Add a new comment to a pull request review.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the pull request
            id: id of the review
            body:
            extra_lines_count: number of additional lines after the commented line (0 = single line comment)
            new_position: if comment to new file line or 0
            old_position: if comment to old file line or 0
            path: the tree path

        Returns:
            PullComment.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: repoCreatePullReviewComment
        """
        _payload = CreatePullReviewComment(
            body=body,
            extra_lines_count=extra_lines_count,
            new_position=new_position,
            old_position=old_position,
            path=path,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = self._client._request(
            "POST", f"/repos/{owner}/{repo}/pulls/{index}/reviews/{id}/comments", json=_payload
        )
        return decode(_response, PullReviewComment)

    def get(self, owner: str, repo: str, index: int, id: int, comment: int) -> PullReviewComment:
        """
        Get a pull review comment.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the pull request
            id: id of the review
            comment: id of the comment

        Returns:
            PullComment.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoGetPullReviewComment
        """
        _response = self._client._request("GET", f"/repos/{owner}/{repo}/pulls/{index}/reviews/{id}/comments/{comment}")
        return decode(_response, PullReviewComment)

    def delete(self, owner: str, repo: str, index: int, id: int, comment: int) -> None:
        """
        Delete a pull review comment.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the pull request
            id: id of the review
            comment: id of the comment

        Returns:
            No content.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoDeletePullReviewComment
        """
        _response = self._client._request(
            "DELETE", f"/repos/{owner}/{repo}/pulls/{index}/reviews/{id}/comments/{comment}"
        )
        return decode(_response, None)


class AsyncReposPullsReviewsComments:
    """The ``repos.pulls.reviews.comments`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def list(self, owner: str, repo: str, index: int, id: int) -> builtins.list[PullReviewComment]:
        """
        Get a specific review for a pull request.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the pull request
            id: id of the review

        Returns:
            PullCommentList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoGetPullReviewComments
        """
        _response = await self._client._request("GET", f"/repos/{owner}/{repo}/pulls/{index}/reviews/{id}/comments")
        return decode(_response, list[PullReviewComment])

    async def create(
        self,
        owner: str,
        repo: str,
        index: int,
        id: int,
        *,
        body: str | None = None,
        extra_lines_count: int | None = None,
        new_position: int | None = None,
        old_position: int | None = None,
        path: str | None = None,
    ) -> PullReviewComment:
        """
        Add a new comment to a pull request review.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the pull request
            id: id of the review
            body:
            extra_lines_count: number of additional lines after the commented line (0 = single line comment)
            new_position: if comment to new file line or 0
            old_position: if comment to old file line or 0
            path: the tree path

        Returns:
            PullComment.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: repoCreatePullReviewComment
        """
        _payload = CreatePullReviewComment(
            body=body,
            extra_lines_count=extra_lines_count,
            new_position=new_position,
            old_position=old_position,
            path=path,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = await self._client._request(
            "POST", f"/repos/{owner}/{repo}/pulls/{index}/reviews/{id}/comments", json=_payload
        )
        return decode(_response, PullReviewComment)

    async def get(self, owner: str, repo: str, index: int, id: int, comment: int) -> PullReviewComment:
        """
        Get a pull review comment.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the pull request
            id: id of the review
            comment: id of the comment

        Returns:
            PullComment.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoGetPullReviewComment
        """
        _response = await self._client._request(
            "GET", f"/repos/{owner}/{repo}/pulls/{index}/reviews/{id}/comments/{comment}"
        )
        return decode(_response, PullReviewComment)

    async def delete(self, owner: str, repo: str, index: int, id: int, comment: int) -> None:
        """
        Delete a pull review comment.

        Args:
            owner: owner of the repo
            repo: name of the repo
            index: index of the pull request
            id: id of the review
            comment: id of the comment

        Returns:
            No content.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoDeletePullReviewComment
        """
        _response = await self._client._request(
            "DELETE", f"/repos/{owner}/{repo}/pulls/{index}/reviews/{id}/comments/{comment}"
        )
        return decode(_response, None)


class ReposPushMirrors:
    """The ``repos.push_mirrors`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def list(
        self,
        owner: str,
        repo: str,
        *,
        page: int | None = None,
        limit: int | None = None,
    ) -> Paginated[PushMirror]:
        """
        Get all push mirrors of the repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            PushMirrorList.

        Raises:
            BadRequestError: 400. APIError is error format response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoListPushMirrors
        """
        return self._client._paginate(
            "GET", f"/repos/{owner}/{repo}/push_mirrors", model=PushMirror, page=page, limit=limit
        )

    def create(
        self,
        owner: str,
        repo: str,
        *,
        branch_filter: str | None = None,
        interval: str | None = None,
        remote_address: str | None = None,
        remote_password: str | None = None,
        remote_username: str | None = None,
        sync_on_commit: bool | None = None,
        use_ssh: bool | None = None,
    ) -> PushMirror:
        """
        Set up a new push mirror in a repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            branch_filter:
            interval:
            remote_address:
            remote_password:
            remote_username:
            sync_on_commit:
            use_ssh:

        Returns:
            PushMirror.

        Raises:
            BadRequestError: 400. APIError is error format response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.
            PayloadTooLargeError: 413. QuotaExceeded.

        Operation ID: repoAddPushMirror
        """
        if (
            branch_filter is not None
            or interval is not None
            or remote_address is not None
            or remote_password is not None
            or remote_username is not None
            or sync_on_commit is not None
            or use_ssh is not None
        ):
            _payload = CreatePushMirrorOption(
                branch_filter=branch_filter,
                interval=interval,
                remote_address=remote_address,
                remote_password=remote_password,
                remote_username=remote_username,
                sync_on_commit=sync_on_commit,
                use_ssh=use_ssh,
            ).model_dump(mode="json", by_alias=True, exclude_none=True)
        else:
            _payload = None

        _response = self._client._request("POST", f"/repos/{owner}/{repo}/push_mirrors", json=_payload)
        return decode(_response, PushMirror)

    def get(self, owner: str, repo: str, name: str) -> PushMirror:
        """
        Get push mirror of the repository by remoteName.

        Args:
            owner: owner of the repo
            repo: name of the repo
            name: remote name of push mirror

        Returns:
            PushMirror.

        Raises:
            BadRequestError: 400. APIError is error format response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoGetPushMirrorByRemoteName
        """
        _response = self._client._request("GET", f"/repos/{owner}/{repo}/push_mirrors/{name}")
        return decode(_response, PushMirror)

    def delete(self, owner: str, repo: str, name: str) -> None:
        """
        Remove a push mirror from a repository by remoteName.

        Args:
            owner: owner of the repo
            repo: name of the repo
            name: remote name of the pushMirror

        Returns:
            No content.

        Raises:
            BadRequestError: 400. APIError is error format response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoDeletePushMirror
        """
        _response = self._client._request("DELETE", f"/repos/{owner}/{repo}/push_mirrors/{name}")
        return decode(_response, None)


class AsyncReposPushMirrors:
    """The ``repos.push_mirrors`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def list(
        self,
        owner: str,
        repo: str,
        *,
        page: int | None = None,
        limit: int | None = None,
    ) -> AsyncPaginated[PushMirror]:
        """
        Get all push mirrors of the repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            PushMirrorList.

        Raises:
            BadRequestError: 400. APIError is error format response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoListPushMirrors
        """
        return await self._client._paginate(
            "GET", f"/repos/{owner}/{repo}/push_mirrors", model=PushMirror, page=page, limit=limit
        )

    async def create(
        self,
        owner: str,
        repo: str,
        *,
        branch_filter: str | None = None,
        interval: str | None = None,
        remote_address: str | None = None,
        remote_password: str | None = None,
        remote_username: str | None = None,
        sync_on_commit: bool | None = None,
        use_ssh: bool | None = None,
    ) -> PushMirror:
        """
        Set up a new push mirror in a repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            branch_filter:
            interval:
            remote_address:
            remote_password:
            remote_username:
            sync_on_commit:
            use_ssh:

        Returns:
            PushMirror.

        Raises:
            BadRequestError: 400. APIError is error format response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.
            PayloadTooLargeError: 413. QuotaExceeded.

        Operation ID: repoAddPushMirror
        """
        if (
            branch_filter is not None
            or interval is not None
            or remote_address is not None
            or remote_password is not None
            or remote_username is not None
            or sync_on_commit is not None
            or use_ssh is not None
        ):
            _payload = CreatePushMirrorOption(
                branch_filter=branch_filter,
                interval=interval,
                remote_address=remote_address,
                remote_password=remote_password,
                remote_username=remote_username,
                sync_on_commit=sync_on_commit,
                use_ssh=use_ssh,
            ).model_dump(mode="json", by_alias=True, exclude_none=True)
        else:
            _payload = None

        _response = await self._client._request("POST", f"/repos/{owner}/{repo}/push_mirrors", json=_payload)
        return decode(_response, PushMirror)

    async def get(self, owner: str, repo: str, name: str) -> PushMirror:
        """
        Get push mirror of the repository by remoteName.

        Args:
            owner: owner of the repo
            repo: name of the repo
            name: remote name of push mirror

        Returns:
            PushMirror.

        Raises:
            BadRequestError: 400. APIError is error format response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoGetPushMirrorByRemoteName
        """
        _response = await self._client._request("GET", f"/repos/{owner}/{repo}/push_mirrors/{name}")
        return decode(_response, PushMirror)

    async def delete(self, owner: str, repo: str, name: str) -> None:
        """
        Remove a push mirror from a repository by remoteName.

        Args:
            owner: owner of the repo
            repo: name of the repo
            name: remote name of the pushMirror

        Returns:
            No content.

        Raises:
            BadRequestError: 400. APIError is error format response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoDeletePushMirror
        """
        _response = await self._client._request("DELETE", f"/repos/{owner}/{repo}/push_mirrors/{name}")
        return decode(_response, None)


class ReposRaw:
    """The ``repos.raw`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def get(self, owner: str, repo: str, filepath: str, *, ref: str | None = None) -> bytes:
        """
        Get a file from a repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            filepath: filepath of the file to get
            ref: The name of the commit/branch/tag. Default the repository's default branch (usually master)

        Returns:
            Returns raw file content.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoGetRawFile
        """
        _query: dict[str, object] = {"ref": ref}

        _response = self._client._request("GET", f"/repos/{owner}/{repo}/raw/{filepath}", params=_query)
        return decode(_response, bytes)


class AsyncReposRaw:
    """The ``repos.raw`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def get(self, owner: str, repo: str, filepath: str, *, ref: str | None = None) -> bytes:
        """
        Get a file from a repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            filepath: filepath of the file to get
            ref: The name of the commit/branch/tag. Default the repository's default branch (usually master)

        Returns:
            Returns raw file content.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoGetRawFile
        """
        _query: dict[str, object] = {"ref": ref}

        _response = await self._client._request("GET", f"/repos/{owner}/{repo}/raw/{filepath}", params=_query)
        return decode(_response, bytes)


class ReposReleases:
    """The ``repos.releases`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client
        self.assets: ReposReleasesAssets = ReposReleasesAssets(client)
        self.tags: ReposReleasesTags = ReposReleasesTags(client)

    def list(
        self,
        owner: str,
        repo: str,
        *,
        draft: bool | None = None,
        pre_release: bool | None = None,
        q: str | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> Paginated[Release]:
        """
        List a repo's releases.

        Args:
            owner: owner of the repo
            repo: name of the repo
            draft: filter (exclude / include) drafts, if you dont have repo write access none will show
            pre_release: filter (exclude / include) pre-releases
            q: Search string
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            ReleaseList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoListReleases
        """
        _query: dict[str, object] = {"draft": draft, "pre-release": pre_release, "q": q}

        return self._client._paginate(
            "GET", f"/repos/{owner}/{repo}/releases", model=Release, params=_query, page=page, limit=limit
        )

    def create(
        self,
        owner: str,
        repo: str,
        *,
        body: str | None = None,
        draft: bool | None = None,
        hide_archive_links: bool | None = None,
        name: str | None = None,
        prerelease: bool | None = None,
        tag_name: str,
        target_commitish: str | None = None,
    ) -> Release:
        """
        Create a release.

        Args:
            owner: owner of the repo
            repo: name of the repo
            body:
            draft:
            hide_archive_links:
            name:
            prerelease:
            tag_name:
            target_commitish:

        Returns:
            Release.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.
            ConflictError: 409. APIError is error format response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: repoCreateRelease
        """
        _payload = CreateReleaseOption(
            body=body,
            draft=draft,
            hide_archive_links=hide_archive_links,
            name=name,
            prerelease=prerelease,
            tag_name=tag_name,
            target_commitish=target_commitish,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = self._client._request("POST", f"/repos/{owner}/{repo}/releases", json=_payload)
        return decode(_response, Release)

    def latest(self, owner: str, repo: str) -> Release:
        """
        Gets the most recent non-prerelease, non-draft release of a repository, sorted by created_at.

        Args:
            owner: owner of the repo
            repo: name of the repo

        Returns:
            Release.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoGetLatestRelease
        """
        _response = self._client._request("GET", f"/repos/{owner}/{repo}/releases/latest")
        return decode(_response, Release)

    def get(self, owner: str, repo: str, id: int) -> Release:
        """
        Get a release.

        Args:
            owner: owner of the repo
            repo: name of the repo
            id: id of the release to get

        Returns:
            Release.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoGetRelease
        """
        _response = self._client._request("GET", f"/repos/{owner}/{repo}/releases/{id}")
        return decode(_response, Release)

    def update(
        self,
        owner: str,
        repo: str,
        id: int,
        *,
        body: str | None = None,
        draft: bool | None = None,
        hide_archive_links: bool | None = None,
        name: str | None = None,
        prerelease: bool | None = None,
        tag_name: str | None = None,
        target_commitish: str | None = None,
    ) -> Release:
        """
        Update a release.

        Args:
            owner: owner of the repo
            repo: name of the repo
            id: id of the release to edit
            body:
            draft:
            hide_archive_links:
            name:
            prerelease:
            tag_name:
            target_commitish:

        Returns:
            Release.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoEditRelease
        """
        if (
            body is not None
            or draft is not None
            or hide_archive_links is not None
            or name is not None
            or prerelease is not None
            or tag_name is not None
            or target_commitish is not None
        ):
            _payload = EditReleaseOption(
                body=body,
                draft=draft,
                hide_archive_links=hide_archive_links,
                name=name,
                prerelease=prerelease,
                tag_name=tag_name,
                target_commitish=target_commitish,
            ).model_dump(mode="json", by_alias=True, exclude_none=True)
        else:
            _payload = None

        _response = self._client._request("PATCH", f"/repos/{owner}/{repo}/releases/{id}", json=_payload)
        return decode(_response, Release)

    def delete(self, owner: str, repo: str, id: int) -> None:
        """
        Delete a release.

        Args:
            owner: owner of the repo
            repo: name of the repo
            id: id of the release to delete

        Returns:
            No content.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: repoDeleteRelease
        """
        _response = self._client._request("DELETE", f"/repos/{owner}/{repo}/releases/{id}")
        return decode(_response, None)


class AsyncReposReleases:
    """The ``repos.releases`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client
        self.assets: AsyncReposReleasesAssets = AsyncReposReleasesAssets(client)
        self.tags: AsyncReposReleasesTags = AsyncReposReleasesTags(client)

    async def list(
        self,
        owner: str,
        repo: str,
        *,
        draft: bool | None = None,
        pre_release: bool | None = None,
        q: str | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> AsyncPaginated[Release]:
        """
        List a repo's releases.

        Args:
            owner: owner of the repo
            repo: name of the repo
            draft: filter (exclude / include) drafts, if you dont have repo write access none will show
            pre_release: filter (exclude / include) pre-releases
            q: Search string
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            ReleaseList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoListReleases
        """
        _query: dict[str, object] = {"draft": draft, "pre-release": pre_release, "q": q}

        return await self._client._paginate(
            "GET", f"/repos/{owner}/{repo}/releases", model=Release, params=_query, page=page, limit=limit
        )

    async def create(
        self,
        owner: str,
        repo: str,
        *,
        body: str | None = None,
        draft: bool | None = None,
        hide_archive_links: bool | None = None,
        name: str | None = None,
        prerelease: bool | None = None,
        tag_name: str,
        target_commitish: str | None = None,
    ) -> Release:
        """
        Create a release.

        Args:
            owner: owner of the repo
            repo: name of the repo
            body:
            draft:
            hide_archive_links:
            name:
            prerelease:
            tag_name:
            target_commitish:

        Returns:
            Release.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.
            ConflictError: 409. APIError is error format response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: repoCreateRelease
        """
        _payload = CreateReleaseOption(
            body=body,
            draft=draft,
            hide_archive_links=hide_archive_links,
            name=name,
            prerelease=prerelease,
            tag_name=tag_name,
            target_commitish=target_commitish,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = await self._client._request("POST", f"/repos/{owner}/{repo}/releases", json=_payload)
        return decode(_response, Release)

    async def latest(self, owner: str, repo: str) -> Release:
        """
        Gets the most recent non-prerelease, non-draft release of a repository, sorted by created_at.

        Args:
            owner: owner of the repo
            repo: name of the repo

        Returns:
            Release.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoGetLatestRelease
        """
        _response = await self._client._request("GET", f"/repos/{owner}/{repo}/releases/latest")
        return decode(_response, Release)

    async def get(self, owner: str, repo: str, id: int) -> Release:
        """
        Get a release.

        Args:
            owner: owner of the repo
            repo: name of the repo
            id: id of the release to get

        Returns:
            Release.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoGetRelease
        """
        _response = await self._client._request("GET", f"/repos/{owner}/{repo}/releases/{id}")
        return decode(_response, Release)

    async def update(
        self,
        owner: str,
        repo: str,
        id: int,
        *,
        body: str | None = None,
        draft: bool | None = None,
        hide_archive_links: bool | None = None,
        name: str | None = None,
        prerelease: bool | None = None,
        tag_name: str | None = None,
        target_commitish: str | None = None,
    ) -> Release:
        """
        Update a release.

        Args:
            owner: owner of the repo
            repo: name of the repo
            id: id of the release to edit
            body:
            draft:
            hide_archive_links:
            name:
            prerelease:
            tag_name:
            target_commitish:

        Returns:
            Release.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoEditRelease
        """
        if (
            body is not None
            or draft is not None
            or hide_archive_links is not None
            or name is not None
            or prerelease is not None
            or tag_name is not None
            or target_commitish is not None
        ):
            _payload = EditReleaseOption(
                body=body,
                draft=draft,
                hide_archive_links=hide_archive_links,
                name=name,
                prerelease=prerelease,
                tag_name=tag_name,
                target_commitish=target_commitish,
            ).model_dump(mode="json", by_alias=True, exclude_none=True)
        else:
            _payload = None

        _response = await self._client._request("PATCH", f"/repos/{owner}/{repo}/releases/{id}", json=_payload)
        return decode(_response, Release)

    async def delete(self, owner: str, repo: str, id: int) -> None:
        """
        Delete a release.

        Args:
            owner: owner of the repo
            repo: name of the repo
            id: id of the release to delete

        Returns:
            No content.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: repoDeleteRelease
        """
        _response = await self._client._request("DELETE", f"/repos/{owner}/{repo}/releases/{id}")
        return decode(_response, None)


class ReposReleasesAssets:
    """The ``repos.releases.assets`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def list(self, owner: str, repo: str, id: int) -> builtins.list[Attachment]:
        """
        List release's attachments.

        Args:
            owner: owner of the repo
            repo: name of the repo
            id: id of the release

        Returns:
            AttachmentList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoListReleaseAttachments
        """
        _response = self._client._request("GET", f"/repos/{owner}/{repo}/releases/{id}/assets")
        return decode(_response, list[Attachment])

    def create(
        self,
        owner: str,
        repo: str,
        id: int,
        *,
        name: str | None = None,
        attachment: FilePart | None = None,
        external_url: str | None = None,
    ) -> Attachment:
        """
        Create a release attachment.

        Args:
            owner: owner of the repo
            repo: name of the repo
            id: id of the release
            name: name of the attachment
            attachment: attachment to upload (this parameter is incompatible with `external_url`)
            external_url: url to external asset (this parameter is incompatible with `attachment`)

        Returns:
            Attachment.

        Raises:
            BadRequestError: 400. APIError is error format response.
            NotFoundError: 404. APINotFound is a not found error response.
            PayloadTooLargeError: 413. QuotaExceeded.

        Operation ID: repoCreateReleaseAttachment
        """
        _query: dict[str, object] = {"name": name}

        _files: dict[str, object] = {}
        if attachment is not None:
            _files["attachment"] = attachment
        _form: dict[str, object] = {}
        if external_url is not None:
            _form["external_url"] = external_url

        _response = self._client._request(
            "POST", f"/repos/{owner}/{repo}/releases/{id}/assets", params=_query, files=_files, data=_form
        )
        return decode(_response, Attachment)

    def get(self, owner: str, repo: str, id: int, attachment_id: int) -> Attachment:
        """
        Get a release attachment.

        Args:
            owner: owner of the repo
            repo: name of the repo
            id: id of the release
            attachment_id: id of the attachment to get

        Returns:
            Attachment.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoGetReleaseAttachment
        """
        _response = self._client._request("GET", f"/repos/{owner}/{repo}/releases/{id}/assets/{attachment_id}")
        return decode(_response, Attachment)

    def update(
        self,
        owner: str,
        repo: str,
        id: int,
        attachment_id: int,
        *,
        browser_download_url: str | None = None,
        name: str | None = None,
    ) -> Attachment:
        """
        Edit a release attachment.

        Args:
            owner: owner of the repo
            repo: name of the repo
            id: id of the release
            attachment_id: id of the attachment to edit
            browser_download_url: (Can only be set if existing attachment is of external type)
            name:

        Returns:
            Attachment.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.
            PayloadTooLargeError: 413. QuotaExceeded.

        Operation ID: repoEditReleaseAttachment
        """
        if browser_download_url is not None or name is not None:
            _payload = EditAttachmentOptions(browser_download_url=browser_download_url, name=name).model_dump(
                mode="json", by_alias=True, exclude_none=True
            )
        else:
            _payload = None

        _response = self._client._request(
            "PATCH", f"/repos/{owner}/{repo}/releases/{id}/assets/{attachment_id}", json=_payload
        )
        return decode(_response, Attachment)

    def delete(self, owner: str, repo: str, id: int, attachment_id: int) -> None:
        """
        Delete a release attachment.

        Args:
            owner: owner of the repo
            repo: name of the repo
            id: id of the release
            attachment_id: id of the attachment to delete

        Returns:
            No content.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoDeleteReleaseAttachment
        """
        _response = self._client._request("DELETE", f"/repos/{owner}/{repo}/releases/{id}/assets/{attachment_id}")
        return decode(_response, None)


class AsyncReposReleasesAssets:
    """The ``repos.releases.assets`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def list(self, owner: str, repo: str, id: int) -> builtins.list[Attachment]:
        """
        List release's attachments.

        Args:
            owner: owner of the repo
            repo: name of the repo
            id: id of the release

        Returns:
            AttachmentList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoListReleaseAttachments
        """
        _response = await self._client._request("GET", f"/repos/{owner}/{repo}/releases/{id}/assets")
        return decode(_response, list[Attachment])

    async def create(
        self,
        owner: str,
        repo: str,
        id: int,
        *,
        name: str | None = None,
        attachment: FilePart | None = None,
        external_url: str | None = None,
    ) -> Attachment:
        """
        Create a release attachment.

        Args:
            owner: owner of the repo
            repo: name of the repo
            id: id of the release
            name: name of the attachment
            attachment: attachment to upload (this parameter is incompatible with `external_url`)
            external_url: url to external asset (this parameter is incompatible with `attachment`)

        Returns:
            Attachment.

        Raises:
            BadRequestError: 400. APIError is error format response.
            NotFoundError: 404. APINotFound is a not found error response.
            PayloadTooLargeError: 413. QuotaExceeded.

        Operation ID: repoCreateReleaseAttachment
        """
        _query: dict[str, object] = {"name": name}

        _files: dict[str, object] = {}
        if attachment is not None:
            _files["attachment"] = attachment
        _form: dict[str, object] = {}
        if external_url is not None:
            _form["external_url"] = external_url

        _response = await self._client._request(
            "POST", f"/repos/{owner}/{repo}/releases/{id}/assets", params=_query, files=_files, data=_form
        )
        return decode(_response, Attachment)

    async def get(self, owner: str, repo: str, id: int, attachment_id: int) -> Attachment:
        """
        Get a release attachment.

        Args:
            owner: owner of the repo
            repo: name of the repo
            id: id of the release
            attachment_id: id of the attachment to get

        Returns:
            Attachment.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoGetReleaseAttachment
        """
        _response = await self._client._request("GET", f"/repos/{owner}/{repo}/releases/{id}/assets/{attachment_id}")
        return decode(_response, Attachment)

    async def update(
        self,
        owner: str,
        repo: str,
        id: int,
        attachment_id: int,
        *,
        browser_download_url: str | None = None,
        name: str | None = None,
    ) -> Attachment:
        """
        Edit a release attachment.

        Args:
            owner: owner of the repo
            repo: name of the repo
            id: id of the release
            attachment_id: id of the attachment to edit
            browser_download_url: (Can only be set if existing attachment is of external type)
            name:

        Returns:
            Attachment.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.
            PayloadTooLargeError: 413. QuotaExceeded.

        Operation ID: repoEditReleaseAttachment
        """
        if browser_download_url is not None or name is not None:
            _payload = EditAttachmentOptions(browser_download_url=browser_download_url, name=name).model_dump(
                mode="json", by_alias=True, exclude_none=True
            )
        else:
            _payload = None

        _response = await self._client._request(
            "PATCH", f"/repos/{owner}/{repo}/releases/{id}/assets/{attachment_id}", json=_payload
        )
        return decode(_response, Attachment)

    async def delete(self, owner: str, repo: str, id: int, attachment_id: int) -> None:
        """
        Delete a release attachment.

        Args:
            owner: owner of the repo
            repo: name of the repo
            id: id of the release
            attachment_id: id of the attachment to delete

        Returns:
            No content.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoDeleteReleaseAttachment
        """
        _response = await self._client._request("DELETE", f"/repos/{owner}/{repo}/releases/{id}/assets/{attachment_id}")
        return decode(_response, None)


class ReposReleasesTags:
    """The ``repos.releases.tags`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def get(self, owner: str, repo: str, tag: str) -> Release:
        """
        Get a release by tag name.

        Args:
            owner: owner of the repo
            repo: name of the repo
            tag: tag name of the release to get

        Returns:
            Release.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoGetReleaseByTag
        """
        _response = self._client._request("GET", f"/repos/{owner}/{repo}/releases/tags/{tag}")
        return decode(_response, Release)

    def delete(self, owner: str, repo: str, tag: str) -> None:
        """
        Delete a release by tag name.

        Args:
            owner: owner of the repo
            repo: name of the repo
            tag: tag name of the release to delete

        Returns:
            No content.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: repoDeleteReleaseByTag
        """
        _response = self._client._request("DELETE", f"/repos/{owner}/{repo}/releases/tags/{tag}")
        return decode(_response, None)


class AsyncReposReleasesTags:
    """The ``repos.releases.tags`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def get(self, owner: str, repo: str, tag: str) -> Release:
        """
        Get a release by tag name.

        Args:
            owner: owner of the repo
            repo: name of the repo
            tag: tag name of the release to get

        Returns:
            Release.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoGetReleaseByTag
        """
        _response = await self._client._request("GET", f"/repos/{owner}/{repo}/releases/tags/{tag}")
        return decode(_response, Release)

    async def delete(self, owner: str, repo: str, tag: str) -> None:
        """
        Delete a release by tag name.

        Args:
            owner: owner of the repo
            repo: name of the repo
            tag: tag name of the release to delete

        Returns:
            No content.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: repoDeleteReleaseByTag
        """
        _response = await self._client._request("DELETE", f"/repos/{owner}/{repo}/releases/tags/{tag}")
        return decode(_response, None)


class ReposStatuses:
    """The ``repos.statuses`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def list(
        self,
        owner: str,
        repo: str,
        sha: str,
        *,
        sort: Literal["oldest", "recentupdate", "leastupdate", "leastindex", "highestindex"] | None = None,
        state: Literal["pending", "success", "error", "failure", "warning"] | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> Paginated[CommitStatus]:
        """
        Get a commit's statuses.

        Args:
            owner: owner of the repo
            repo: name of the repo
            sha: sha of the commit
            sort: type of sort
            state: type of state
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            CommitStatusList.

        Raises:
            BadRequestError: 400. APIError is error format response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoListStatuses
        """
        _query: dict[str, object] = {"sort": sort, "state": state}

        return self._client._paginate(
            "GET", f"/repos/{owner}/{repo}/statuses/{sha}", model=CommitStatus, params=_query, page=page, limit=limit
        )

    def create(
        self,
        owner: str,
        repo: str,
        sha: str,
        *,
        context: str | None = None,
        description: str | None = None,
        state: str | None = None,
        target_url: str | None = None,
    ) -> CommitStatus:
        """
        Create a commit status.

        Args:
            owner: owner of the repo
            repo: name of the repo
            sha: sha of the commit
            context:
            description:
            state:
            target_url:

        Returns:
            CommitStatus.

        Raises:
            BadRequestError: 400. APIError is error format response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoCreateStatus
        """
        if context is not None or description is not None or state is not None or target_url is not None:
            _payload = CreateStatusOption(
                context=context, description=description, state=state, target_url=target_url
            ).model_dump(mode="json", by_alias=True, exclude_none=True)
        else:
            _payload = None

        _response = self._client._request("POST", f"/repos/{owner}/{repo}/statuses/{sha}", json=_payload)
        return decode(_response, CommitStatus)


class AsyncReposStatuses:
    """The ``repos.statuses`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def list(
        self,
        owner: str,
        repo: str,
        sha: str,
        *,
        sort: Literal["oldest", "recentupdate", "leastupdate", "leastindex", "highestindex"] | None = None,
        state: Literal["pending", "success", "error", "failure", "warning"] | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> AsyncPaginated[CommitStatus]:
        """
        Get a commit's statuses.

        Args:
            owner: owner of the repo
            repo: name of the repo
            sha: sha of the commit
            sort: type of sort
            state: type of state
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            CommitStatusList.

        Raises:
            BadRequestError: 400. APIError is error format response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoListStatuses
        """
        _query: dict[str, object] = {"sort": sort, "state": state}

        return await self._client._paginate(
            "GET", f"/repos/{owner}/{repo}/statuses/{sha}", model=CommitStatus, params=_query, page=page, limit=limit
        )

    async def create(
        self,
        owner: str,
        repo: str,
        sha: str,
        *,
        context: str | None = None,
        description: str | None = None,
        state: str | None = None,
        target_url: str | None = None,
    ) -> CommitStatus:
        """
        Create a commit status.

        Args:
            owner: owner of the repo
            repo: name of the repo
            sha: sha of the commit
            context:
            description:
            state:
            target_url:

        Returns:
            CommitStatus.

        Raises:
            BadRequestError: 400. APIError is error format response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoCreateStatus
        """
        if context is not None or description is not None or state is not None or target_url is not None:
            _payload = CreateStatusOption(
                context=context, description=description, state=state, target_url=target_url
            ).model_dump(mode="json", by_alias=True, exclude_none=True)
        else:
            _payload = None

        _response = await self._client._request("POST", f"/repos/{owner}/{repo}/statuses/{sha}", json=_payload)
        return decode(_response, CommitStatus)


class ReposSubscription:
    """The ``repos.subscription`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def get(self, owner: str, repo: str) -> WatchInfo:
        """
        Check if the current user is watching a repo.

        Args:
            owner: owner of the repo
            repo: name of the repo

        Returns:
            WatchInfo.

        Raises:
            NotFoundError: 404. User is not watching this repo or repo do not exist.

        Operation ID: userCurrentCheckSubscription
        """
        _response = self._client._request("GET", f"/repos/{owner}/{repo}/subscription")
        return decode(_response, WatchInfo)

    def update(self, owner: str, repo: str) -> WatchInfo:
        """
        Watch a repo.

        Args:
            owner: owner of the repo
            repo: name of the repo

        Returns:
            WatchInfo.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: userCurrentPutSubscription
        """
        _response = self._client._request("PUT", f"/repos/{owner}/{repo}/subscription")
        return decode(_response, WatchInfo)

    def delete(self, owner: str, repo: str) -> None:
        """
        Unwatch a repo.

        Args:
            owner: owner of the repo
            repo: name of the repo

        Returns:
            No content.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: userCurrentDeleteSubscription
        """
        _response = self._client._request("DELETE", f"/repos/{owner}/{repo}/subscription")
        return decode(_response, None)


class AsyncReposSubscription:
    """The ``repos.subscription`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def get(self, owner: str, repo: str) -> WatchInfo:
        """
        Check if the current user is watching a repo.

        Args:
            owner: owner of the repo
            repo: name of the repo

        Returns:
            WatchInfo.

        Raises:
            NotFoundError: 404. User is not watching this repo or repo do not exist.

        Operation ID: userCurrentCheckSubscription
        """
        _response = await self._client._request("GET", f"/repos/{owner}/{repo}/subscription")
        return decode(_response, WatchInfo)

    async def update(self, owner: str, repo: str) -> WatchInfo:
        """
        Watch a repo.

        Args:
            owner: owner of the repo
            repo: name of the repo

        Returns:
            WatchInfo.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: userCurrentPutSubscription
        """
        _response = await self._client._request("PUT", f"/repos/{owner}/{repo}/subscription")
        return decode(_response, WatchInfo)

    async def delete(self, owner: str, repo: str) -> None:
        """
        Unwatch a repo.

        Args:
            owner: owner of the repo
            repo: name of the repo

        Returns:
            No content.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: userCurrentDeleteSubscription
        """
        _response = await self._client._request("DELETE", f"/repos/{owner}/{repo}/subscription")
        return decode(_response, None)


class ReposSyncFork:
    """The ``repos.sync_fork`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def get(self, owner: str, repo: str) -> SyncForkInfo:
        """
        Gets information about syncing the fork default branch with the base branch.

        Args:
            owner: owner of the repo
            repo: name of the repo

        Returns:
            SyncForkInfo.

        Raises:
            BadRequestError: 400. APIError is error format response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoSyncForkDefaultInfo
        """
        _response = self._client._request("GET", f"/repos/{owner}/{repo}/sync_fork")
        return decode(_response, SyncForkInfo)

    def sync(self, owner: str, repo: str) -> None:
        """
        Syncs the default branch of a fork with the base branch.

        Args:
            owner: owner of the repo
            repo: name of the repo

        Returns:
            No content.

        Raises:
            BadRequestError: 400. APIError is error format response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoSyncForkDefault
        """
        _response = self._client._request("POST", f"/repos/{owner}/{repo}/sync_fork")
        return decode(_response, None)

    def get_branch(self, owner: str, repo: str, branch: str) -> SyncForkInfo:
        """
        Gets information about syncing a fork branch with the base branch.

        Args:
            owner: owner of the repo
            repo: name of the repo
            branch: The branch

        Returns:
            SyncForkInfo.

        Raises:
            BadRequestError: 400. APIError is error format response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoSyncForkBranchInfo
        """
        _response = self._client._request("GET", f"/repos/{owner}/{repo}/sync_fork/{branch}")
        return decode(_response, SyncForkInfo)

    def sync_branch(self, owner: str, repo: str, branch: str) -> None:
        """
        Syncs a fork branch with the base branch.

        Args:
            owner: owner of the repo
            repo: name of the repo
            branch: The branch

        Returns:
            No content.

        Raises:
            BadRequestError: 400. APIError is error format response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoSyncForkBranch
        """
        _response = self._client._request("POST", f"/repos/{owner}/{repo}/sync_fork/{branch}")
        return decode(_response, None)


class AsyncReposSyncFork:
    """The ``repos.sync_fork`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def get(self, owner: str, repo: str) -> SyncForkInfo:
        """
        Gets information about syncing the fork default branch with the base branch.

        Args:
            owner: owner of the repo
            repo: name of the repo

        Returns:
            SyncForkInfo.

        Raises:
            BadRequestError: 400. APIError is error format response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoSyncForkDefaultInfo
        """
        _response = await self._client._request("GET", f"/repos/{owner}/{repo}/sync_fork")
        return decode(_response, SyncForkInfo)

    async def sync(self, owner: str, repo: str) -> None:
        """
        Syncs the default branch of a fork with the base branch.

        Args:
            owner: owner of the repo
            repo: name of the repo

        Returns:
            No content.

        Raises:
            BadRequestError: 400. APIError is error format response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoSyncForkDefault
        """
        _response = await self._client._request("POST", f"/repos/{owner}/{repo}/sync_fork")
        return decode(_response, None)

    async def get_branch(self, owner: str, repo: str, branch: str) -> SyncForkInfo:
        """
        Gets information about syncing a fork branch with the base branch.

        Args:
            owner: owner of the repo
            repo: name of the repo
            branch: The branch

        Returns:
            SyncForkInfo.

        Raises:
            BadRequestError: 400. APIError is error format response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoSyncForkBranchInfo
        """
        _response = await self._client._request("GET", f"/repos/{owner}/{repo}/sync_fork/{branch}")
        return decode(_response, SyncForkInfo)

    async def sync_branch(self, owner: str, repo: str, branch: str) -> None:
        """
        Syncs a fork branch with the base branch.

        Args:
            owner: owner of the repo
            repo: name of the repo
            branch: The branch

        Returns:
            No content.

        Raises:
            BadRequestError: 400. APIError is error format response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoSyncForkBranch
        """
        _response = await self._client._request("POST", f"/repos/{owner}/{repo}/sync_fork/{branch}")
        return decode(_response, None)


class ReposTagProtections:
    """The ``repos.tag_protections`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def list(self, owner: str, repo: str) -> builtins.list[TagProtection]:
        """
        List tag protections for a repository.

        Args:
            owner: owner of the repo
            repo: name of the repo

        Returns:
            TagProtectionList.

        Operation ID: repoListTagProtection
        """
        _response = self._client._request("GET", f"/repos/{owner}/{repo}/tag_protections")
        return decode(_response, list[TagProtection])

    def create(
        self,
        owner: str,
        repo: str,
        *,
        name_pattern: str | None = None,
        whitelist_teams: builtins.list[str] | None = None,
        whitelist_usernames: builtins.list[str] | None = None,
    ) -> TagProtection:
        """
        Create a tag protections for a repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            name_pattern:
            whitelist_teams:
            whitelist_usernames:

        Returns:
            TagProtection.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.
            LockedError: 423. APIRepoArchivedError is an error that is raised when an archived repo should be modified.

        Operation ID: repoCreateTagProtection
        """
        if name_pattern is not None or whitelist_teams is not None or whitelist_usernames is not None:
            _payload = CreateTagProtectionOption(
                name_pattern=name_pattern, whitelist_teams=whitelist_teams, whitelist_usernames=whitelist_usernames
            ).model_dump(mode="json", by_alias=True, exclude_none=True)
        else:
            _payload = None

        _response = self._client._request("POST", f"/repos/{owner}/{repo}/tag_protections", json=_payload)
        return decode(_response, TagProtection)

    def get(self, owner: str, repo: str, id: int) -> TagProtection:
        """
        Get a specific tag protection for the repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            id: id of the tag protect to get

        Returns:
            TagProtection.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoGetTagProtection
        """
        _response = self._client._request("GET", f"/repos/{owner}/{repo}/tag_protections/{id}")
        return decode(_response, TagProtection)

    def update(
        self,
        owner: str,
        repo: str,
        id: int,
        *,
        name_pattern: str | None = None,
        whitelist_teams: builtins.list[str] | None = None,
        whitelist_usernames: builtins.list[str] | None = None,
    ) -> TagProtection:
        """
        Edit a tag protections for a repository. Only fields that are set will be changed.

        Args:
            owner: owner of the repo
            repo: name of the repo
            id: id of protected tag
            name_pattern:
            whitelist_teams:
            whitelist_usernames:

        Returns:
            TagProtection.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.
            LockedError: 423. APIRepoArchivedError is an error that is raised when an archived repo should be modified.

        Operation ID: repoEditTagProtection
        """
        if name_pattern is not None or whitelist_teams is not None or whitelist_usernames is not None:
            _payload = EditTagProtectionOption(
                name_pattern=name_pattern, whitelist_teams=whitelist_teams, whitelist_usernames=whitelist_usernames
            ).model_dump(mode="json", by_alias=True, exclude_none=True)
        else:
            _payload = None

        _response = self._client._request("PATCH", f"/repos/{owner}/{repo}/tag_protections/{id}", json=_payload)
        return decode(_response, TagProtection)

    def delete(self, owner: str, repo: str, id: int) -> None:
        """
        Delete a specific tag protection for the repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            id: id of protected tag

        Returns:
            No content.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoDeleteTagProtection
        """
        _response = self._client._request("DELETE", f"/repos/{owner}/{repo}/tag_protections/{id}")
        return decode(_response, None)


class AsyncReposTagProtections:
    """The ``repos.tag_protections`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def list(self, owner: str, repo: str) -> builtins.list[TagProtection]:
        """
        List tag protections for a repository.

        Args:
            owner: owner of the repo
            repo: name of the repo

        Returns:
            TagProtectionList.

        Operation ID: repoListTagProtection
        """
        _response = await self._client._request("GET", f"/repos/{owner}/{repo}/tag_protections")
        return decode(_response, list[TagProtection])

    async def create(
        self,
        owner: str,
        repo: str,
        *,
        name_pattern: str | None = None,
        whitelist_teams: builtins.list[str] | None = None,
        whitelist_usernames: builtins.list[str] | None = None,
    ) -> TagProtection:
        """
        Create a tag protections for a repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            name_pattern:
            whitelist_teams:
            whitelist_usernames:

        Returns:
            TagProtection.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.
            LockedError: 423. APIRepoArchivedError is an error that is raised when an archived repo should be modified.

        Operation ID: repoCreateTagProtection
        """
        if name_pattern is not None or whitelist_teams is not None or whitelist_usernames is not None:
            _payload = CreateTagProtectionOption(
                name_pattern=name_pattern, whitelist_teams=whitelist_teams, whitelist_usernames=whitelist_usernames
            ).model_dump(mode="json", by_alias=True, exclude_none=True)
        else:
            _payload = None

        _response = await self._client._request("POST", f"/repos/{owner}/{repo}/tag_protections", json=_payload)
        return decode(_response, TagProtection)

    async def get(self, owner: str, repo: str, id: int) -> TagProtection:
        """
        Get a specific tag protection for the repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            id: id of the tag protect to get

        Returns:
            TagProtection.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoGetTagProtection
        """
        _response = await self._client._request("GET", f"/repos/{owner}/{repo}/tag_protections/{id}")
        return decode(_response, TagProtection)

    async def update(
        self,
        owner: str,
        repo: str,
        id: int,
        *,
        name_pattern: str | None = None,
        whitelist_teams: builtins.list[str] | None = None,
        whitelist_usernames: builtins.list[str] | None = None,
    ) -> TagProtection:
        """
        Edit a tag protections for a repository. Only fields that are set will be changed.

        Args:
            owner: owner of the repo
            repo: name of the repo
            id: id of protected tag
            name_pattern:
            whitelist_teams:
            whitelist_usernames:

        Returns:
            TagProtection.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.
            LockedError: 423. APIRepoArchivedError is an error that is raised when an archived repo should be modified.

        Operation ID: repoEditTagProtection
        """
        if name_pattern is not None or whitelist_teams is not None or whitelist_usernames is not None:
            _payload = EditTagProtectionOption(
                name_pattern=name_pattern, whitelist_teams=whitelist_teams, whitelist_usernames=whitelist_usernames
            ).model_dump(mode="json", by_alias=True, exclude_none=True)
        else:
            _payload = None

        _response = await self._client._request("PATCH", f"/repos/{owner}/{repo}/tag_protections/{id}", json=_payload)
        return decode(_response, TagProtection)

    async def delete(self, owner: str, repo: str, id: int) -> None:
        """
        Delete a specific tag protection for the repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            id: id of protected tag

        Returns:
            No content.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoDeleteTagProtection
        """
        _response = await self._client._request("DELETE", f"/repos/{owner}/{repo}/tag_protections/{id}")
        return decode(_response, None)


class ReposTags:
    """The ``repos.tags`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def list(self, owner: str, repo: str, *, page: int | None = None, limit: int | None = None) -> Paginated[Tag]:
        """
        List a repository's tags.

        Args:
            owner: owner of the repo
            repo: name of the repo
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            TagList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoListTags
        """
        return self._client._paginate("GET", f"/repos/{owner}/{repo}/tags", model=Tag, page=page, limit=limit)

    def create(
        self,
        owner: str,
        repo: str,
        *,
        message: str | None = None,
        tag_name: str,
        target: str | None = None,
    ) -> Tag:
        """
        Create a new git tag in a repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            message:
            tag_name:
            target:

        Returns:
            Tag.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.
            MethodNotAllowedError: 405. APIEmpty is an empty response.
            ConflictError: 409. APIConflict is a conflict empty response.
            PayloadTooLargeError: 413. QuotaExceeded.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.
            LockedError: 423. APIRepoArchivedError is an error that is raised when an archived repo should be modified.

        Operation ID: repoCreateTag
        """
        _payload = CreateTagOption(
            message=message,
            tag_name=tag_name,
            target=target,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = self._client._request("POST", f"/repos/{owner}/{repo}/tags", json=_payload)
        return decode(_response, Tag)

    def get(self, owner: str, repo: str, tag: str) -> Tag:
        """
        Get the tag of a repository by tag name.

        Args:
            owner: owner of the repo
            repo: name of the repo
            tag: name of tag

        Returns:
            Tag.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoGetTag
        """
        _response = self._client._request("GET", f"/repos/{owner}/{repo}/tags/{tag}")
        return decode(_response, Tag)

    def delete(self, owner: str, repo: str, tag: str) -> None:
        """
        Delete a repository's tag by name.

        Args:
            owner: owner of the repo
            repo: name of the repo
            tag: name of tag to delete

        Returns:
            No content.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.
            MethodNotAllowedError: 405. APIEmpty is an empty response.
            ConflictError: 409. APIConflict is a conflict empty response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.
            LockedError: 423. APIRepoArchivedError is an error that is raised when an archived repo should be modified.

        Operation ID: repoDeleteTag
        """
        _response = self._client._request("DELETE", f"/repos/{owner}/{repo}/tags/{tag}")
        return decode(_response, None)


class AsyncReposTags:
    """The ``repos.tags`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def list(
        self,
        owner: str,
        repo: str,
        *,
        page: int | None = None,
        limit: int | None = None,
    ) -> AsyncPaginated[Tag]:
        """
        List a repository's tags.

        Args:
            owner: owner of the repo
            repo: name of the repo
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            TagList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoListTags
        """
        return await self._client._paginate("GET", f"/repos/{owner}/{repo}/tags", model=Tag, page=page, limit=limit)

    async def create(
        self,
        owner: str,
        repo: str,
        *,
        message: str | None = None,
        tag_name: str,
        target: str | None = None,
    ) -> Tag:
        """
        Create a new git tag in a repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            message:
            tag_name:
            target:

        Returns:
            Tag.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.
            MethodNotAllowedError: 405. APIEmpty is an empty response.
            ConflictError: 409. APIConflict is a conflict empty response.
            PayloadTooLargeError: 413. QuotaExceeded.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.
            LockedError: 423. APIRepoArchivedError is an error that is raised when an archived repo should be modified.

        Operation ID: repoCreateTag
        """
        _payload = CreateTagOption(
            message=message,
            tag_name=tag_name,
            target=target,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = await self._client._request("POST", f"/repos/{owner}/{repo}/tags", json=_payload)
        return decode(_response, Tag)

    async def get(self, owner: str, repo: str, tag: str) -> Tag:
        """
        Get the tag of a repository by tag name.

        Args:
            owner: owner of the repo
            repo: name of the repo
            tag: name of tag

        Returns:
            Tag.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoGetTag
        """
        _response = await self._client._request("GET", f"/repos/{owner}/{repo}/tags/{tag}")
        return decode(_response, Tag)

    async def delete(self, owner: str, repo: str, tag: str) -> None:
        """
        Delete a repository's tag by name.

        Args:
            owner: owner of the repo
            repo: name of the repo
            tag: name of tag to delete

        Returns:
            No content.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.
            MethodNotAllowedError: 405. APIEmpty is an empty response.
            ConflictError: 409. APIConflict is a conflict empty response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.
            LockedError: 423. APIRepoArchivedError is an error that is raised when an archived repo should be modified.

        Operation ID: repoDeleteTag
        """
        _response = await self._client._request("DELETE", f"/repos/{owner}/{repo}/tags/{tag}")
        return decode(_response, None)


class ReposTeams:
    """The ``repos.teams`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def list(self, owner: str, repo: str) -> builtins.list[Team]:
        """
        List a repository's teams.

        Args:
            owner: owner of the repo
            repo: name of the repo

        Returns:
            TeamListWithoutPagination - Teams without pagination headers.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.
            MethodNotAllowedError: 405. APIError is error format response.

        Operation ID: repoListTeams
        """
        _response = self._client._request("GET", f"/repos/{owner}/{repo}/teams")
        return decode(_response, list[Team])

    def get(self, owner: str, repo: str, team: str) -> Team:
        """
        Check if a team is assigned to a repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            team: team name

        Returns:
            Team.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.
            MethodNotAllowedError: 405. APIError is error format response.

        Operation ID: repoCheckTeam
        """
        _response = self._client._request("GET", f"/repos/{owner}/{repo}/teams/{team}")
        return decode(_response, Team)

    def add(self, owner: str, repo: str, team: str) -> None:
        """
        Add a team to a repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            team: team name

        Returns:
            No content.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.
            MethodNotAllowedError: 405. APIError is error format response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: repoAddTeam
        """
        _response = self._client._request("PUT", f"/repos/{owner}/{repo}/teams/{team}")
        return decode(_response, None)

    def remove(self, owner: str, repo: str, team: str) -> None:
        """
        Delete a team from a repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            team: team name

        Returns:
            No content.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.
            MethodNotAllowedError: 405. APIError is error format response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: repoDeleteTeam
        """
        _response = self._client._request("DELETE", f"/repos/{owner}/{repo}/teams/{team}")
        return decode(_response, None)


class AsyncReposTeams:
    """The ``repos.teams`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def list(self, owner: str, repo: str) -> builtins.list[Team]:
        """
        List a repository's teams.

        Args:
            owner: owner of the repo
            repo: name of the repo

        Returns:
            TeamListWithoutPagination - Teams without pagination headers.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.
            MethodNotAllowedError: 405. APIError is error format response.

        Operation ID: repoListTeams
        """
        _response = await self._client._request("GET", f"/repos/{owner}/{repo}/teams")
        return decode(_response, list[Team])

    async def get(self, owner: str, repo: str, team: str) -> Team:
        """
        Check if a team is assigned to a repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            team: team name

        Returns:
            Team.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.
            MethodNotAllowedError: 405. APIError is error format response.

        Operation ID: repoCheckTeam
        """
        _response = await self._client._request("GET", f"/repos/{owner}/{repo}/teams/{team}")
        return decode(_response, Team)

    async def add(self, owner: str, repo: str, team: str) -> None:
        """
        Add a team to a repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            team: team name

        Returns:
            No content.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.
            MethodNotAllowedError: 405. APIError is error format response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: repoAddTeam
        """
        _response = await self._client._request("PUT", f"/repos/{owner}/{repo}/teams/{team}")
        return decode(_response, None)

    async def remove(self, owner: str, repo: str, team: str) -> None:
        """
        Delete a team from a repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            team: team name

        Returns:
            No content.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.
            MethodNotAllowedError: 405. APIError is error format response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: repoDeleteTeam
        """
        _response = await self._client._request("DELETE", f"/repos/{owner}/{repo}/teams/{team}")
        return decode(_response, None)


class ReposTimes:
    """The ``repos.times`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def list(
        self,
        owner: str,
        repo: str,
        *,
        user: str | None = None,
        since: datetime | None = None,
        before: datetime | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> Paginated[TrackedTime]:
        """
        List a repo's tracked times.

        Args:
            owner: owner of the repo
            repo: name of the repo
            user: optional filter by user (available for issue managers)
            since: Only show times updated after the given time. This is a timestamp in RFC 3339 format
            before: Only show times updated before the given time. This is a timestamp in RFC 3339 format
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            TrackedTimeList.

        Raises:
            BadRequestError: 400. APIError is error format response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: repoTrackedTimes
        """
        _query: dict[str, object] = {
            "user": user,
            "since": None if since is None else since.isoformat(),
            "before": None if before is None else before.isoformat(),
        }

        return self._client._paginate(
            "GET", f"/repos/{owner}/{repo}/times", model=TrackedTime, params=_query, page=page, limit=limit
        )

    def get(self, owner: str, repo: str, user: str) -> builtins.list[TrackedTime]:
        """
        List a user's tracked times in a repo.

        Args:
            owner: owner of the repo
            repo: name of the repo
            user: username of user

        Returns:
            TrackedTimeListWithoutPagination - Tracked times for a specific user (no pagination headers).

        Raises:
            BadRequestError: 400. APIError is error format response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Deprecated:
            Deprecated in the vendored Spec; generated for compatibility.

        Operation ID: userTrackedTimes
        """
        _response = self._client._request("GET", f"/repos/{owner}/{repo}/times/{user}")
        return decode(_response, list[TrackedTime])


class AsyncReposTimes:
    """The ``repos.times`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def list(
        self,
        owner: str,
        repo: str,
        *,
        user: str | None = None,
        since: datetime | None = None,
        before: datetime | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> AsyncPaginated[TrackedTime]:
        """
        List a repo's tracked times.

        Args:
            owner: owner of the repo
            repo: name of the repo
            user: optional filter by user (available for issue managers)
            since: Only show times updated after the given time. This is a timestamp in RFC 3339 format
            before: Only show times updated before the given time. This is a timestamp in RFC 3339 format
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            TrackedTimeList.

        Raises:
            BadRequestError: 400. APIError is error format response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: repoTrackedTimes
        """
        _query: dict[str, object] = {
            "user": user,
            "since": None if since is None else since.isoformat(),
            "before": None if before is None else before.isoformat(),
        }

        return await self._client._paginate(
            "GET", f"/repos/{owner}/{repo}/times", model=TrackedTime, params=_query, page=page, limit=limit
        )

    async def get(self, owner: str, repo: str, user: str) -> builtins.list[TrackedTime]:
        """
        List a user's tracked times in a repo.

        Args:
            owner: owner of the repo
            repo: name of the repo
            user: username of user

        Returns:
            TrackedTimeListWithoutPagination - Tracked times for a specific user (no pagination headers).

        Raises:
            BadRequestError: 400. APIError is error format response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Deprecated:
            Deprecated in the vendored Spec; generated for compatibility.

        Operation ID: userTrackedTimes
        """
        _response = await self._client._request("GET", f"/repos/{owner}/{repo}/times/{user}")
        return decode(_response, list[TrackedTime])


class ReposTopics:
    """The ``repos.topics`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def list(self, owner: str, repo: str, *, page: int | None = None, limit: int | None = None) -> TopicName:
        """
        Get list of topics that a repository has.

        Args:
            owner: owner of the repo
            repo: name of the repo
            page: page number of results to return (1-based)
            limit: page size of results

        Returns:
            TopicNames.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoListTopics
        """
        _query: dict[str, object] = {"page": page, "limit": limit}

        _response = self._client._request("GET", f"/repos/{owner}/{repo}/topics", params=_query)
        return decode(_response, TopicName)

    def update(self, owner: str, repo: str, *, topics: builtins.list[str] | None = None) -> None:
        """
        Replace list of topics for a repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            topics: list of topic names

        Returns:
            No content.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIInvalidTopicsError is error format response to invalid topics.

        Operation ID: repoUpdateTopics
        """
        if topics is not None:
            _payload = RepoTopicOptions(topics=topics).model_dump(mode="json", by_alias=True, exclude_none=True)
        else:
            _payload = None

        _response = self._client._request("PUT", f"/repos/{owner}/{repo}/topics", json=_payload)
        return decode(_response, None)

    def add(self, owner: str, repo: str, topic: str) -> None:
        """
        Add a topic to a repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            topic: name of the topic to add

        Returns:
            No content.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIInvalidTopicsError is error format response to invalid topics.

        Operation ID: repoAddTopic
        """
        _response = self._client._request("PUT", f"/repos/{owner}/{repo}/topics/{topic}")
        return decode(_response, None)

    def remove(self, owner: str, repo: str, topic: str) -> None:
        """
        Delete a topic from a repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            topic: name of the topic to delete

        Returns:
            No content.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIInvalidTopicsError is error format response to invalid topics.

        Operation ID: repoDeleteTopic
        """
        _response = self._client._request("DELETE", f"/repos/{owner}/{repo}/topics/{topic}")
        return decode(_response, None)


class AsyncReposTopics:
    """The ``repos.topics`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def list(self, owner: str, repo: str, *, page: int | None = None, limit: int | None = None) -> TopicName:
        """
        Get list of topics that a repository has.

        Args:
            owner: owner of the repo
            repo: name of the repo
            page: page number of results to return (1-based)
            limit: page size of results

        Returns:
            TopicNames.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoListTopics
        """
        _query: dict[str, object] = {"page": page, "limit": limit}

        _response = await self._client._request("GET", f"/repos/{owner}/{repo}/topics", params=_query)
        return decode(_response, TopicName)

    async def update(self, owner: str, repo: str, *, topics: builtins.list[str] | None = None) -> None:
        """
        Replace list of topics for a repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            topics: list of topic names

        Returns:
            No content.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIInvalidTopicsError is error format response to invalid topics.

        Operation ID: repoUpdateTopics
        """
        if topics is not None:
            _payload = RepoTopicOptions(topics=topics).model_dump(mode="json", by_alias=True, exclude_none=True)
        else:
            _payload = None

        _response = await self._client._request("PUT", f"/repos/{owner}/{repo}/topics", json=_payload)
        return decode(_response, None)

    async def add(self, owner: str, repo: str, topic: str) -> None:
        """
        Add a topic to a repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            topic: name of the topic to add

        Returns:
            No content.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIInvalidTopicsError is error format response to invalid topics.

        Operation ID: repoAddTopic
        """
        _response = await self._client._request("PUT", f"/repos/{owner}/{repo}/topics/{topic}")
        return decode(_response, None)

    async def remove(self, owner: str, repo: str, topic: str) -> None:
        """
        Delete a topic from a repository.

        Args:
            owner: owner of the repo
            repo: name of the repo
            topic: name of the topic to delete

        Returns:
            No content.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIInvalidTopicsError is error format response to invalid topics.

        Operation ID: repoDeleteTopic
        """
        _response = await self._client._request("DELETE", f"/repos/{owner}/{repo}/topics/{topic}")
        return decode(_response, None)


class ReposWiki:
    """The ``repos.wiki`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client
        self.page: ReposWikiPage = ReposWikiPage(client)
        self.revisions: ReposWikiRevisions = ReposWikiRevisions(client)

    def create(
        self,
        owner: str,
        repo: str,
        *,
        content_base64: str | None = None,
        message: str | None = None,
        title: str | None = None,
    ) -> WikiPage:
        """
        Create a wiki page.

        Args:
            owner: owner of the repo
            repo: name of the repo
            content_base64: content must be base64 encoded
            message: optional commit message summarizing the change
            title: page title. leave empty to keep unchanged

        Returns:
            WikiPage.

        Raises:
            BadRequestError: 400. APIError is error format response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.
            PayloadTooLargeError: 413. QuotaExceeded.
            LockedError: 423. APIRepoArchivedError is an error that is raised when an archived repo should be modified.

        Operation ID: repoCreateWikiPage
        """
        if content_base64 is not None or message is not None or title is not None:
            _payload = CreateWikiPageOptions(content_base64=content_base64, message=message, title=title).model_dump(
                mode="json", by_alias=True, exclude_none=True
            )
        else:
            _payload = None

        _response = self._client._request("POST", f"/repos/{owner}/{repo}/wiki/new", json=_payload)
        return decode(_response, WikiPage)

    def pages(
        self,
        owner: str,
        repo: str,
        *,
        page: int | None = None,
        limit: int | None = None,
    ) -> Paginated[WikiPageMetaData]:
        """
        Get all wiki pages.

        Args:
            owner: owner of the repo
            repo: name of the repo
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            WikiPageList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoGetWikiPages
        """
        return self._client._paginate(
            "GET", f"/repos/{owner}/{repo}/wiki/pages", model=WikiPageMetaData, page=page, limit=limit
        )


class AsyncReposWiki:
    """The ``repos.wiki`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client
        self.page: AsyncReposWikiPage = AsyncReposWikiPage(client)
        self.revisions: AsyncReposWikiRevisions = AsyncReposWikiRevisions(client)

    async def create(
        self,
        owner: str,
        repo: str,
        *,
        content_base64: str | None = None,
        message: str | None = None,
        title: str | None = None,
    ) -> WikiPage:
        """
        Create a wiki page.

        Args:
            owner: owner of the repo
            repo: name of the repo
            content_base64: content must be base64 encoded
            message: optional commit message summarizing the change
            title: page title. leave empty to keep unchanged

        Returns:
            WikiPage.

        Raises:
            BadRequestError: 400. APIError is error format response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.
            PayloadTooLargeError: 413. QuotaExceeded.
            LockedError: 423. APIRepoArchivedError is an error that is raised when an archived repo should be modified.

        Operation ID: repoCreateWikiPage
        """
        if content_base64 is not None or message is not None or title is not None:
            _payload = CreateWikiPageOptions(content_base64=content_base64, message=message, title=title).model_dump(
                mode="json", by_alias=True, exclude_none=True
            )
        else:
            _payload = None

        _response = await self._client._request("POST", f"/repos/{owner}/{repo}/wiki/new", json=_payload)
        return decode(_response, WikiPage)

    async def pages(
        self,
        owner: str,
        repo: str,
        *,
        page: int | None = None,
        limit: int | None = None,
    ) -> AsyncPaginated[WikiPageMetaData]:
        """
        Get all wiki pages.

        Args:
            owner: owner of the repo
            repo: name of the repo
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            WikiPageList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoGetWikiPages
        """
        return await self._client._paginate(
            "GET", f"/repos/{owner}/{repo}/wiki/pages", model=WikiPageMetaData, page=page, limit=limit
        )


class ReposWikiPage:
    """The ``repos.wiki.page`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def get(self, owner: str, repo: str, page_name: str) -> WikiPage:
        """
        Get a wiki page.

        Args:
            owner: owner of the repo
            repo: name of the repo
            page_name: name of the page

        Returns:
            WikiPage.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoGetWikiPage
        """
        _response = self._client._request("GET", f"/repos/{owner}/{repo}/wiki/page/{page_name}")
        return decode(_response, WikiPage)

    def update(
        self,
        owner: str,
        repo: str,
        page_name: str,
        *,
        content_base64: str | None = None,
        message: str | None = None,
        title: str | None = None,
    ) -> WikiPage:
        """
        Edit a wiki page.

        Args:
            owner: owner of the repo
            repo: name of the repo
            page_name: name of the page
            content_base64: content must be base64 encoded
            message: optional commit message summarizing the change
            title: page title. leave empty to keep unchanged

        Returns:
            WikiPage.

        Raises:
            BadRequestError: 400. APIError is error format response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.
            PayloadTooLargeError: 413. QuotaExceeded.
            LockedError: 423. APIRepoArchivedError is an error that is raised when an archived repo should be modified.

        Operation ID: repoEditWikiPage
        """
        if content_base64 is not None or message is not None or title is not None:
            _payload = CreateWikiPageOptions(content_base64=content_base64, message=message, title=title).model_dump(
                mode="json", by_alias=True, exclude_none=True
            )
        else:
            _payload = None

        _response = self._client._request("PATCH", f"/repos/{owner}/{repo}/wiki/page/{page_name}", json=_payload)
        return decode(_response, WikiPage)

    def delete(self, owner: str, repo: str, page_name: str) -> None:
        """
        Delete a wiki page.

        Args:
            owner: owner of the repo
            repo: name of the repo
            page_name: name of the page

        Returns:
            No content.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.
            LockedError: 423. APIRepoArchivedError is an error that is raised when an archived repo should be modified.

        Operation ID: repoDeleteWikiPage
        """
        _response = self._client._request("DELETE", f"/repos/{owner}/{repo}/wiki/page/{page_name}")
        return decode(_response, None)


class AsyncReposWikiPage:
    """The ``repos.wiki.page`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def get(self, owner: str, repo: str, page_name: str) -> WikiPage:
        """
        Get a wiki page.

        Args:
            owner: owner of the repo
            repo: name of the repo
            page_name: name of the page

        Returns:
            WikiPage.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoGetWikiPage
        """
        _response = await self._client._request("GET", f"/repos/{owner}/{repo}/wiki/page/{page_name}")
        return decode(_response, WikiPage)

    async def update(
        self,
        owner: str,
        repo: str,
        page_name: str,
        *,
        content_base64: str | None = None,
        message: str | None = None,
        title: str | None = None,
    ) -> WikiPage:
        """
        Edit a wiki page.

        Args:
            owner: owner of the repo
            repo: name of the repo
            page_name: name of the page
            content_base64: content must be base64 encoded
            message: optional commit message summarizing the change
            title: page title. leave empty to keep unchanged

        Returns:
            WikiPage.

        Raises:
            BadRequestError: 400. APIError is error format response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.
            PayloadTooLargeError: 413. QuotaExceeded.
            LockedError: 423. APIRepoArchivedError is an error that is raised when an archived repo should be modified.

        Operation ID: repoEditWikiPage
        """
        if content_base64 is not None or message is not None or title is not None:
            _payload = CreateWikiPageOptions(content_base64=content_base64, message=message, title=title).model_dump(
                mode="json", by_alias=True, exclude_none=True
            )
        else:
            _payload = None

        _response = await self._client._request("PATCH", f"/repos/{owner}/{repo}/wiki/page/{page_name}", json=_payload)
        return decode(_response, WikiPage)

    async def delete(self, owner: str, repo: str, page_name: str) -> None:
        """
        Delete a wiki page.

        Args:
            owner: owner of the repo
            repo: name of the repo
            page_name: name of the page

        Returns:
            No content.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.
            LockedError: 423. APIRepoArchivedError is an error that is raised when an archived repo should be modified.

        Operation ID: repoDeleteWikiPage
        """
        _response = await self._client._request("DELETE", f"/repos/{owner}/{repo}/wiki/page/{page_name}")
        return decode(_response, None)


class ReposWikiRevisions:
    """The ``repos.wiki.revisions`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def get(self, owner: str, repo: str, page_name: str, *, page: int | None = None) -> WikiCommitList:
        """
        Get revisions of a wiki page.

        Args:
            owner: owner of the repo
            repo: name of the repo
            page_name: name of the page
            page: page number of results to return (1-based)

        Returns:
            WikiCommitList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoGetWikiPageRevisions
        """
        _query: dict[str, object] = {"page": page}

        _response = self._client._request("GET", f"/repos/{owner}/{repo}/wiki/revisions/{page_name}", params=_query)
        return decode(_response, WikiCommitList)


class AsyncReposWikiRevisions:
    """The ``repos.wiki.revisions`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def get(self, owner: str, repo: str, page_name: str, *, page: int | None = None) -> WikiCommitList:
        """
        Get revisions of a wiki page.

        Args:
            owner: owner of the repo
            repo: name of the repo
            page_name: name of the page
            page: page number of results to return (1-based)

        Returns:
            WikiCommitList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoGetWikiPageRevisions
        """
        _query: dict[str, object] = {"page": page}

        _response = await self._client._request(
            "GET", f"/repos/{owner}/{repo}/wiki/revisions/{page_name}", params=_query
        )
        return decode(_response, WikiCommitList)
