import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    s=" "+s+" "
    ums=re.findall(r"[ |\.,]+um+[ |\.+,|\?]+",s,re.IGNORECASE)
    return len(ums)

if __name__ == "__main__":
    main()
