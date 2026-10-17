cart = ["pen", "book"]

cart.append("bag")
cart.insert(0, "ruler")
cart.extend(["eraser", "pencil"])
cart.remove("book")

print(cart)

cart.sort()
print(cart, len(cart))

cart.reverse()
print(cart)