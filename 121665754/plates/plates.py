def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Check the length of the plate
    if not (2 <= len(s) <= 6):
        return False

    # Check if the plate starts with at least two letters
    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    # Check for invalid characters (only letters and numbers are allowed)
    for char in s:
        if not (char.isalnum()):
            return False

    # Find the first digit, if any, and check the rest
    has_digit = False
    for i, char in enumerate(s):
        if char.isdigit():
            has_digit = True
            # Numbers must come at the end
            if not s[i:].isdigit():
                return False
            # The first number used cannot be '0'
            if char == '0':
                return False
            break

    return True



main()
