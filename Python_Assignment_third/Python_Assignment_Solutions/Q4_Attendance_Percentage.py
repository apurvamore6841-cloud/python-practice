# Q4: Attendance Percentage
# Calculate attendance and check eligibility at 75%.

attendance = "PPAPPPAPPP"
present = 0

for day in attendance:
    if day == "P":
        present += 1

total_days = len(attendance)
percentage = (present / total_days) * 100

if percentage >= 75:
    result = "Eligible"
else:
    result = "Not eligible"

print("Present Days:", present)
print(f"Attendance: {percentage:.2f}%")
print(result)

