"""Generated resource namespaces for the ``misc`` group. Do not edit by hand.

Regenerate with ``python -m codegen``; see docs/development/codegen.md.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from pyfj._generated.models.create_repo_option import CreateRepoOption
from pyfj._generated.models.gitignore_template_info import GitignoreTemplateInfo
from pyfj._generated.models.label_template import LabelTemplate
from pyfj._generated.models.license_template_info import LicenseTemplateInfo
from pyfj._generated.models.licenses_template_list_entry import LicensesTemplateListEntry
from pyfj._generated.models.markdown_option import MarkdownOption
from pyfj._generated.models.markup_option import MarkupOption
from pyfj._generated.models.node_info import NodeInfo
from pyfj._generated.models.repository import Repository
from pyfj._generated.models.server_version import ServerVersion
from pyfj._generated.models.topic_search_results import TopicSearchResults
from pyfj._runtime import decode

if TYPE_CHECKING:
    import builtins

    from pyfj._generated.models.create_repo_option import CreateRepoOptionObjectFormatName, CreateRepoOptionTrustModel
    from pyfj._runtime import AsyncForgejo as _RuntimeAsyncForgejo
    from pyfj._runtime import Forgejo as _RuntimeForgejo


class Misc:
    """The ``misc`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client
        self.gitignore: MiscGitignore = MiscGitignore(client)
        self.label: MiscLabel = MiscLabel(client)
        self.licenses: MiscLicenses = MiscLicenses(client)
        self.markdown: MiscMarkdown = MiscMarkdown(client)
        self.org: MiscOrg = MiscOrg(client)
        self.repositories: MiscRepositories = MiscRepositories(client)
        self.topics: MiscTopics = MiscTopics(client)

    def markup(
        self,
        *,
        branch_path: str | None = None,
        context: str | None = None,
        file_path: str | None = None,
        mode: str | None = None,
        text: str | None = None,
        wiki: bool | None = None,
    ) -> str:
        """
        Render a markup document as HTML.

        Args:
            branch_path: The current branch path where the form gets posted
            context: Context to render
            file_path: File path for detecting extension in file mode
            mode: Mode to render (comment, gfm, markdown, file)
            text: Text markup to render
            wiki: Is it a wiki page ?

        Returns:
            MarkupRender is a rendered markup document.

        Raises:
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: renderMarkup
        """
        if (
            branch_path is not None
            or context is not None
            or file_path is not None
            or mode is not None
            or text is not None
            or wiki is not None
        ):
            _payload = MarkupOption(
                branch_path=branch_path, context=context, file_path=file_path, mode=mode, text=text, wiki=wiki
            ).model_dump(mode="json", by_alias=True, exclude_none=True)
        else:
            _payload = None

        _response = self._client._request("POST", "/markup", json=_payload)
        return decode(_response, str)

    def nodeinfo(self) -> NodeInfo:
        """
        Returns the nodeinfo of the Forgejo application.

        Returns:
            NodeInfo.

        Operation ID: getNodeInfo
        """
        _response = self._client._request("GET", "/nodeinfo")
        return decode(_response, NodeInfo)

    def signing_key_gpg(self) -> str:
        """
        Get default signing-key.gpg.

        Returns:
            GPG armored public key.

        Operation ID: getSigningKey
        """
        _response = self._client._request("GET", "/signing-key.gpg")
        return decode(_response, str)

    def signing_key_ssh(self) -> str:
        """
        Get default signing-key.ssh.

        Returns:
            SSH public key in OpenSSH authorized key format.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: getSSHSigningKey
        """
        _response = self._client._request("GET", "/signing-key.ssh")
        return decode(_response, str)

    def version(self) -> ServerVersion:
        """
        Returns the version of the running application.

        Returns:
            ServerVersion.

        Operation ID: getVersion
        """
        _response = self._client._request("GET", "/version")
        return decode(_response, ServerVersion)


class AsyncMisc:
    """The ``misc`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client
        self.gitignore: AsyncMiscGitignore = AsyncMiscGitignore(client)
        self.label: AsyncMiscLabel = AsyncMiscLabel(client)
        self.licenses: AsyncMiscLicenses = AsyncMiscLicenses(client)
        self.markdown: AsyncMiscMarkdown = AsyncMiscMarkdown(client)
        self.org: AsyncMiscOrg = AsyncMiscOrg(client)
        self.repositories: AsyncMiscRepositories = AsyncMiscRepositories(client)
        self.topics: AsyncMiscTopics = AsyncMiscTopics(client)

    async def markup(
        self,
        *,
        branch_path: str | None = None,
        context: str | None = None,
        file_path: str | None = None,
        mode: str | None = None,
        text: str | None = None,
        wiki: bool | None = None,
    ) -> str:
        """
        Render a markup document as HTML.

        Args:
            branch_path: The current branch path where the form gets posted
            context: Context to render
            file_path: File path for detecting extension in file mode
            mode: Mode to render (comment, gfm, markdown, file)
            text: Text markup to render
            wiki: Is it a wiki page ?

        Returns:
            MarkupRender is a rendered markup document.

        Raises:
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: renderMarkup
        """
        if (
            branch_path is not None
            or context is not None
            or file_path is not None
            or mode is not None
            or text is not None
            or wiki is not None
        ):
            _payload = MarkupOption(
                branch_path=branch_path, context=context, file_path=file_path, mode=mode, text=text, wiki=wiki
            ).model_dump(mode="json", by_alias=True, exclude_none=True)
        else:
            _payload = None

        _response = await self._client._request("POST", "/markup", json=_payload)
        return decode(_response, str)

    async def nodeinfo(self) -> NodeInfo:
        """
        Returns the nodeinfo of the Forgejo application.

        Returns:
            NodeInfo.

        Operation ID: getNodeInfo
        """
        _response = await self._client._request("GET", "/nodeinfo")
        return decode(_response, NodeInfo)

    async def signing_key_gpg(self) -> str:
        """
        Get default signing-key.gpg.

        Returns:
            GPG armored public key.

        Operation ID: getSigningKey
        """
        _response = await self._client._request("GET", "/signing-key.gpg")
        return decode(_response, str)

    async def signing_key_ssh(self) -> str:
        """
        Get default signing-key.ssh.

        Returns:
            SSH public key in OpenSSH authorized key format.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: getSSHSigningKey
        """
        _response = await self._client._request("GET", "/signing-key.ssh")
        return decode(_response, str)

    async def version(self) -> ServerVersion:
        """
        Returns the version of the running application.

        Returns:
            ServerVersion.

        Operation ID: getVersion
        """
        _response = await self._client._request("GET", "/version")
        return decode(_response, ServerVersion)


class MiscGitignore:
    """The ``misc.gitignore`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client
        self.templates: MiscGitignoreTemplates = MiscGitignoreTemplates(client)


class AsyncMiscGitignore:
    """The ``misc.gitignore`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client
        self.templates: AsyncMiscGitignoreTemplates = AsyncMiscGitignoreTemplates(client)


class MiscGitignoreTemplates:
    """The ``misc.gitignore.templates`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def list(self) -> builtins.list[str]:
        """
        Returns a list of all gitignore templates.

        Returns:
            GitignoreTemplateList.

        Operation ID: listGitignoresTemplates
        """
        _response = self._client._request("GET", "/gitignore/templates")
        return decode(_response, list[str])

    def get(self, name: str) -> GitignoreTemplateInfo:
        """
        Returns information about a gitignore template.

        Args:
            name: name of the template

        Returns:
            GitignoreTemplateInfo.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: getGitignoreTemplateInfo
        """
        _response = self._client._request("GET", f"/gitignore/templates/{name}")
        return decode(_response, GitignoreTemplateInfo)


class AsyncMiscGitignoreTemplates:
    """The ``misc.gitignore.templates`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def list(self) -> builtins.list[str]:
        """
        Returns a list of all gitignore templates.

        Returns:
            GitignoreTemplateList.

        Operation ID: listGitignoresTemplates
        """
        _response = await self._client._request("GET", "/gitignore/templates")
        return decode(_response, list[str])

    async def get(self, name: str) -> GitignoreTemplateInfo:
        """
        Returns information about a gitignore template.

        Args:
            name: name of the template

        Returns:
            GitignoreTemplateInfo.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: getGitignoreTemplateInfo
        """
        _response = await self._client._request("GET", f"/gitignore/templates/{name}")
        return decode(_response, GitignoreTemplateInfo)


class MiscLabel:
    """The ``misc.label`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client
        self.templates: MiscLabelTemplates = MiscLabelTemplates(client)


class AsyncMiscLabel:
    """The ``misc.label`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client
        self.templates: AsyncMiscLabelTemplates = AsyncMiscLabelTemplates(client)


class MiscLabelTemplates:
    """The ``misc.label.templates`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def list(self) -> builtins.list[str]:
        """
        Returns a list of all label templates.

        Returns:
            LabelTemplateList.

        Operation ID: listLabelTemplates
        """
        _response = self._client._request("GET", "/label/templates")
        return decode(_response, list[str])

    def get(self, name: str) -> builtins.list[LabelTemplate]:
        """
        Returns all labels in a template.

        Args:
            name: name of the template

        Returns:
            LabelTemplateInfo.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: getLabelTemplateInfo
        """
        _response = self._client._request("GET", f"/label/templates/{name}")
        return decode(_response, list[LabelTemplate])


class AsyncMiscLabelTemplates:
    """The ``misc.label.templates`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def list(self) -> builtins.list[str]:
        """
        Returns a list of all label templates.

        Returns:
            LabelTemplateList.

        Operation ID: listLabelTemplates
        """
        _response = await self._client._request("GET", "/label/templates")
        return decode(_response, list[str])

    async def get(self, name: str) -> builtins.list[LabelTemplate]:
        """
        Returns all labels in a template.

        Args:
            name: name of the template

        Returns:
            LabelTemplateInfo.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: getLabelTemplateInfo
        """
        _response = await self._client._request("GET", f"/label/templates/{name}")
        return decode(_response, list[LabelTemplate])


class MiscLicenses:
    """The ``misc.licenses`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def list(self) -> builtins.list[LicensesTemplateListEntry]:
        """
        Returns a list of all license templates.

        Returns:
            LicenseTemplateList.

        Operation ID: listLicenseTemplates
        """
        _response = self._client._request("GET", "/licenses")
        return decode(_response, list[LicensesTemplateListEntry])

    def get(self, name: str) -> LicenseTemplateInfo:
        """
        Returns information about a license template.

        Args:
            name: name of the license

        Returns:
            LicenseTemplateInfo.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: getLicenseTemplateInfo
        """
        _response = self._client._request("GET", f"/licenses/{name}")
        return decode(_response, LicenseTemplateInfo)


class AsyncMiscLicenses:
    """The ``misc.licenses`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def list(self) -> builtins.list[LicensesTemplateListEntry]:
        """
        Returns a list of all license templates.

        Returns:
            LicenseTemplateList.

        Operation ID: listLicenseTemplates
        """
        _response = await self._client._request("GET", "/licenses")
        return decode(_response, list[LicensesTemplateListEntry])

    async def get(self, name: str) -> LicenseTemplateInfo:
        """
        Returns information about a license template.

        Args:
            name: name of the license

        Returns:
            LicenseTemplateInfo.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: getLicenseTemplateInfo
        """
        _response = await self._client._request("GET", f"/licenses/{name}")
        return decode(_response, LicenseTemplateInfo)


class MiscMarkdown:
    """The ``misc.markdown`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def render(
        self,
        *,
        context: str | None = None,
        mode: str | None = None,
        text: str | None = None,
        wiki: bool | None = None,
    ) -> str:
        """
        Render a markdown document as HTML.

        Args:
            context: Context to render
            mode: Mode to render (comment, gfm, markdown)
            text: Text markdown to render
            wiki: Is it a wiki page ?

        Returns:
            MarkdownRender is a rendered markdown document.

        Raises:
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: renderMarkdown
        """
        if context is not None or mode is not None or text is not None or wiki is not None:
            _payload = MarkdownOption(context=context, mode=mode, text=text, wiki=wiki).model_dump(
                mode="json", by_alias=True, exclude_none=True
            )
        else:
            _payload = None

        _response = self._client._request("POST", "/markdown", json=_payload)
        return decode(_response, str)

    def render_raw(self, *, body: str) -> str:
        """
        Render raw markdown as HTML.

        Returns:
            MarkdownRender is a rendered markdown document.

        Raises:
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: renderMarkdownRaw
        """
        _payload = body
        _response = self._client._request("POST", "/markdown/raw", json=_payload)
        return decode(_response, str)


class AsyncMiscMarkdown:
    """The ``misc.markdown`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def render(
        self,
        *,
        context: str | None = None,
        mode: str | None = None,
        text: str | None = None,
        wiki: bool | None = None,
    ) -> str:
        """
        Render a markdown document as HTML.

        Args:
            context: Context to render
            mode: Mode to render (comment, gfm, markdown)
            text: Text markdown to render
            wiki: Is it a wiki page ?

        Returns:
            MarkdownRender is a rendered markdown document.

        Raises:
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: renderMarkdown
        """
        if context is not None or mode is not None or text is not None or wiki is not None:
            _payload = MarkdownOption(context=context, mode=mode, text=text, wiki=wiki).model_dump(
                mode="json", by_alias=True, exclude_none=True
            )
        else:
            _payload = None

        _response = await self._client._request("POST", "/markdown", json=_payload)
        return decode(_response, str)

    async def render_raw(self, *, body: str) -> str:
        """
        Render raw markdown as HTML.

        Returns:
            MarkdownRender is a rendered markdown document.

        Raises:
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: renderMarkdownRaw
        """
        _payload = body
        _response = await self._client._request("POST", "/markdown/raw", json=_payload)
        return decode(_response, str)


class MiscOrg:
    """The ``misc.org`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def create_repo(
        self,
        org: str,
        *,
        auto_init: bool | None = None,
        default_branch: str | None = None,
        description: str | None = None,
        gitignores: str | None = None,
        issue_labels: str | None = None,
        license: str | None = None,
        name: str,
        object_format_name: CreateRepoOptionObjectFormatName | None = None,
        private: bool | None = None,
        readme: str | None = None,
        template: bool | None = None,
        trust_model: CreateRepoOptionTrustModel | None = None,
    ) -> Repository:
        """
        Create a repository in an organization.

        Args:
            org: name of organization
            auto_init: Whether the repository should be auto-initialized?
            default_branch: DefaultBranch of the repository (used when initializes and in template)
            description: Description of the repository to create
            gitignores: Gitignores to use, separated by commas
            issue_labels: Label-Set to use
            license: License to use
            name: Name of the repository to create
            object_format_name: ObjectFormatName of the underlying git repository
            private: Whether the repository is private
            readme: Readme of the repository to create
            template: Whether the repository is template
            trust_model: TrustModel of the repository

        Returns:
            Repository.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Deprecated:
            Deprecated in the vendored Spec; generated for compatibility.

        Operation ID: createOrgRepoDeprecated
        """
        _payload = CreateRepoOption(
            auto_init=auto_init,
            default_branch=default_branch,
            description=description,
            gitignores=gitignores,
            issue_labels=issue_labels,
            license=license,
            name=name,
            object_format_name=object_format_name,
            private=private,
            readme=readme,
            template=template,
            trust_model=trust_model,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = self._client._request("POST", f"/org/{org}/repos", json=_payload)
        return decode(_response, Repository)


class AsyncMiscOrg:
    """The ``misc.org`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def create_repo(
        self,
        org: str,
        *,
        auto_init: bool | None = None,
        default_branch: str | None = None,
        description: str | None = None,
        gitignores: str | None = None,
        issue_labels: str | None = None,
        license: str | None = None,
        name: str,
        object_format_name: CreateRepoOptionObjectFormatName | None = None,
        private: bool | None = None,
        readme: str | None = None,
        template: bool | None = None,
        trust_model: CreateRepoOptionTrustModel | None = None,
    ) -> Repository:
        """
        Create a repository in an organization.

        Args:
            org: name of organization
            auto_init: Whether the repository should be auto-initialized?
            default_branch: DefaultBranch of the repository (used when initializes and in template)
            description: Description of the repository to create
            gitignores: Gitignores to use, separated by commas
            issue_labels: Label-Set to use
            license: License to use
            name: Name of the repository to create
            object_format_name: ObjectFormatName of the underlying git repository
            private: Whether the repository is private
            readme: Readme of the repository to create
            template: Whether the repository is template
            trust_model: TrustModel of the repository

        Returns:
            Repository.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Deprecated:
            Deprecated in the vendored Spec; generated for compatibility.

        Operation ID: createOrgRepoDeprecated
        """
        _payload = CreateRepoOption(
            auto_init=auto_init,
            default_branch=default_branch,
            description=description,
            gitignores=gitignores,
            issue_labels=issue_labels,
            license=license,
            name=name,
            object_format_name=object_format_name,
            private=private,
            readme=readme,
            template=template,
            trust_model=trust_model,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = await self._client._request("POST", f"/org/{org}/repos", json=_payload)
        return decode(_response, Repository)


class MiscRepositories:
    """The ``misc.repositories`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def get(self, id: int) -> Repository:
        """
        Get a repository by id.

        Args:
            id: id of the repo to get

        Returns:
            Repository.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoGetByID
        """
        _response = self._client._request("GET", f"/repositories/{id}")
        return decode(_response, Repository)


class AsyncMiscRepositories:
    """The ``misc.repositories`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def get(self, id: int) -> Repository:
        """
        Get a repository by id.

        Args:
            id: id of the repo to get

        Returns:
            Repository.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: repoGetByID
        """
        _response = await self._client._request("GET", f"/repositories/{id}")
        return decode(_response, Repository)


class MiscTopics:
    """The ``misc.topics`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def search(self, *, q: str, page: int | None = None, limit: int | None = None) -> TopicSearchResults:
        """
        Search for topics by keyword.

        Args:
            q: keyword to search for
            page: page number of results to return (1-based)
            limit: page size of results

        Returns:
            SearchResults of a successful search.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: topicSearch
        """
        _query: dict[str, object] = {"q": q, "page": page, "limit": limit}

        _response = self._client._request("GET", "/topics/search", params=_query)
        return decode(_response, TopicSearchResults)


class AsyncMiscTopics:
    """The ``misc.topics`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def search(self, *, q: str, page: int | None = None, limit: int | None = None) -> TopicSearchResults:
        """
        Search for topics by keyword.

        Args:
            q: keyword to search for
            page: page number of results to return (1-based)
            limit: page size of results

        Returns:
            SearchResults of a successful search.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: topicSearch
        """
        _query: dict[str, object] = {"q": q, "page": page, "limit": limit}

        _response = await self._client._request("GET", "/topics/search", params=_query)
        return decode(_response, TopicSearchResults)
