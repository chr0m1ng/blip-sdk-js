from lime_python import Command, ContentTypes
from ...extension_base import ExtensionBase
from .content_type import ContentType
from .uri_templates import UriTemplates

POSTMASTER_AI = 'postmaster@ai'


class ContentAssistantExtension(ExtensionBase):
    """Extension to handle Content Assistant Services."""

    async def analyse_content(self, analysis: dict) -> Command:
        """Analyse content.

        Args:
            analysis (dict): Content Analysis object

        Returns:
            Command: Command response
        """
        return await self.process_command_async(
            self.create_set_command(
                UriTemplates.CONTENT_ANALYSIS,
                analysis,
                ContentType.ANALYSIS
            )
        )

    async def match_content(self, combination: dict) -> Command:
        """Match content.

        Args:
            combination (dict): combination object

        Returns:
            Command: Command response
        """
        return await self.process_command_async(
            self.create_set_command(
                UriTemplates.CONTENT_ANALYSIS,
                combination,
                ContentType.CONTENT_COMBINATION
            )
        )

    async def get_contents(
        self,
        skip: int = 0,
        take: int = 100,
        ascending: bool = False,
        intents: str = None,
        entities: str = None,
        text: str = None,
        begin_date: str = None,
        end_date: str = None
    ) -> Command:
        """Get contents.

        Args:
            skip (int): Number of contents to be skipped.
            take (int): Number of contents to be take.
            ascending (bool): Sets ascending alphabetical order..
            intents (str): Intents list.
            entities (str): Entities list.
            text (str): text.
            begin_date (str): begin date of contents.
            end_date (str): end date of contents.

        Returns:
            Command: Command response
        """
        contents_resource_query = self.build_resource_query(
            UriTemplates.CONTENT,
            {
                '$skip': skip,
                '$take': take,
                '$ascending': ascending,
                'intents': intents,
                'entities': entities,
                'text': text,
                'beginDate': begin_date,
                'endDate': end_date
            }
        )

        return await self.process_command_async(
            self.create_get_command(contents_resource_query)
        )

    async def get_content(self, id: str) -> Command:
        """Get content.

        Args:
            id (str): Content id

        Returns:
            Command: Command response
        """
        return await self.process_command_async(
            self.create_get_command(
                self.build_uri(UriTemplates.CONTENT_ID, id)
            )
        )

    async def set_content(self, content: dict) -> Command:
        """Create content combination.

        Args:
            content (dict): Content object

        Returns:
            Command: Command response
        """
        return await self.process_command_async(
            self.create_set_command(
                UriTemplates.CONTENT,
                content,
                ContentType.CONTENT_RESULT
            )
        )

    async def set_content_result(self, id: str, content: dict) -> Command:
        """Set content result.

        Args:
            id (str): Content id.
            content (dict): Content object.

        Returns:
            Command: Command response
        """
        content_result_command = self.create_set_command(
            self.build_uri(UriTemplates.CONTENT_ID, id),
            content,
            ContentType.CONTENT_RESULT
        )

        return await self.process_command_async(content_result_command)

    async def set_content_combination(
        self,
        id: str,
        combination: dict
    ) -> Command:
        """Set content combination.

        Args:
            id (str): Combination id
            combination (dict): Combination object

        Returns:
            Command: Command response
        """
        return await self.process_command_async(
            self.create_set_command(
                self.build_uri(UriTemplates.CONTENT_ID, id),
                combination,
                ContentType.CONTENT_COMBINATION
            )
        )

    async def set_content_combinations(
        self,
        id: str,
        combinations=list
    ) -> Command:
        """Set list of combinations.

        Args:
            id (str): Combinations id.
            combinations (list, optional): Combinations list.

        Returns:
            Command: Command response
        """
        combinations_command = self.create_set_command(
            self.build_uri(UriTemplates.CONTENT_ID, id),
            type_n=ContentTypes.COLLECTION,
            resource={
                'itemType': ContentType.CONTENT_COMBINATION,
                'items': combinations
            }
        )

        return await self.process_command_async(combinations_command)

    async def delete_content(self, id: str) -> Command:
        """Delete content.

        Args:
            id (str): Content id

        Returns:
            Command: Command response
        """
        return await self.process_command_async(
            self.create_delete_command(
                self.build_uri(UriTemplates.CONTENT_ID, id)
            )
        )
