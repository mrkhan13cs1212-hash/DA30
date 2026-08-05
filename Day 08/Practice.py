import numpy as np

a = np.array([10, 20, 30, 40])
b = np.array([2, 4, 5, 8])

print("Array A:", a)
print("Array B:", b)

print("\nAddition:")
print(a + b)

print("\nSubtraction:")
print(a - b)

print("\nMultiplication:")
print(a * b)

print("\nDivision:")
print(a / b)

prices = np.array([100, 250, 300, 450])

print("Original Prices:")
print(prices)

print("\nAfter Adding GST ₹18:")
print(prices + prices * 0.18)

print("\n10% Discount:")
print(prices * 0.90)

marks = np.array([45, 78, 32, 90, 67])

print("\nMarks:")
print(marks)

print("\nGreater than 50:")
print(marks > 50)

print("\nEqual to 90:")
print(marks == 90)

print("\nLess than or Equal to 45:")
print(marks <= 45)

print("\nBroadcasting Example:")
import numpy as np

sales = np.array([1200, 1500, 1800, 2000])

bonus = np.array([100])

print("\nOriginal Sales:")
print(sales)
print("\nBonus:")
print(bonus)

print("\nAfter Bonus:")
print(sales + bonus)