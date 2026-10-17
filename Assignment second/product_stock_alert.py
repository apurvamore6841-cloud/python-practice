'''A shop needs to reorder products with fewer than 10 units in stock.'''


stock = {
    'Notebook': 18,
    'Pen': 7,
    'Marker': 4,
    'Folder': 12,
    'Eraser': 9
}

count = 0

for product, quantity in stock.items():
    print(product, ":", quantity)

    if quantity < 10:
        print("Reorder:", product)
        count += 1

print("Products needing reorder:", count)
