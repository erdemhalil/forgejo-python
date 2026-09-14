"""Multipart uploads: issue, comment, and release attachments."""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

if TYPE_CHECKING:
    from harness import Seed

    import pyfj

pytestmark = pytest.mark.integration


def test_issue_attachment_forms(admin_client: pyfj.Forgejo, seed: Seed) -> None:
    repo = seed.repo_for("scenario-uploads")
    issue = seed.issue(repo, "uploads")

    named = admin_client.repos.issues.assets.create(
        repo.owner,
        repo.name,
        issue.index,
        attachment=("upload-named.txt", b"named attachment", "text/plain"),
    )
    assert named.name == "upload-named.txt"
    assert named.size == len(b"named attachment")
    assert named.id is not None

    fetched = admin_client.repos.issues.assets.get(repo.owner, repo.name, issue.index, named.id)
    assert fetched.id == named.id

    attachments = admin_client.repos.issues.assets.list(repo.owner, repo.name, issue.index)
    assert [item.id for item in attachments] == [named.id]

    renamed = admin_client.repos.issues.assets.update(
        repo.owner,
        repo.name,
        issue.index,
        named.id,
        name="renamed-upload.txt",
    )
    assert renamed.name == "renamed-upload.txt"


def test_comment_attachment_round_trip(admin_client: pyfj.Forgejo, seed: Seed) -> None:
    repo = seed.repo_for("scenario-uploads-comment")
    issue = seed.issue(repo, "uploads")
    comment = admin_client.repos.issues.comments.create(repo.owner, repo.name, issue.index, body="attachment comment")
    assert comment.id is not None

    attachment = admin_client.repos.issues.comments.assets.create(
        repo.owner,
        repo.name,
        comment.id,
        attachment=("comment-upload.txt", b"comment attachment", "text/plain"),
    )
    assert attachment.id is not None
    listed = admin_client.repos.issues.comments.assets.list(repo.owner, repo.name, comment.id)
    assert [item.id for item in listed] == [attachment.id]
    admin_client.repos.issues.comments.assets.delete(repo.owner, repo.name, comment.id, attachment.id)
    assert admin_client.repos.issues.comments.assets.list(repo.owner, repo.name, comment.id) == []


def test_release_attachment_round_trip(admin_client: pyfj.Forgejo, seed: Seed) -> None:
    repo = seed.repo_for("scenario-uploads-release")
    release = admin_client.repos.releases.create(
        repo.owner,
        repo.name,
        tag_name="v9.9.9",
        name="upload release",
        target_commitish="main",
    )
    assert release.id is not None

    uploaded = admin_client.repos.releases.assets.create(
        repo.owner,
        repo.name,
        release.id,
        name="release-upload.zip",
        attachment=("release-upload.zip", b"PK\x03\x04", "application/zip"),
    )
    assert uploaded.id is not None
    assert uploaded.size == 4

    listed = admin_client.repos.releases.assets.list(repo.owner, repo.name, release.id)
    assert [item.id for item in listed] == [uploaded.id]
    fetched = admin_client.repos.releases.assets.get(repo.owner, repo.name, release.id, uploaded.id)
    assert fetched.name == "release-upload.zip"
