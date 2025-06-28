from year import *

def test_digits_1():
    assert digits(1) == [1]

def test_digits_12():
    assert digits(12) == [1, 2]

def test_digits_123():
    assert digits(123) == [1, 2, 3]

def test_eval_1987():
    assert eval(1987) == 2013

def test_eval_2013():
    assert eval(2013) == 2014
