# Q3: Pass and Fail Count
#Count passed/failed students and calculate pass percentage.

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

