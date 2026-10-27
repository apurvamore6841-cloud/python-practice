# Q10: Result Card
# Purpose: Print subject-wise results, total, percentage, and final result.

name = input("Enter student name: ")
marks = {"Maths": 78, "Science": 35, "English": 70, "Computer": 88}

total = 0
all_pass = True

print("Result Card:", name)
for subject, mark in marks.items():
    result = "Pass" if mark >= 40 else "Fail"
    print(f"{subject}: {mark} - {result}")
    total += mark
    if mark < 40:
        all_pass = False

percentage = total / len(marks)
final_result = "PASS" if all_pass else "FAIL"

print("Total:", total)
print(f"Percentage: {percentage:.2f}%")
print("Final Result:", final_result)

# Explanation:
# The loop checks each subject and prints Pass/Fail.
# total += mark adds each subject's marks to the total.
# all_pass becomes False if any subject has less than 40.
# There are four subjects, each out of 100, so total/4 gives percentage.
# The final result is PASS only if every subject is passed.
