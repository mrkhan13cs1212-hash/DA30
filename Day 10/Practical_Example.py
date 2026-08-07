import numpy as np

np.random.seed(10)

marks = np.random.randint(35,101,20)

print("Student Marks:")
print(marks)

print("\nAverage:", np.mean(marks))
print("Highest:", np.max(marks))
print("Lowest:", np.min(marks))