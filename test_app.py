import pytest
from app import add_numbers, multiply_numbers

def test_add_numbers_pass():
    assert add_numbers(10, 5) == 15 

def test_multiply_numbers_fail():
    assert multiply_numbers(10, "5") == 15