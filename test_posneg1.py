from posneg1 import pos_neg

def test_positive():
    assert pos_neg(10) == "Positive number"

def test_negative():
    assert pos_neg(-5) == "Negative number"

def test_zero():
    assert pos_neg(0) == "Zero"
