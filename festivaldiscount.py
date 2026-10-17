
# Name: Your Name
prices = [499, 1299, 250, 3999, 150]
total_saving = 0

for price in prices:
    discount = price * 10 / 100
    discounted_price = price - discount

    print(f"Original: {price} | Discounted: {discounted_price:.2f}")
    total_saving = total_saving + discount

print(f"Total saving: {total_saving:.2f}")