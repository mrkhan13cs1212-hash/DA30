# A shop increases all product prices by 12% GST and then gives a 5% discount.
import numpy as np

products = np.array([500, 1200, 850, 2300])

gst_price = products * 1.12
final_price = gst_price * 0.95

print("Original Prices:")
print(products)

print("\nPrice After GST:")
print(gst_price)

print("\nFinal Price After Discount:")
print(final_price)