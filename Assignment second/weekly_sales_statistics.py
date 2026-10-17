'''Review the sales values for a week.'''



sales = [1200, 1500, 980, 1750, 1600, 2100, 1900]

total = sum(sales)
average = total / len(sales)
highest = max(sales)
lowest = min(sales)

count = 0

for sale in sales:
    if sale >= 1500:
        count += 1

print("Total sales:", total)
print("Average sales:", average)
print("Highest sales:", highest)
print("Lowest sales:", lowest)
print("Days with sales >= 1500:", count)
