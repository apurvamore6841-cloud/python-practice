# Q7: Employees per Department
# Count employees in each department and group their names.

staff = [
    ("Aman", "Sales"), ("Purva", "IT"), ("Radha", "HR"),
    ("samruddhi", "IT"), ("Kishori", "Sales"), ("sonu", "IT")
]

counts = {}
department_names = {}

for name, department in staff:
    counts[department] = counts.get(department, 0) + 1
    department_names.setdefault(department, []).append(name)

print("Employee Counts:", counts)
print("Department Names:", department_names)

