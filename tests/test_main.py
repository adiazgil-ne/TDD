# -*- coding: utf-8 -*-
from calculator.main import Calc

def test_add_two_numbers():
    calculator = Calc() # Instantation
    
    result = calculator.add(2, 3)
    
    assert result == 5