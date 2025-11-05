import pytest
from string_calculator import add


def test_add_empty_string():
    """Test that add returns 0 for an empty string"""
    assert add("") == 0