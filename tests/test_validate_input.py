import pytest
from delivery_input_validation import validate_input

def test_validate_input_all_invalid():
    test_error_dict = validate_input(50,50,60)

    assert len(test_error_dict) == 3

def test_validate_input_price_invalid():
    errors = validate_input(10, 100, 5)
    assert "price" in errors
    assert "distance" not in errors
    assert "duration" not in errors

def test_validate_duration_invalid():
    errors = validate_input(20, 10, 100)

    assert "price" not in errors
    assert "duration" in errors
    assert "distance" not in errors

