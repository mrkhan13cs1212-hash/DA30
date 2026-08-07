#A teacher wants to generate marks for 50 students.
#Requirements
#1. Generate random marks between 35 and 100.
#2. Display all marks.
#3. Find:
#   - Average mark
#   - Highest mark
#   - Lowest mark
#4. Count how many students scored:
#   - Above 90
#   - Between 75 and 90
#   - Below 50
#5. Display the marks in sorted order.

import numpy as np

np.random.seed(10)
marks = np.random.randint(35, 101, 50)
print("Student Marks:")
print(marks)
print("\nAverage:", np.mean(marks))
print("Highest:", np.max(marks))
print("Lowest:", np.min(marks))
print("\nNumber of students scoring above 90:", np.sum(marks > 90))
print("Number of students scoring between 75 and 90:", np.sum((marks >= 75) & (marks <= 90)))
print("Number of students scoring below 50:", np.sum(marks < 50))
print("\nMarks in sorted order:")
print(np.sort(marks))