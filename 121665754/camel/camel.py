def snake(camel):
    snake = ""
    for i in camel:
        if i.isupper():
           snake += "_" + i.lower()
        else:
            snake += i
    return snake



camel = input("camelCase: ")
print(f"snake_case {snake(camel)}")
