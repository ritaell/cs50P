from bank import value
def main():
    test()

def test():
    assert value("Hello")==0
    assert value("hello")==0
    assert value("HELLO")==0
    assert value("How are you doing")==20
    assert value("how are you doing")==20
    assert value("goodmorning")==100

