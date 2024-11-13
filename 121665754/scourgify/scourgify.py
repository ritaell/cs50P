import csv
import sys

def main():
    print(scourgify(sys.argv))



def scourgify(console):
    data=[]
    try:
        if len(console) < 3:
            sys.exit("Too few command-line arguments")
        elif len(console) > 3:
            sys.exit("Too many command-line arguments")
        elif sys.argv[1].rfind(".csv")==-1:
            sys.exit("Not a csv file")
        else:
            with open(sys.argv[1]) as before:
                reader=csv.DictReader(before)
                for row in reader:
                    house=row["house"]
                    last,first=row["name"].rstrip().split(",")
                    data.append(f"{first.strip()},{last.strip()},{house.strip()}")
            with open(sys.argv[2],"w") as after:
                after.write("first,last,house\n")
                for line in data:
                    after.write(f"{str(line)}\n")




    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")


if __name__=="__main__":
    main()
