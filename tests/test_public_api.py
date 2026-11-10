def test_analyze_is_importable() -> None:
    from repo_pulse import analyze
    assert callable(analyze)