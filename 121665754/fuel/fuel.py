
def main():
    per = get_fraction()
    print(per)

def get_fraction():
    while True:
        try:
            fraction = input("Fraction: ")
            a , b = fraction.split("/")
            percent=int(a)/int(b)*100
            if 1<percent<99:
                percent = round(percent)
                return f"{percent}%"
            elif percent<=1:
                return "E"
            elif 99<=percent<=100:
                return "F"
            elif percent>100:
                continue
            break
        except ValueError:
            pass
        except ZeroDivisionError:
            pass


main()
