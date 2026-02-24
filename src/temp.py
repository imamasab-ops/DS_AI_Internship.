# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import matplotlib.pyplot as plt

# Sample data
size = [500, 800, 1000, 1200, 1500, 1800, 2000]
price = [150000, 220000, 260000, 300000, 360000, 420000, 480000]

plt.scatter(size, price)
plt.xlabel("Size (sq ft)")
plt.ylabel("Price ($)")
plt.title("Scatter Plot: Size vs Price")
plt.show()

#Task1
import matplotlib.pyplot as plt

# Example numerical variables
x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11]
y = [99, 86, 87, 88, 100, 86, 103, 87, 94, 78]

# Create scatter plot
plt.scatter(x, y)

# Add labels and title
plt.xlabel("Variable X")
plt.ylabel("Variable Y")
plt.title("Scatter Plot of Two Numerical Variables")

# Show plot
plt.show()
