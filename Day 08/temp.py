import numpy as np

morning = np.array([24, 25, 26, 24, 23])
evening = np.array([32, 34, 35, 31, 30])

difference = evening - morning

print("Morning Temperature:")
print(morning)

print("\nEvening Temperature:")
print(evening)

print("\nTemperature Increase:")
print(difference)