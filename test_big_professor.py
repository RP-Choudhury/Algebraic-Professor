from project import answer_checker, equation
import pytest

def test_answer_checker():

    assert answer_checker(1.50,1.50) == True
    assert answer_checker(1.50,1.51) == False




def test_equation():

    eq1, x1 = equation('1')

    assert 'x' in eq1
    assert '=' in eq1



def test_equation_invalid_level():

    with pytest.raises(ValueError):
        equation("99")
