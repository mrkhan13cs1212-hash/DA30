"""
A company records sales for 12 months:

[1200,1400,1500,1600,
 1700,1800,1900,2000,
 2100,2200,2300,2400]

Perform the following:

Create the array.
Reshape it into 4 quarters × 3 months.
Display each quarter.
Flatten it back to 1D.
Split it into 2 half-year arrays
"""

import numpy as np

sales = np.array([1200,1400,1500,1600,
                  1700,1800,1900,2000,
                  2100,2200,2300,2400])

print("Original Sales Array:")
print(sales)
print("\nReshaped into 4 Quarters x 3 Months:")
quarters = sales.reshape(4,3)
print(quarters)

print("\nDisplaying Each Quarter:")
for i, quarter in enumerate(quarters):
    print(f"Quarter {i+1}: {quarter}")

print("\nFlattened Array:")
flattened = quarters.flatten()
print(flattened)

print("\nSplitting into 2 Half-Year Arrays:")
half_year1, half_year2 = np.split(flattened, 2)
print(f"Half-Year 1: {half_year1}")
print(f"Half-Year 2: {half_year2}")