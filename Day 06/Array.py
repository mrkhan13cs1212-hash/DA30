import numpy as np

marks = np.array([45, 67, 89, 34, 56, 78, 91])

print(marks)
print("Index of Array")
print("First element:", marks[0])
print("Third element:", marks[2])
print("Last element:", marks[-1])
print("Slicing of Array")
print(marks[1:5])
print(marks[:4])
print(marks[3:])
print(marks[-3:])
print("Step Slicing of Array")
print(marks[::2])
print(marks[::-1])
print("Boolean Filtering of Array")
print("Passed Students:")
print(marks[marks >= 35])
print("Failed Students:")
print(marks[marks < 35])
print("Students scoring above 75:")
print(marks[marks > 75])
print("Count of Students")
print("Number of Passed Students:")
print(np.count_nonzero(marks >= 35))
print("Number of Distinction Students:")
print(np.count_nonzero(marks >= 75))
print("Replacing Values in Array")
marks[marks < 35] = 35
print(marks)
print("2D Array")
students = np.array([
    [101, 78],
    [102, 65],
    [103, 91],
    [104, 55]
])

print(students)
print("Access Data")
print(students[0])
print(students[2][1])
print(students[:,0])
print(students[:,1])
print("Students scoring above 70:")
print(students[students[:,1] > 70])