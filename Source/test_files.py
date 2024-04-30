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


def test_division_integers():
    





# Test de la fonction 'isdigit'