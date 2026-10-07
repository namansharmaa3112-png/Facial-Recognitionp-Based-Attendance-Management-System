import pandas as pd

# Load attendance data
attendance = pd.read_csv("data/attendance.csv")

# Total days attendance taken
total_days = attendance["Date"].nunique()

print("Total Attendance Days:", total_days)
print("\n--- Attendance Summary ---")

# Count attendance per student
summary = attendance["Student"].value_counts()

# Calculate percentage
percentage = (summary / total_days) * 100

result = pd.DataFrame({
    "Days Present": summary,
    "Attendance %": percentage.round(2)
})

print(result)

# Save analysis result
result.to_csv("data/attendance_summary.csv")

print("\nAttendance analysis saved as attendance_summary.csv")
