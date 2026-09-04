import numpy as np

sales = np.array([800, 1200, 1500, 900, 2100, 1800, 700])

print("Sales:", sales)

high_sales = sales[sales > 1000]

print("Sales above 1000:", high_sales)

filtered_sales = sales[(sales >= 1000) & (sales <= 2000)]

print("Sales between 1000 and 2000:", filtered_sales)

extreme_sales = sales[(sales < 1000) | (sales > 2000)]

print("Sales below 1000 or above 2000:", extreme_sales)

count = np.count_nonzero(sales > 1000)

print("Number of sales above 1000:", count)

sales[sales < 1000] = 0

print("Updated sales:", sales)