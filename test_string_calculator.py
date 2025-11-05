import pytest
from string_calculator import add


def test_add_empty_string():
    """Test that add returns 0 for an empty string"""
    assert add("") == 0

def test_add_single_number():
    """Test that add returns the number for a single number"""
    assert add("1") == 1