from random import randint

def main():
    level=get_level()
    score = generate_integer(level)
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level=input("Level: ")
            if level != "1" and level != "2" and level!="3":
                continue
            else:
                break
        except EOFError:
            break
    return level



def generate_integer(level):
    score = 0
    for i in range(0,10):
        if level == "1":
            a = randint(0,9)
            b = randint(0,9)
            try:
                user=int(input(f"{a} + {b} = "))
                result=a+b
            except ValueError:
                user="str"
                result=a+b
            if user==result:
                score+=1
                continue
            else:
                print("EEE")
                for j in range(1,3):
                    try:
                        user=int(input(f"{a} + {b} = "))
                        result=a+b
                    except ValueError:
                        user="str"
                    if input == result:
                        score+=1
                    else:
                        print("EEE")
                        continue
                print(f"{a} + {b} = {result}")

        if level == "2":
            a = randint(10,99)
            b = randint(10,99)
            try:
                user=int(input(f"{a} + {b} = "))
                result=a+b
            except ValueError:
                user="str"
                result=a+b
            if user==result:
                score+=1
                continue
            else:
                print("EEE")
                for j in range(1,3):
                    try:
                        user=int(input(f"{a} + {b} = "))
                        result=a+b
                    except ValueError:
                        user="str"
                    if input == result:
                        score+=1
                    else:
                        print("EEE")
                        continue
                print(f"{a} + {b} = {result}")


        if level == "3":
            a = randint(100,999)
            b = randint(100,999)
            try:
                user=int(input(f"{a} + {b} = "))
                result=a+b
            except ValueError:
                user="str"
                result=a+b
            if user==result:
                score+=1
                continue
            else:
                print("EEE")
                for j in range(1,3):
                    try:
                        user=int(input(f"{a} + {b} = "))
                        result=a+b
                    except ValueError:
                        user="str"
                    if input == result:
                        score+=1
                    else:
                        print("EEE")
                        continue
                print(f"{a} + {b} = {result}")

    return score


if __name__ == "__main__":
    main()
