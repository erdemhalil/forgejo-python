"""Pull-request flow: create, inspect, review, dismiss, merge."""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

import pyfj

if TYPE_CHECKING:
    from harness import Seed

pytestmark = pytest.mark.integration


def test_pull_request_flow(admin_client: pyfj.Forgejo, user_client: pyfj.Forgejo, seed: Seed) -> None:
    repo = seed.repo_for("scenario-pull")
    admin_client.repos.contents.create(
        repo.owner,
        repo.name,
        "scenario-pull.txt",
        content="cHVsbCBjb250ZW50",
        message="add scenario pull file",
        new_branch="scenario-pull",
    )

    pull = admin_client.repos.pulls.create(
        repo.owner,
        repo.name,
        title="Scenario pull",
        head="scenario-pull",
        base="main",
        body="scenario body",
    )
    assert pull.number is not None
    assert pull.number is not None
    assert pull.state == "open"

    listed = admin_client.repos.pulls.list(repo.owner, repo.name, state="open")
    assert [item.number for item in listed.page(1)] == [pull.number]
    by_base_head = admin_client.repos.pulls.get_by_base_head(repo.owner, repo.name, "main", "scenario-pull")
    assert by_base_head.number == pull.number

    commits = admin_client.repos.pulls.commits(repo.owner, repo.name, pull.number)
    assert len(commits.page(1)) == 1
    files = admin_client.repos.pulls.files(repo.owner, repo.name, pull.number)
    changed = files.page(1)
    assert [file.filename for file in changed] == ["scenario-pull.txt"]

    diff = admin_client.repos.pulls.download(repo.owner, repo.name, pull.number, "diff")
    assert "scenario-pull.txt" in diff

    comparison = admin_client.repos.compare(repo.owner, repo.name, "main...scenario-pull")
    assert comparison.total_commits == 1

    # Reviews: the regular user approves, the admin dismisses and un-dismisses.
    admin_client.repos.pulls.requested_reviewers.create(repo.owner, repo.name, pull.number, reviewers=[seed.user])
    admin_client.repos.collaborators.add(
        repo.owner,
        repo.name,
        seed.user,
        permission=pyfj.AddCollaboratorOptionPermission.WRITE,
    )
    review = user_client.repos.pulls.reviews.create(
        repo.owner,
        repo.name,
        pull.number,
        body="scenario review",
        event="APPROVED",
    )
    assert review.state == "APPROVED"
    assert review.official is True
    assert review.id is not None
    reviews = admin_client.repos.pulls.reviews.list(repo.owner, repo.name, pull.number)
    assert [item.id for item in reviews.page(1)] == [review.id]

    dismissed = admin_client.repos.pulls.reviews.dismiss(
        repo.owner,
        repo.name,
        pull.number,
        review.id,
        message="scenario dismiss",
    )
    assert dismissed.dismissed is True
    undismissed = admin_client.repos.pulls.reviews.undismiss(repo.owner, repo.name, pull.number, review.id)
    assert undismissed.dismissed is False
    admin_client.repos.pulls.requested_reviewers.delete(repo.owner, repo.name, pull.number, reviewers=[seed.user])

    # Review comments on a pending review.
    pending = admin_client.repos.pulls.reviews.create(
        repo.owner,
        repo.name,
        pull.number,
        body="pending review",
    )
    assert pending.id is not None
    comment = admin_client.repos.pulls.reviews.comments.create(
        repo.owner,
        repo.name,
        pull.number,
        pending.id,
        body="scenario review comment",
        path="scenario-pull.txt",
        new_position=1,
    )
    assert comment.id is not None
    fetched = admin_client.repos.pulls.reviews.comments.get(repo.owner, repo.name, pull.number, pending.id, comment.id)
    assert fetched.body == "scenario review comment"
    admin_client.repos.pulls.reviews.comments.delete(repo.owner, repo.name, pull.number, pending.id, comment.id)
    admin_client.repos.pulls.reviews.delete(repo.owner, repo.name, pull.number, pending.id)

    # Merge and confirm the state.
    admin_client.repos.pulls.merge(
        repo.owner,
        repo.name,
        pull.number,
        do=pyfj.MergePullRequestOptionDo.MERGE,
    )
    merged = admin_client.repos.pulls.get(repo.owner, repo.name, pull.number)
    assert merged.merged is True
    assert merged.merge_commit_sha is not None
    admin_client.repos.pulls.is_merged(repo.owner, repo.name, pull.number)

    from_commit = admin_client.repos.commits.pull_request(repo.owner, repo.name, merged.merge_commit_sha)
    assert from_commit.number == pull.number
