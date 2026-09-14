"""Issue lifecycle: create, comment, label, time, react, subscribe, close, delete."""

from __future__ import annotations

from datetime import UTC, datetime
from typing import TYPE_CHECKING

import pytest

import pyfj

if TYPE_CHECKING:
    from harness import RepoRef, Seed

pytestmark = pytest.mark.integration


def test_issue_lifecycle(admin_client: pyfj.Forgejo, seed: Seed) -> None:
    repo: RepoRef = seed.repo_for("scenario-issues")
    milestone = admin_client.repos.milestones.create(repo.owner, repo.name, title="scenario milestone")
    assert milestone.id is not None
    label = admin_client.repos.labels.create(repo.owner, repo.name, name="scenario-bug", color="#d73a4a")
    assert label.id is not None

    issue = admin_client.repos.issues.create(
        repo.owner,
        repo.name,
        title="Scenario issue",
        body="first body",
        labels=[label.id],
        milestone=milestone.id,
    )
    assert issue.number is not None
    assert issue.title == "Scenario issue"
    assert issue.state == "open"
    assert issue.labels
    assert issue.labels[0].name == "scenario-bug"

    fetched = admin_client.repos.issues.get(repo.owner, repo.name, issue.number)
    assert fetched.number == issue.number

    edited = admin_client.repos.issues.update(repo.owner, repo.name, issue.number, body="edited body")
    assert edited.body == "edited body"

    # Comments, listing and timeline.
    comment = admin_client.repos.issues.comments.create(repo.owner, repo.name, issue.number, body="a comment")
    assert comment.id is not None
    comments = admin_client.repos.issues.comments.list(repo.owner, repo.name, issue.number)
    assert [item.id for item in comments] == [comment.id]
    edited_comment = admin_client.repos.issues.comments.update(repo.owner, repo.name, comment.id, body="edited comment")
    assert edited_comment is not None
    assert edited_comment.body == "edited comment"
    timeline = admin_client.repos.issues.timeline(repo.owner, repo.name, issue.number)
    assert any(entry.id == comment.id for entry in timeline.page(1))

    # Labels: add, replace, clear.
    second_label = admin_client.repos.labels.create(repo.owner, repo.name, name="scenario-feature", color="#0e8a16")
    assert second_label.id is not None
    added = admin_client.repos.issues.labels.add(repo.owner, repo.name, issue.number, labels=[second_label.id])
    assert {lab.id for lab in added} == {label.id, second_label.id}
    replaced = admin_client.repos.issues.labels.update(repo.owner, repo.name, issue.number, labels=[label.id])
    assert {lab.id for lab in replaced} == {label.id}
    admin_client.repos.issues.labels.clear(repo.owner, repo.name, issue.number)
    assert admin_client.repos.issues.labels.list(repo.owner, repo.name, issue.number) == []

    # Tracked time.
    entry = admin_client.repos.issues.times.add(repo.owner, repo.name, issue.number, time=90)
    assert entry.time == 90
    assert entry.id is not None
    times = admin_client.repos.issues.times.list(repo.owner, repo.name, issue.number)
    assert [item.id for item in times.page(1)] == [entry.id]
    admin_client.repos.issues.times.delete(repo.owner, repo.name, issue.number, entry.id)

    # Reaction. Only the first page is fetched explicitly: Forgejo returns
    # JSON null for the empty next page, which decoding (correctly, per Spec)
    # rejects, so transparent iteration cannot walk past the last page.
    reaction = admin_client.repos.issues.reactions.create(repo.owner, repo.name, issue.number, content="+1")
    assert reaction.content == "+1"
    reactions = admin_client.repos.issues.reactions.list(repo.owner, repo.name, issue.number)
    assert [item.content for item in reactions.page(1)] == ["+1"]
    admin_client.repos.issues.reactions.delete(repo.owner, repo.name, issue.number, content="+1")

    # Subscription check for the acting user.
    login = admin_client.user.get().login
    assert login is not None
    admin_client.repos.issues.subscriptions.add(repo.owner, repo.name, issue.number, login)
    watch = admin_client.repos.issues.subscriptions.check(repo.owner, repo.name, issue.number)
    assert watch.subscribed is True
    admin_client.repos.issues.subscriptions.remove(repo.owner, repo.name, issue.number, login)
    after = admin_client.repos.issues.subscriptions.check(repo.owner, repo.name, issue.number)
    assert after.subscribed is False

    # Deadline and pinning.
    deadline = admin_client.repos.issues.deadline(
        repo.owner,
        repo.name,
        issue.number,
        due_date=datetime(2030, 1, 1, tzinfo=UTC),
    )
    assert deadline.due_date is not None
    admin_client.repos.issues.pin(repo.owner, repo.name, issue.number)
    pinned = admin_client.repos.issues.pinned(repo.owner, repo.name)
    assert any(item.number == issue.number for item in pinned)
    admin_client.repos.issues.unpin(repo.owner, repo.name, issue.number)

    # Close and delete.
    closed = admin_client.repos.issues.update(repo.owner, repo.name, issue.number, state="closed")
    assert closed.state == "closed"
    admin_client.repos.issues.delete(repo.owner, repo.name, issue.number)

    with pytest.raises(pyfj.NotFoundError):
        admin_client.repos.issues.get(repo.owner, repo.name, issue.number)
