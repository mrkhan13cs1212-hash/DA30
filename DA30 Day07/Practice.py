import numpy as np

marks = np.array([45, 78, 32, 90, 67, 25, 88])

print("Original Marks:", marks)

print("Passed Students:")
print(marks[marks >= 35])

print("Failed Students:")
print(marks[marks < 35])

marks[marks < 35] = 35

print("Updated Marks:")
print(marks)

sales = np.array([1200, 900, 1800, 1500, 2200, 800, 1700])

print("Sales Greater Than 1500:")
print(sales[sales > 1500])

print("Sales Less Than 1000:")
print(sales[sales < 1000])

ages = np.array([15, 18, 22, 30, 40, 65, 70])

adults = ages[(ages >= 18) & (ages <= 60)]

print("Adults:")
print(adults)

temperatures = np.array([28, 32, 35, 40, 25, 0, 30, 38])

print("Hot Days (>35°C):")
print(temperatures[temperatures > 35])

print("Pleasant Days (25°C - 35°C):")
print(temperatures[(temperatures >= 25) & (temperatures <= 35)])

print("Number of Hot Days:")
print(np.count_nonzero(temperatures > 35))

print("Number of Cold Days:")
print(np.count_nonzero(temperatures <= 25))