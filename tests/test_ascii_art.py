"""Tests for the ASCII art CLI prototype."""

import sys

import pytest
from PIL import Image

import ascii_art


def test_image_to_ascii_converts_image_to_text():
    """A standard image should render to non-empty ASCII text."""
    art = ascii_art.image_to_ascii("images/rabbit.jpg", width=20)
    assert art.strip()
    assert "\n" in art


def test_image_to_ascii_supports_rotation():
    """Rotation should not break conversion output."""
    art = ascii_art.image_to_ascii("images/rabbit.jpg", width=20, rotate=90)
    assert art.strip()
    assert "\n" in art


def test_image_to_ascii_rejects_non_positive_width():
    """A width of zero should be rejected before processing starts."""
    with pytest.raises(ValueError, match="width"):
        ascii_art.image_to_ascii("images/rabbit.jpg", width=0)


def test_rotate_image_rejects_invalid_angle():
    """Unsupported angles should raise a clear error."""
    with pytest.raises(ValueError, match="rotate"):
        ascii_art.rotate_image(Image.new("L", (10, 10), 0), 45)


def test_main_reports_missing_file(monkeypatch, capsys):
    """A missing input path should return a non-zero exit code and a clear message."""
    monkeypatch.setattr(sys, "argv", ["ascii_art.py", "missing.jpg"])
    exit_code = ascii_art.main()
    captured = capsys.readouterr()
    assert exit_code == 1
    assert "Error" in captured.err


def test_main_reports_invalid_width(monkeypatch, capsys):
    """Non-positive widths should be rejected by the CLI."""
    monkeypatch.setattr(sys, "argv", ["ascii_art.py", "images/rabbit.jpg", "--width", "0"])
    exit_code = ascii_art.main()
    captured = capsys.readouterr()
    assert exit_code == 1
    assert "width" in captured.err
