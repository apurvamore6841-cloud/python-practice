# Q2: Class Average
# Purpose: Calculate class average, find the topper, and list below-average students.

marks = {"Riya": 78, "Omkar": 64, "Sneha": 91, "Aditya": 55, "Isha": 67}

average = sum(marks.values()) / len(marks)
topper = max(marks, key=marks.get)

print(f"Class Average: {average:.2f}")
print(f"Topper: {topper} - {marks[topper]}")

for name, mark in marks.items():
    if mark < average:
        print(f"Below average: {name} - {mark}")

# Explanation:
# Dictionary stores each student's name and marks.
# values() gets marks, sum() adds them, and len() counts students.
# max(..., key=marks.get) finds the student with the highest marks.
# items() provides each name-mark pair for the loop.
