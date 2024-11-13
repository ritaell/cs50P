choice = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
choice = choice.replace("-" , " ").strip().casefold()

match choice:
    case "42" | "forty two" :
        print("Yes")
    case _:
        print("No")

