
def main():
    fraction = input("Fraction: ")
    percentage=convert(fraction)
    print(gauge(percentage))



def convert(fraction):
     a , b = fraction.split("/")
     if a>b and b!="0":
        raise(ValueError)
     elif not a.isdigit() or not b.isdigit():
         raise(ValueError)
     elif not a.isdigit() and not b.isdigit():
         raise(ValueError)
     elif b=="0":
         raise(ZeroDivisionError)
     else:
        percent=int(a)/int(b)*100
        return percent


def gauge(percentage):
    percent=percentage
    if 1<percent<99:
        percent = round(percent)
        return f"{percent}%"
    elif percent<=1:
        return "E"
    elif 99<=percent<=100:
        return "F"





if __name__ == "__main__":
    main()
