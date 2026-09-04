import numpy as np

# Student marks
marks = np.array([
    45, 78, 92, 56, 67,
    34, 88, 73, 95, 41,
    62, 85, 29, 76, 90
])

# Basic Statistics
print("===== BASIC STATISTICS =====")
print("1. Total marks:", np.sum(marks))
print("2. Average marks:", round(np.mean(marks), 2))
print("3. Highest marks:", np.max(marks))
print("4. Lowest marks:", np.min(marks))

# Pass and Fail Analysis
passed_students = marks[marks >= 40]
failed_students = marks[marks < 40]

print("\n===== PASS / FAIL ANALYSIS =====")
print("5. All students who passed:", passed_students)
print("6. All students who failed:", failed_students)
print("7. No. of Students Passed:", np.count_nonzero(marks >= 40))
print("8. No. of Students Failed:", np.count_nonzero(marks < 40))

# Marks Categorization
print("\n===== MARKS CATEGORY =====")
print("Excellent:", marks[marks >= 90])
print("Very Good:", marks[(marks >= 75) & (marks < 90)])
print("Good:", marks[(marks >= 60) & (marks < 75)])
print("Average:", marks[(marks >= 40) & (marks < 60)])
print("Failed:", marks[marks < 40])

# Conditional Analysis
print("\n===== CONDITIONAL ANALYSIS =====")
print(
    "Students who scored between 60 and 80:",
    marks[(marks >= 60) & (marks <= 80)]
)

print(
    "Students who scored below 40 OR above 90:",
    marks[(marks < 40) | (marks > 90)]
)

# Percentage Analysis
passed = np.count_nonzero(marks >= 40)
pass_percentage = (passed / len(marks)) * 100

above_75 = np.count_nonzero(marks >= 75)
above_75_percentage = (above_75 / len(marks)) * 100

print("\n===== PERCENTAGE ANALYSIS =====")
print(
    "Percentage of students passed the examination:",
    round(pass_percentage, 2), "%"
)

print(
    "Percentage of students scored 75 or above:",
    round(above_75_percentage, 2), "%"
)

# Top 5 Marks
sorted_marks = np.sort(marks)

print("\n===== TOP 5 MARKS =====")
print("Top 5 marks:", sorted_marks[-5:])