import pytest
from string_calculator import add


def test_add_empty_string():
    """Test that add returns 0 for an empty string"""
    assert add("") == 0

def test_add_single_number():
    """Test that add returns the number for a single number"""
    assert add("1") == 1

def test_add_two_numbers():
    """Test that add returns the sum for two comma-separated numbers"""
    assert add("1,5") == 6

def test_add_multiple_numbers():
    """Test that add handles any amount of numbers"""
    assert add("1,2,3,4,5") == 15
    assert add("10,20,30") == 60

def test_add_with_newlines():
    """Test that add handles newlines between numbers"""
    assert add("1\n2,3") == 6
    assert add("1\n2\n3") == 6

def test_add_custom_delimiter():
    """Test that add supports custom delimiters"""
    assert add("//;\n1;2") == 3
    assert add("//|\n1|2|3") == 6
    assert add("//@\n10@20") == 30

def test_add_negative_number_single():
    """Test that add throws exception for a single negative number"""
    with pytest.raises(ValueError) as exc_info:
        add("-1")
    assert "negative numbers not allowed -1" in str(exc_info.value) 

def test_add_negative_numbers_multiple():
    """Test that add shows all negative numbers in exception message"""
    with pytest.raises(ValueError) as exc_info:
        add("-1,-2,3")
    assert "negative numbers not allowed" in str(exc_info.value)
    assert "-1" in str(exc_info.value)
    assert "-2" in str(exc_info.value)