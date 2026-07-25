# Student Grade Calculation Program

# Input marks for 5 subjects
marks1 = float(input("Enter marks for Subject 1: "))
marks2 = float(input("Enter marks for Subject 2: "))
marks3 = float(input("Enter marks for Subject 3: "))
marks4 = float(input("Enter marks for Subject 4: "))
marks5 = float(input("Enter marks for Subject 5: "))

# Calculate total and percentage
total = marks1 + marks2 + marks3 + marks4 + marks5
percentage = total / 5

# Determine grade
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

# Display results
print("\n----- Student Result -----")
print("Total Marks:", total)
print("Percentage:", percentage, "%")
print("Grade:", grade)
