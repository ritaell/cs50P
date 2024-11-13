user_input = input("Expression: ").rstrip().strip()
x , action , y = user_input.split(" ")

if action == "+":
    print(float(x) + float(y))
if action == "-":
    print(float(x) - float(y))
if action == "*":
    print(float(x) * float(y))
if action == "/":
    print(float(x) / float(y))
