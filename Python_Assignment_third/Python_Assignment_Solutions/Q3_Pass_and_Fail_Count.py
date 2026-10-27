# Q3: Pass and Fail Count
# Purpose: Count passed/failed students and calculate pass percentage.

marks = [78, 35, 64, 91, 28, 55, 40, 67, 39, 82]
passed = 0
failed = 0

for mark in marks:
    if mark >= 40:
        passed += 1
    else:
        failed += 1

percentage = (passed / len(marks)) * 100

print("Passed:", passed)
print("Failed:", failed)
print(f"Pass Percentage: {percentage:.2f}%")

# Explanation:
# The list contains the students' marks.
# Counters start at zero and increase for each pass or fail.
# A mark of 40 or more is considered a pass.
# Pass percentage = passed students / total students * 100.
