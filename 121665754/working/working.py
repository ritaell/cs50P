import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.match(r"([1-9]|1[0-2])(\:[0-5][0-9])? (AM|PM) to ([1-9]|1[0-2])(\:[0-5][0-9])? (AM|PM)",s):
        h1=matches.group(1)
        m1=matches.group(2)
        h2=matches.group(4)
        m2=matches.group(5)
        if m1==None:
            m1=":00"
        if m2==None:
            m2=":00"
        if h1=="12" and matches.group(3)=="AM":
            h1="00"
        elif h2=="12" and matches.group(6)=="AM":
            h1="00"
        if h1!="12" and matches.group(3)=="PM":
            h1=12+int(h1)
        if h2!="12" and matches.group(6)=="PM":
            h2=12+int(h2)
        if len(str(h1))==1 and matches.group(3)=="AM":
            h1=f"0{h1}"
        if len(str(h2))==1 and matches.group(6)=="AM":
            h2=f"0{h2}"
        return f"{h1}{m1} to {h2}{m2}"


    else:
        raise ValueError

if __name__ == "__main__":
    main()
