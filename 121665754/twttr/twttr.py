
def notvow(vow):
    novow=""
    for i in vow:
        if i!="a" and i!="e" and i!="i" and i!="o" and i!="u" and i!="A" and i!="E" and i!="I" and i!="O" and i!="U" :
            novow += i
        elif i == " ":
            novow+=i
        else:
            novow+=""

    return novow

vowel=input("Input: ")
print(f"Output: {notvow(vowel)}")
