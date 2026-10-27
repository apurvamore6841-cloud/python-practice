# Q2: Class Average
# Calculate class average, find the topper, and list below-average students.

marks = {"sonali": 64, "Apurva": 91, "riddhi": 55, "sangivani": 67}

average = sum(marks.values()) / len(marks)
topper = max(marks, key=marks.get)

print(f"Class Average: {average:.2f}")
print(f"Topper: {topper} - {marks[topper]}")

for name, mark in marks.items():
    if mark < average:
        print(f"Below average: {name} - {mark}")

