cost=float(input("Enter Cost Price"))
selling=float(input("Enter selling Price"))
profit=selling-cost
profit_percentage=(profit/cost)*100
print(f"profit:{profit:2f}")
print(f"profit_percentage:{profit_percentage:.2f}")