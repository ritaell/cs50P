def main():
    word=input("Input: ")
    print(f"Output: {shorten(word)}")


def shorten(word):
    novow=""
    for i in word:
        if i not in "AEIOUaeiou" and  i in ".,':;?!":
            novow += i
        elif i == " ":
            novow+=i
        else:
            novow+=""

    return novow


if __name__ == "__main__":
    main()
