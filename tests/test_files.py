from Source.addition import addition
from Source.division import division_func
from Source.multiplication import multiplication_func
from Source.soustraction import soustraction
import pytest

# Test de la fonction addition:

def test_addition_integers():
    assert addition(10, 10) == 20
    assert addition(3.4, 3.2) == 6.6
    assert addition(2.5, 2.5) == 5
    assert addition(-1, 1) == 0
    assert addition(-5, -5) == -10
    assert addition(9000000, 20000000) == 29000000

#Test de la fonction division: 
def test_division_integers():
    assert division_func(1,1) == 1
    assert division_func(1,2) == 0.5
    assert division_func(2.2,2) == 1.1

def test_divide_zero():
    with pytest.raises(ZeroDivisionError):
        division_func(8,0)


# Test de la fonction multiplication:
def test_multiplication_integers():
    assert multiplication_func(10, 10) == 100
    assert multiplication_func(3.4, 3.2) == 10.88
    assert multiplication_func(2.5, 2.5) == 6.25
    assert multiplication_func(-1, 1) == -1
    assert multiplication_func(-5, -5) == 25
    assert multiplication_func(9000000, 20000000) == 180000000000000


# Test de la fonction soustraction:
def test_soustraction():
    assert soustraction(10, 10) == 0
    assert soustraction(3.4, 3.2) == 0.2
    assert soustraction(2.5, 2.5) == 0
    assert soustraction(-1, 1) == -2
    assert soustraction(-5, -5) == 0
    assert soustraction(9000000, 20000000) == -11000000




# Test de la fonction 'isdigit'