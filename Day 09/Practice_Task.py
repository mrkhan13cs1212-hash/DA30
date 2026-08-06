import numpy as np

a = np.array([5,10,15])
b = np.array([20,25,30])

print("Concatenated Array:")
print(np.concatenate((a, b)))

print("Horizontal Stacking:")
print(np.hstack((a,b)))

print("Vertical Stacking:")
print(np.vstack((a,b)))

arr = np.arange(1,13)
print("Original Array:")
print(arr)
print("Reshaped Array (3x4):")
print(arr.reshape(3,4))
print("Reshaped Array (4x3):")
print(arr.reshape(4,3))
print("Reshaped Array (2x6):")
print(arr.reshape(2,6))


matrix = np.array([[11,22],
 [33,44],
 [55,66],
 [77,88]])

print("Original Matrix:")
print(matrix)
print("Flattened Matrix:")
print(matrix.flatten())
print("Split Matrix into 2 parts:")
print(np.split(matrix, 2, axis=0))

arr2 = np.array([100, 200, 300, 400, 500, 600])
print("Original Array:")
print(arr2)
print("Splitting Array into 3 parts:")
print(np.split(arr2, 3))