table = [["Jan", 1200], ["Feb", 1500], ["Mar", 900]]

print(table[1][1])

table.append(["Apr", 1700])

total = 0

for row in table:
    print(f"Month: {row[0]}, Sales: {row[1]}")
    total = total + row[1]

print("Total:", total)