import sys
from tabulate import tabulate
import csv



def main():
    print(menu(sys.argv))



def menu(console):
    data=[]
    try:
        if len(console) < 2:
            sys.exit("Too few command-line arguments")
        elif len(console) > 2:
            sys.exit("Too many command-line arguments")
        elif sys.argv[1].rfind(".csv")==-1:
            sys.exit("Not a csv file")
        else:
            with open(console[1]) as file:
                for line in file:
                    row=line.rstrip().split(",")
                    data.append(row)

    except FileNotFoundError:
        sys.exit("File does not exist")
    #return data
    return (tabulate(data, headers="firstrow" , tablefmt="grid"))

if __name__ == "__main__":
    main()
