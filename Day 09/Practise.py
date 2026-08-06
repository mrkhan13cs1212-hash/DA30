import numpy as np

a = np.array([10, 20, 30])
b = np.array([40, 50, 60])

result = np.concatenate((a, b))

print(result)

print("Horizontal Stacking:")
print(np.hstack((a,b)))

print("Vertical Stacking:")
print(np.vstack((a,b)))

print("Column Stacking:")
print(np.column_stack((a,b)))

print("Splitting Array:")
split_array = np.split(result, 3)
print(split_array)

print("Reshaping Array:")
arr = np.arange(1,13)

matrix = arr.reshape(3,4)
print(arr)
print(matrix)

print("Flattening Array:")
print(matrix.flatten())

print("Reshaping into One Row:")
print(matrix.reshape(1,12))

print("Reshaping into One Column:")
print(matrix.reshape(12,1))