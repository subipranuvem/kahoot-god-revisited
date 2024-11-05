import pytest
from unittest.mock import patch
from typing import List
from urllib.parse import ParseResult
from input.url_chooser import (
    URLChooser,
)


def test_choose_url_with_valid_input(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("builtins.input", lambda _: "https://example.com")
    monkeypatch.setattr("sys.argv", ["script_name"])

    result: str = URLChooser.choose_url()
    assert result == "https://example.com"


def test_choose_url_with_invalid_then_valid_input(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    inputs: List[str] = ["invalid_url", "https://example.com"]
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
    monkeypatch.setattr("sys.argv", ["script_name"])

    result: str = URLChooser.choose_url()
    assert result == "https://example.com"


def test_choose_url_with_command_line_arg(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("sys.argv", ["script_name", "https://example.com"])

    result: str = URLChooser.choose_url()
    assert result == "https://example.com"


def test_choose_url_with_invalid_command_line_arg(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr("sys.argv", ["script_name", "invalid_url"])

    with pytest.raises(ValueError, match="invalid url"):
        URLChooser.choose_url()


def test_choose_url_with_too_many_args(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("sys.argv", ["script_name", "https://example.com", "extra_arg"])

    with pytest.raises(ValueError, match="more than 1 arg informed"):
        URLChooser.choose_url()
