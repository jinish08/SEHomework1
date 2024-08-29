import pytest
from app import add_numbers, multiply_numbers

def test_add_numbers_pass():
    assert add_numbers(10, 5) == 15 

def test_add_numbers_fail():
    assert add_numbers(10, "5") == 15
