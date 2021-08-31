import pathlib
from main_task import get_content
import pytest


def test_get_content():
    url = "https://www.google.co.uk"
    soup = get_content(url)
    assert "https://" in url