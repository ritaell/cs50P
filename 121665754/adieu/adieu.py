import inflect


names=[]
while True:
    try:
        name=input("Name: ")
        if name!="":
            names.append(name)
        else:
            break
    except EOFError:
        break

p=inflect.engine()
print(f"Adieu, adieu, to {p.join(names)}")


