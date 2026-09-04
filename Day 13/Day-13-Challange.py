# Find:
#Total sales
#Average sales
#Maximum sales
#Minimum sales
#Sales greater than ₹1,500
#Sales less than ₹1,000
#Sales between ₹1,000 and ₹2,000
#Sales greater than ₹2,000
#Number of sales greater than ₹1,500
#Number of sales below ₹1,000

#Greater than ₹1,000 AND less than ₹2,000
#Less than ₹1,000 OR greater than ₹2,000


import numpy as np


sales = np.array([
    750, 1200, 1800, 950, 2200,
    1600, 900, 2500, 1350, 1100,
    700, 1950
])

print("Total Sales: ", np.sum(sales))
print("Average Sales: ", np.mean(sales))
print("Maximum Sales: ", np.max(sales))
print("Minimum Sales: ", np.min(sales))
print("Sales greater than 1,500: ", sales[sales > 1500])
print("Sales Less than 1,000: ", sales[sales < 1000])
print("Sales between 1,000 and 2,000: ", sales[(sales > 1000) & (sales < 2000)])
print("Sales greater than 2,000: ", sales[sales > 2000])
print("No.of Sales greater than 1,500: ", np.count_nonzero(sales > 1500))
print("No.of Sales below 1,000: ", np.count_nonzero(sales < 1000))
print("Sales less than 1,000 OR greater than 2,000: ", sales[(sales < 1000) | (sales > 2000)])
count = np.count_nonzero(sales >= 1500)

percentage = (count / len(sales)) * 100

print("Percentage of all transactions generated ₹1,500 or more: ", percentage)