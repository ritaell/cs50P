def main():
    time_input  = input("what time is it? ")
    if 7.0 <= convert(time_input) <= 8.0:
      print("breakfast time")
    elif 12.0 <= convert(time_input) <= 13.0:
      print("lunch time")
    else:
     print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    minutes = int(minutes) / 60
    return float(hours) + minutes



if __name__ == "__main__":
    main()
