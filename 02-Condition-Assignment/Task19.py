# Calculate Class Attendance Percentage

# Input
total_classes = int(input("Enter total classes held: "))
attended_classes = int(input("Enter classes attended: "))

# Calculate percentage
attendance_percentage = (attended_classes / total_classes) * 100

# Display percentage
print("Attendance Percentage =", attendance_percentage, "%")

# Check eligibility
if attendance_percentage >= 75:
    print("Eligible to sit in the exam.")

else:
    print("Not eligible to sit in the exam.")