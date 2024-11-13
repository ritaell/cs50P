fruits = {
            "apple":130,
            "avocado":50,
            "banana":110,
            "sweet cherries":100,
            "kiwifruit":90,
            "pear":100
                }
def carolies(item):
    if item in fruits:
        return fruits[item]
    else:
        return ""




item=input("Item: ").lower()
print(carolies(item))
