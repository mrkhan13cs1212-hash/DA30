import numpy as np

sales = np.array([1200, 900, 1800, 1500, 2200, 800, 1700])

print("Sales:", sales)
print("First Sale:", sales[0])
print("Last Sale:", sales[-1])
print("1-4 Sales:", sales[0:4])
print("Alternate Sales:", sales[::2])
print("Reverse Sales:", sales[::-1])
print("Sales greater than 1500:", sales[sales > 1500])
print("Number of Sales greater than 1500:", np.count_nonzero(sales > 1500))
print("Highest Sale:", np.max(sales))
print("Lowest Sale:", np.min(sales))
print("Average Sale:", np.mean(sales))
print("Total Sales:", np.sum(sales))
print("Replacing Sales less than 1000 with 1000")
sales[sales < 1000] = 1000
print("Updated Sales:", sales)
print("Top 3 Highest Sales:", np.sort(sales)[-3:])