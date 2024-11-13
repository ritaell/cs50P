from fuel import convert,gauge
from pytest import raises
def main():
    test_convert()

def test_convert():
    assert convert("3/4")==75
    assert convert("1/4")==25
    assert convert("4/4")==100
    assert convert("0/4")==0
    with raises(ValueError):
        convert("5/4")
    with raises(ZeroDivisionError):
        convert("4/0")
    with raises(ValueError):
        convert("cat/dog")==""
    with raises(ValueError):
        convert("5/4")

def test_gauge():
    assert gauge(75)=="75%"
    assert gauge(25)=="25%"
    assert gauge(100)=="F"
    assert gauge(99)=="F"
    assert gauge(1)=="E"
    assert gauge(0)=="E"


