"""Async mirror of the public surface: auth modes, journeys, errors, uploads."""

from __future__ import annotations

import asyncio
from typing import TYPE_CHECKING

import httpx
import pytest
from harness import ADMIN_PASSWORD, ADMIN_USERNAME, USER_USERNAME

import pyfj

if TYPE_CHECKING:
    from harness import ForgejoServer, Seed

pytestmark = pytest.mark.integration


async def test_async_basic_auth(server: ForgejoServer) -> None:
    async with pyfj.AsyncForgejo(server.base_url, auth=(ADMIN_USERNAME, ADMIN_PASSWORD)) as client:
        assert (await client.user.get()).login == ADMIN_USERNAME


async def test_async_sudo_switches_the_actor(server: ForgejoServer) -> None:
    async with pyfj.AsyncForgejo(server.base_url, token=server.admin_token, sudo=USER_USERNAME) as client:
        assert (await client.user.get()).login == USER_USERNAME
        # An override wins over the client default; the async scope restores it.
        async with client.sudo_as(ADMIN_USERNAME):
            assert (await client.user.get()).login == ADMIN_USERNAME
        assert (await client.user.get()).login == USER_USERNAME


async def test_async_sudo_is_context_local(server: ForgejoServer) -> None:
    """Concurrent tasks on one client each impersonate their own user."""
    async with pyfj.AsyncForgejo(server.base_url, token=server.admin_token) as client:

        async def whoami(username: str) -> str:
            async with client.sudo_as(username):
                await asyncio.sleep(0)
                login = (await client.user.get()).login
                assert login is not None
                return login

        alice, root = await asyncio.gather(whoami(USER_USERNAME), whoami(ADMIN_USERNAME))
        assert alice == USER_USERNAME
        assert root == ADMIN_USERNAME
        assert (await client.user.get()).login == ADMIN_USERNAME


async def test_async_anonymous_errors_and_client_injection(server: ForgejoServer) -> None:
    async with pyfj.AsyncForgejo(server.base_url) as anonymous:
        assert (await anonymous.misc.version()).version
        with pytest.raises(pyfj.UnauthorizedError):
            await anonymous.user.get()

    async with httpx.AsyncClient() as injected:
        client = pyfj.AsyncForgejo(server.base_url, token=server.admin_token, client=injected)
        try:
            assert (await client.user.get()).login == ADMIN_USERNAME
            with pytest.raises(TypeError, match="injected httpx client"):
                pyfj.AsyncForgejo(server.base_url, client=injected, timeout=5.0)
        finally:
            await client.aclose()


async def test_async_repository_and_issue_journey(async_admin_client: pyfj.AsyncForgejo, seed: Seed) -> None:
    name = seed.name("repo", "async-scenario")
    repo = await async_admin_client.orgs.repos.create(seed.org, name=name, auto_init=True)
    try:
        assert repo.full_name == f"{seed.org}/{name}"
        assert repo.default_branch == "main"

        issue = await async_admin_client.repos.issues.create(seed.org, name, title="async issue", body="async body")
        assert issue.number is not None
        fetched = await async_admin_client.repos.issues.get(seed.org, name, issue.number)
        assert fetched.title == "async issue"

        comment = await async_admin_client.repos.issues.comments.create(
            seed.org,
            name,
            issue.number,
            body="async comment",
        )
        assert comment.id is not None
        comments = await async_admin_client.repos.issues.comments.list(seed.org, name, issue.number)
        assert [item.id for item in comments] == [comment.id]

        attachment = await async_admin_client.repos.issues.assets.create(
            seed.org,
            name,
            issue.number,
            attachment=("async-upload.txt", b"async attachment", "text/plain"),
        )
        assert attachment.size == len(b"async attachment")
    finally:
        await async_admin_client.repos.delete(seed.org, name)


async def test_async_pull_request_flow(
    async_admin_client: pyfj.AsyncForgejo,
    async_user_client: pyfj.AsyncForgejo,
    seed: Seed,
) -> None:
    repo = seed.repo_for("async-pull")
    await async_admin_client.repos.contents.create(
        repo.owner,
        repo.name,
        "async-pull.txt",
        content="YXN5bmMgcHVsbA==",
        message="add async pull file",
        new_branch="async-pull",
    )
    pull = await async_admin_client.repos.pulls.create(
        repo.owner,
        repo.name,
        title="Async pull",
        head="async-pull",
        base="main",
    )
    assert pull.number is not None
    listed = await async_admin_client.repos.pulls.list(repo.owner, repo.name, state="open")
    page = await listed.page(1)
    assert [item.number for item in page] == [pull.number]

    await async_admin_client.repos.collaborators.add(
        repo.owner,
        repo.name,
        seed.user,
        permission=pyfj.AddCollaboratorOptionPermission.WRITE,
    )
    review = await async_user_client.repos.pulls.reviews.create(
        repo.owner,
        repo.name,
        pull.number,
        body="async review",
        event="APPROVED",
    )
    assert review.state == "APPROVED"

    await async_admin_client.repos.pulls.merge(
        repo.owner,
        repo.name,
        pull.number,
        do=pyfj.MergePullRequestOptionDo.MERGE,
    )
    merged = await async_admin_client.repos.pulls.get(repo.owner, repo.name, pull.number)
    assert merged.merged is True


async def test_async_org_and_team_membership(async_admin_client: pyfj.AsyncForgejo, seed: Seed) -> None:
    org = seed.org_for("async-scenario")
    member = seed.user_for("async-member")

    team = await async_admin_client.orgs.teams.create(
        org,
        name=seed.name("team", "async"),
        units=["repo.code", "repo.issues"],
    )
    assert team.id is not None
    await async_admin_client.teams.members.add(team.id, member)
    members = await async_admin_client.teams.members.list(team.id)
    member_page = await members.page(1)
    assert [user.login for user in member_page] == [member]
    permissions = await async_admin_client.users.orgs.permissions(member, org)
    assert permissions is not None
    await async_admin_client.teams.members.remove(team.id, member)


async def test_async_errors_are_mapped(async_admin_client: pyfj.AsyncForgejo) -> None:
    with pytest.raises(pyfj.NotFoundError) as caught:
        await async_admin_client.repos.get("pyfj-does-not-exist", "pyfj-does-not-exist")
    assert caught.value.status_code == 404


async def test_async_escape_hatch(async_admin_client: pyfj.AsyncForgejo) -> None:
    response = await async_admin_client.request("GET", "/version")
    assert response.status_code == 200
