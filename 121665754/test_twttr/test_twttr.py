from twttr import shorten

def main():
    test()

def test():
    assert shorten("hello")=="hll"
    assert shorten("HELLO")=="HLL"
    assert shorten("hello, WORLD")=="hll, WRLD"
    assert shorten("50")=="50"
    assert shorten("F11")=="F11"
    assert shorten("_-.,")=="_-.,"

if __name__ == "__main__":
    main()

