# test_capitalize.py
import main

def capital_case(x):
    return x.capitalize()

def test_capital_case():
    assert capital_case('semaphore') == 'Semaphore'
    

def test_adder():
    assert adder(1,2) == 3
    assert adder(1,2) == 4
