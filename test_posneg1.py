from positive_negative import positive_negative

def test_positive():
    assert positive_negative(5) == "Positive number"

def test_negative():
    assert positive_negative(-5) == "Negative number"

def test_zero():
    assert positive_negative(0) == "Zero"