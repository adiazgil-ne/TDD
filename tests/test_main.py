# -*- coding: utf-8 -*-
from calculator.main import Calc
import pytest

def test_add_two_numbers():
    calculator = Calc() # Instantation
    
    result = calculator.add(2, 3)
    
    assert result == 5
    
def test_add_three_numbers():
    calculator = Calc() # Instantation
    
    result = calculator.add(2, 3,4)
    
    assert result == 9

def test_add_many_numbers():
    numbers = range(1,100)
    calculator = Calc() # Instantation
    
    result = calculator.add(*numbers)
    
    assert result == 4950
    
def test_subtract_two_numbers():
    calculator = Calc() # Instantation
    
    result = calculator.sub(10, 4)
    
    assert result == 6
    
def test_divide_two_numbers():
    calculator = Calc() # Instantation
    
    result = calculator.div(10,4)
    
    assert result == 2.5
    
def test_divide_by_zero():
    calculator = Calc() # Instantation
    
    with pytest.raises(ValueError):
        calculator.div(10,0)