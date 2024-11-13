from random import randint
from sys import exit

while True:
    try:
        level = int(input("Level: "))
        if level<=0:
            continue
        else:
            break
    except EOFError:
        break
    except ValueError:
        pass


number=randint(1,level)


while True:
    try:
        guess= int(input("Guess: "))
        if guess<=0:
            continue
        else:
            break
    except EOFError:
        break
    except ValueError:
        pass

while True:
    try:
        if guess>number:
            print("Too large!")
            continue
        elif guess<number:
            print("Too small!")
            continue
        else:
            sys.exit("Just right!")
    except EOFError:
        break

