greeting = input("Greeting: ").strip().rstrip()

match greeting:
   case "Hello" | "Hello, Newman":
       print("$0")
   case "Hey" | "How you doing?":
       print("$20")
   case _:
       print("$100")

