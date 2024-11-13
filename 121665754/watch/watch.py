import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):

    if matches := re.search(r"^<iframe.+src=\"https?://(?:www.)?youtu\.?be(?:.com)(/embed/[a-zA-Z0-9]+)\" ?.+</iframe>$",s):
        return f"https://youtu.be{matches.group(1).replace("/embed","")}"
    else:
        return None



if __name__ == "__main__":
    main()
