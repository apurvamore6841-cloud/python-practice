products = {
    "Mouse": [499, 10],
    "Keyboard": [1299, 5],
    "Monitor": [8999, 3],
    "Cable": [199, 40]
}

grand_total = 0

for name, details in products.items():
    price = details[0]
    quantity = details[1]

    stock_value = price * quantity
    print(f"{name}: stock value = {stock_value}")

    grand_total = grand_total + stock_value

print("Grand total:", grand_total)
print("Products:", len(products))
print("Names:", sorted(products.keys()))