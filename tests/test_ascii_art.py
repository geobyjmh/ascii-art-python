import sys

import ascii_art


def test_image_to_ascii_converts_image_to_text():
    art = ascii_art.image_to_ascii("images/rabbit.jpg", width=20)
    assert art.strip()
    assert "\n" in art


def test_main_reports_missing_file(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["ascii_art.py", "missing.jpg"])
    exit_code = ascii_art.main()
    captured = capsys.readouterr()
    assert exit_code == 1
    assert "Error" in captured.err
