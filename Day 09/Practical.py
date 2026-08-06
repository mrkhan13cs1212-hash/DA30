import numpy as np

sales_q1 = np.array([1200,1500,1800])
sales_q2 = np.array([1700,1600,2100])

year_sales = np.concatenate((sales_q1,sales_q2))

print("Year Sales:")
print(year_sales)

print("\nReshaped:")
print(year_sales.reshape(2,3))