from calculator import calculate
import pytest

def test_simple_addition():
    assert calculate("2+3") == 5

def test_different_addition():
    assert calculate("1+7") == 8

def test_subtraction():
    assert calculate("5-2") == 3

def test_multiple_operations_same_priority():
    assert calculate("2+3+4") == 9
    assert calculate("8-3-1") == 4

def test_multiplication():
    assert calculate("2*3") == 6

def test_division():
    assert calculate("6/3") == 2

def test_priority_problem():
    assert calculate("2+3*4") == 14
    assert calculate("3+3/3") == 4

def test_parentheses():
    assert calculate("(2+3)*4") == 20

def test_invalid_characters():
    with pytest.raises(ValueError):
        calculate("2$3") 
        calculate("2a+3") 

def test_invalid_expression_structure():
    with pytest.raises(ValueError):
        calculate("2++3") 
        calculate("+3") 
        calculate("2+")  
        calculate("2 3") 
        calculate("2+3*4)") 
        calculate("(2+3*4") 
        calculate("(2+3*4))")  
        calculate("2+3(*4)") 
