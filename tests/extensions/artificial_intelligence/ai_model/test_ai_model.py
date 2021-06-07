from lime_python import Command
from pytest import fixture, mark
from pytest_mock import MockerFixture
from src import AiModelExtension
from ....utilities import async_return


class TestAiModelExtension:

    @fixture
    def target(self, mocker: MockerFixture) -> AiModelExtension:
        yield AiModelExtension(mocker.MagicMock())

    @mark.asyncio
    async def test_get_models(
        self,
        mocker: MockerFixture,
        target: AiModelExtension
    ) -> None:
        # Arrange
        expected_command = Command(
            'get',
            '/models?$skip=0&$take=100&$ascending=False'
        )

        mock = mocker.MagicMock(
            return_value=async_return(None)
        )
        target.client.process_command_async = mock

        # Act
        await target.get_models(0, 100, False)

        # Assert
        expected_command.id = mock.call_args[0][0].id
        mock.assert_called_once_with(expected_command)

    @mark.asyncio
    async def test_get_model(
        self,
        mocker: MockerFixture,
        target: AiModelExtension
    ) -> None:
        # Assert
        model_id = '1234'
        expected_command = Command(
            'get',
            '/model/1234'
        )

        mock = mocker.MagicMock(
            return_value=async_return(None)
        )

        target.client.process_command_async = mock

        # Act
        await target.get_model(model_id)

        # Assert
        expected_command.id = mock.call_args[0][0].id
        mock.assert_called_once_with(expected_command)

    @mark.asyncio
    async def test_get_model_summary(
        self,
        mocker: MockerFixture,
        target: AiModelExtension
    ) -> None:
        # Assert
        expected_command = Command(
            'get',
            '/models/summary'
        )

        mock = mocker.MagicMock(
            return_value=async_return(None)
        )

        target.client.process_command_async = mock

        # Act
        await target.get_model_summary()

        # Assert
        expected_command.id = mock.call_args[0][0].id
        mock.assert_called_once_with(expected_command)

    @mark.asyncio
    async def test_get_last_trained_or_published_model(
        self,
        mocker: MockerFixture,
        target: AiModelExtension
    ) -> None:
        # Assert
        expected_command = Command(
            'get',
            '/models/last-trained-or-published'
        )

        mock = mocker.MagicMock(
            return_value=async_return(None)
        )

        target.client.process_command_async = mock

        # Act
        await target.get_last_trained_or_published_model()

        # Assert
        expected_command.id = mock.call_args[0][0].id
        mock.assert_called_once_with(expected_command)

    @mark.asyncio
    async def test_train_model(
        self,
        mocker: MockerFixture,
        target: AiModelExtension
    ) -> None:
        # Assert
        expected_command = Command(
            'set',
            '/models',
            'application/vnd.iris.ai.model-training+json',
            {}
        )

        mock = mocker.MagicMock(
            return_value=async_return(None)
        )

        target.client.process_command_async = mock

        # Act
        await target.train_model()

        # Assert
        expected_command.id = mock.call_args[0][0].id
        mock.assert_called_once_with(expected_command)

    @mark.asyncio
    async def test_publish_model(
        self,
        mocker: MockerFixture,
        target: AiModelExtension
    ) -> None:
        # Assert
        model_id = '1234'
        command_resource = {
            'id': model_id
        }
        expected_command = Command(
            'set',
            '/models',
            'application/vnd.iris.ai.model-publishing+json',
            command_resource
        )

        mock = mocker.MagicMock(
            return_value=async_return(None)
        )

        target.client.process_command_async = mock

        # Act
        await target.publish_model(model_id)

        # Assert
        expected_command.id = mock.call_args[0][0].id
        mock.assert_called_once_with(expected_command)
