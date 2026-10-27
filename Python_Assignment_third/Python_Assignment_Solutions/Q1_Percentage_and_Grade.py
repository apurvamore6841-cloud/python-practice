# Q1: Percentage and Grade
# Calculate a student's total, percentage, and grade.

m1 = float(input("Enter Maths marks: "))
m2 = float(input("Enter Science marks: "))
m3 = float(input("Enter English marks: "))

total = m1 + m2 + m3
percentage = (total / 300) * 100

if percentage >= 75:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 40:
    grade = "C"
else:
    grade = "Fail"

print("Total:", total)
print(f"Percentage: {percentage:.2f}%")
print("Grade:", grade)


