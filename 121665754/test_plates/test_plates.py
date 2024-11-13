import plates

def main():
    test()

def test():
    assert plates.is_valid("AAA222")==True
    assert plates.is_valid("AAA22A")==False
    assert plates.is_valid("CS03")==False
    assert plates.is_valid("H")==False
    assert plates.is_valid("CSAHS30")==False
    assert plates.is_valid("1BSH")==False
    assert plates.is_valid("CS5.0")==False
    assert plates.is_valid("A1BHS")==False
    assert plates.is_valid("12ABH")==False
    assert plates.is_valid("12123")==False

if __name__ == "__main__":
    main()
