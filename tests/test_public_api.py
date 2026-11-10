"""Tests for the public API of repo_pulse."""

import repo_pulse


def test_analyze_is_exposed() -> None:
    assert hasattr(repo_pulse, "analyze"), "analyze() must be part of the public API"


def test_analyze_returns_dict_for_empty_input() -> None:
    result = repo_pulse.analyze([])
    assert isinstance(result, dict)


def test_all_declares_public_names() -> None:
    assert hasattr(repo_pulse, "__all__")
    assert "analyze" in repo_pulse.__all__