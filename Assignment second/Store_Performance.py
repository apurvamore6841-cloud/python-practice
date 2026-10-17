'''A shop owner wants a quick summary of product sales. Each record contains a product name, price, and units sold.'''


products = [
    {'name': 'Notebook', 'price': 40, 'units': 25},
    {'name': 'Pen', 'price': 10, 'units': 60},
    {'name': 'Bottle', 'price': 150, 'units': 12},
    {'name': 'Bag', 'price': 500, 'units': 5}
]

total_revenue = 0
most_units_product = products[0]
highest_revenue_product = products[0]

for product in products:
    revenue = product['price'] * product['units']
    product['revenue'] = revenue

    print(product['name'], "Revenue:", revenue)

    total_revenue += revenue

    if product['units'] > most_units_product['units']:
        most_units_product = product

    if revenue > highest_revenue_product['revenue'] if 'revenue' in highest_revenue_product else revenue > highest_revenue_product['price'] * highest_revenue_product['units']:
        highest_revenue_product = product

print("Total revenue:", total_revenue)
print("Most units sold:", most_units_product['name'])
print("Highest revenue product:", highest_revenue_product['name'])

print("Observation 1: Pen has the highest units sold.")
print("Observation 2: Bag has the highest revenue.")
