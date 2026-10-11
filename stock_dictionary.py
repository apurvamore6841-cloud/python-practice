inventory = {"pen": 50, "book": 20, "bag": 10}

inventory["pencil"] = 100
inventory["book"] = 35
inventory.pop("bag")

print(inventory)
print("Total stock:", sum(inventory.values()))