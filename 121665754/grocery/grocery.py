item_counts = {}

while True:
    try:
        item = input().strip().upper()
        if item:
            if item in item_counts:
                item_counts[item] += 1
            else:
                item_counts[item] = 1
    except EOFError:
        for item, count in sorted(item_counts.items()):
            print(f"{count} {item}")
        break
