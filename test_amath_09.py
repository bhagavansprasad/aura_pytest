import pytest

def test_a():
    print("Hai : a")

def test_b():
    print("Hai : b")

def test_c():
    a = 10
    b = 20
    if (a == b):
        print("Same")
    else:
        print("Not Same")

def test_d():
    a = 10
    b = 20
    assert a == b

def test_e():
    a = 10
    b = 20
    assert a == b, f"A:{a} and B:{b} are not same"

@pytest.mark.parametrize("x", [4, 5, 10])
def test_f(x):
    a = 10
    assert a == x, f"A:{a} and x:{x} are not same"
