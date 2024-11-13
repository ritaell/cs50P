# test_seasons.py

from seasons import Date

def tests():
    assert Date("2023-10-26").find_dif("2023-10-26") == "Five hundred twenty-seven thousand forty minutes", \
        "Failed for 1-year difference"


    assert Date("2022-10-26").find_dif("2022-10-26") == "One million, fifty-two thousand, six hundred forty minutes", \
        "Failed for 2-year difference"

    # Test with an invalid date format, expecting the program to exit
    try:
        Date("invalid-date")
    except SystemExit:
        pass  # Test passes if SystemExit is raised
    else:
        assert False, "Expected SystemExit for invalid date format"

def main():
    tests()
if __name__=="__main__":
    main()
