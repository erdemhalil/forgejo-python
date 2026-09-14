"""Organization and team membership lifecycle."""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

import pyfj

if TYPE_CHECKING:
    from harness import Seed

pytestmark = pytest.mark.integration


def test_org_and_team_lifecycle(admin_client: pyfj.Forgejo, seed: Seed) -> None:
    org = seed.org_for("scenario")
    member = seed.user_for("scenario-member")

    organization = admin_client.orgs.get(org)
    assert organization.username == org

    edited = admin_client.orgs.update(org, description="scenario organization")
    assert edited.description == "scenario organization"

    team = admin_client.orgs.teams.create(org, name=seed.name("team", "scenario"), units=["repo.code", "repo.issues"])
    assert team.id is not None
    repo = seed.repo_for("scenario-team-repo", owner=org)

    try:
        admin_client.teams.members.add(team.id, member)
        members = admin_client.teams.members.list(team.id)
        assert [user.login for user in members.page(1)] == [member]
        assert admin_client.teams.members.get(team.id, member).login == member

        admin_client.teams.repos.add(team.id, org, repo.name)
        team_repos = admin_client.teams.repos.list(team.id)
        assert [item.name for item in team_repos.page(1)] == [repo.name]
        assert admin_client.teams.repos.get(team.id, org, repo.name).name == repo.name
        assert team.name is not None
        assert admin_client.repos.teams.get(org, repo.name, team.name).id == team.id

        permissions = admin_client.users.orgs.permissions(member, org)
        assert permissions is not None

        # Public membership is self-service: act as the member through sudo.
        with admin_client.sudo_as(member):
            admin_client.orgs.public_members.publicize(org, member)
        public_members = admin_client.orgs.public_members.list(org)
        assert member in [user.login for user in public_members.page(1)]
        with admin_client.sudo_as(member):
            admin_client.orgs.public_members.conceal(org, member)

        # Blocking and unblocking.
        member_id = admin_client.users.get(member).id
        assert member_id is not None
        admin_client.orgs.block(org, member)
        blocked = admin_client.orgs.list_blocked(org)
        assert member_id in [user.block_id for user in blocked.page(1)]
        admin_client.orgs.unblock(org, member)

        admin_client.teams.members.remove(team.id, member)
        admin_client.teams.repos.remove(team.id, org, repo.name)
    finally:
        admin_client.teams.delete(team.id)
        admin_client.repos.delete(org, repo.name)

    # The organization has no repositories left, so it can be deleted.
    admin_client.orgs.delete(org)
    with pytest.raises(pyfj.NotFoundError):
        admin_client.orgs.get(org)
