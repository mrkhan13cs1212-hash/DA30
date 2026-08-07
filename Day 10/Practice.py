import numpy as np

print(np.random.rand())

print(np.random.rand(5))

print(np.random.rand(3,4))

print("\n")
print(np.random.randint(1,11))

print("\n")
print(np.random.randint(1,11,5))

print("\n")
print(np.random.randint(1,101,(3,4)))

print("\nColors")
colors = ["Red","Blue","Green","Black"]

print(np.random.choice(colors))

print(np.random.choice(colors,3))

print("\nShuffling")
arr = np.array([1,2,3,4,5,6])

np.random.shuffle(arr)

print(arr)
print("\nSeed")
np.random.seed(42)

print(np.random.randint(1,100,5))

print("Distribution")
data = np.random.randn(5)

print(data)