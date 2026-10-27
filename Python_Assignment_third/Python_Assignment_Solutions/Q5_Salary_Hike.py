# Q5: Salary Hike
# Calculate revised salaries and total payroll before/after a hike.

salaries = {"Aman": 35000, "Pooja": 72000, "Rahul": 38000, "Neha": 66000}
before = sum(salaries.values())

new_salaries = {
    name: salary * 1.10 if salary < 40000 else salary * 1.05
    for name, salary in salaries.items()
}

after = sum(new_salaries.values())

print("New Salaries:", new_salaries)
print("Payroll Before:", before)
print("Payroll After:", after)

