#Generate a 5 × 5 matrix of random integers from 1 to 100.
#Find the:
#Maximum
#Minimum
#Mean
#Count how many numbers are greater than 50.
#Sort all values into ascending order.
#Reshape the sorted values into a 5 × 5 matrix.

import numpy as np
import random

# Generate a 5 × 5 matrix of random integers from 1 to 100
matrix = np.random.randint(1, 101, (5, 5))

print("Original Matrix:")
print(matrix)

# Find the maximum, minimum, and mean
maximum = np.max(matrix)
minimum = np.min(matrix)
mean = np.mean(matrix)

print(f"\nMaximum: {maximum}")
print(f"\nMinimum: {minimum}")
print(f"\nMean: {mean}")

# Count how many numbers are greater than 50
count_greater_than_50 = np.sum(matrix > 50)
print(f"\nCount of numbers greater than 50: {count_greater_than_50}")

# Sort all values into ascending order
sorted_values = np.sort(matrix.flatten())

# Reshape the sorted values into a 5 × 5 matrix
reshaped_matrix = sorted_values.reshape(5, 5)

print("\nSorted Matrix:")
print(reshaped_matrix)