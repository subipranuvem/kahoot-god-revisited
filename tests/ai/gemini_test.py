import pytest
import os
from unittest.mock import Mock
from pytest_mock import MockerFixture
from ai.gemini import GeminiQuizSolver
from ai.env_var_keys import EnvironmentVarKey


@pytest.fixture
def gemini_api():
    os.environ[EnvironmentVarKey.GEMINI_API_KEY] = "mock_key"
    return GeminiQuizSolver()


def test_get_quiz_response(mocker: MockerFixture, gemini_api: GeminiQuizSolver) -> None:
    mock_generate_content: Mock = Mock()
    mock_generate_content.return_value.text = "2"
    mocker.patch.object(gemini_api._model, "generate_content", mock_generate_content)

    question: str = (
        "What is the capital of France?\n1. London\n2. Paris\n3. Berlin\n4. Madrid"
    )
    result: int = gemini_api.solve_quiz(question)

    assert result == 2
    mock_generate_content.assert_called_once()
    assert "You are a helpful assistant" in mock_generate_content.call_args[0][0]


def test_get_quiz_response_invalid_input(
    mocker: MockerFixture, gemini_api: GeminiQuizSolver
) -> None:
    mock_generate_content: Mock = Mock()
    mock_generate_content.return_value.text = "Invalid response"

    mocker.patch.object(gemini_api._model, "generate_content", mock_generate_content)

    question: str = (
        "What is the capital of Germany?\n1. Paris\n2. Berlin\n3. London\n4. Rome"
    )

    with pytest.raises(ValueError):
        gemini_api.solve_quiz(question)


def test_get_quiz_response_out_of_range(
    mocker: MockerFixture, gemini_api: GeminiQuizSolver
) -> None:
    mock_generate_content: Mock = Mock()
    mock_generate_content.return_value.text = "5"
    mocker.patch.object(gemini_api._model, "generate_content", mock_generate_content)
    question: str = (
        "What is the largest planet in our solar system?\n1. Earth\n2. Mars\n3. Jupiter\n4. Saturn"
    )

    with pytest.raises(ValueError):
        gemini_api.solve_quiz(question)
