# Q5: Salary Hike
# Purpose: Calculate revised salaries and total payroll before/after a hike.

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

# Explanation:
# Employees earning less than 40000 get a 10% hike.
# Others get a 5% hike.
# The dictionary comprehension creates a new salary dictionary.
# sum() calculates the total payroll before and after the hike.
