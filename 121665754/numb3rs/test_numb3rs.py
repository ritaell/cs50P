from numb3rs import validate

def main():
    test_range()
    test_format()

def test_format():
    assert validate("1.2.3.4.5")==False
    assert validate("1.2.3.4")==True
    assert validate("1.2.3")==False
    assert validate("1.2")==False
    assert validate("1")==False
    assert validate("666.666.666.666.666")==False

def test_range():
    assert validate("255.255.255.255")==True
    assert validate("512.1.1.1")==False
    assert validate("1.512.1.1")==False
    assert validate("1.1.512.1")==False
    assert validate("1.1.1.512")==False
    assert validate("555.555.555.555")==False

if __name__=="__main__":
    main()
