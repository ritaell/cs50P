import validators
import sys


def main():
    print(isvalid(input("What is your email address? ")))


def isvalid(s):
    if validators.email(s):
        return "Valid"
    else:
        return "Invalid"

if __name__=="__main__":
    main()
