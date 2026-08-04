import numpy as np

marks = np.array([55, 89, 34, 67, 91, 45, 76, 29])

print("Marks:", marks)

print("Highest:", np.max(marks))
print("Lowest:", np.min(marks))
print("Average:", np.mean(marks))

print("Passed Students:")
print(marks[marks >= 35])

print("Failed Students:")
print(marks[marks < 35])

print("Distinction Students:")
print(marks[marks >= 75])

print("Number of Passed Students:")
print(np.count_nonzero(marks >= 35))