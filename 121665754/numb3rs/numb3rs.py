import re

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):

    # Check if the input matches the pattern for a valid IPv4 address
    if re.match(r"^([1-9][0-9]?|1[0-9]{2}|2[0-4][0-9]|25[0-5]|0)\.([1-9][0-9]?|1[0-9]{2}|2[0-4][0-9]|25[0-5]|0)\.([1-9][0-9]?|1[0-9]{2}|2[0-4][0-9]|25[0-5]|0)\.([1-9][0-9]?|1[0-9]{2}|2[0-4][0-9]|25[0-5]|0)$", ip):
        return True
    else:
        return False

if __name__ == "__main__":
    main()
