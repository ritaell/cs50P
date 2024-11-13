import sys
def main():
    print(loc())



def loc():
    if len(sys.argv)>2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv)<2:
        sys.exit("Too few command-line arguments")
    elif sys.argv[1].rfind(".py")==-1:
        sys.exit("Not a Python file")
    else:

        filename=sys.argv[1]
        lines=0
        stipped_line=""
        try:
            with open(filename, "r") as file:
                for line in file:
                    stripped_line = line.strip()
                    if stripped_line.startswith("#"):
                        continue  # Skip full-line comments
                    if "#" in stripped_line:
                        code_part = stripped_line.split("#", 1)[0].strip()
                        if code_part:  # Check if there's code before the comment
                            lines += 1
                    elif stripped_line:  # Non-empty line without #
                        lines += 1
        except FileNotFoundError:
                sys.exit("File does not exist")

    return str(lines)



if __name__=="__main__":
    main()
