# Q7: Employees per Department
# Purpose: Count employees in each department and group their names.

staff = [
    ("Aman", "Sales"), ("Pooja", "IT"), ("Rahul", "HR"),
    ("Neha", "IT"), ("Karan", "Sales"), ("Isha", "IT")
]

counts = {}
department_names = {}

for name, department in staff:
    counts[department] = counts.get(department, 0) + 1
    department_names.setdefault(department, []).append(name)

print("Employee Counts:", counts)
print("Department Names:", department_names)

# Explanation:
# Each tuple contains an employee name and department.
# get(department, 0) retrieves the current count, or 0 if new.
# setdefault(department, []) creates a list for a new department.
# append(name) adds the employee to that department's list.
