due = 50
while True:
    coin = int(input("incert coin "))

    if coin == 5 or coin == 10 or coin == 25:
        due = due - coin
        if due > 0:
          print(f"Amount Due: {due}")
          continue
        elif due < 0:
            print(f"Change Owed: {abs(due)}")
            break
        else:
            print("Change Owed: 0")
            break
    else:
        print(f"Amount Due: {due}")




