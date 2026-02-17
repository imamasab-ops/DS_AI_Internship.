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
plt.scatter(x, y, color='blue', s=100, alpha=0.7)

plt.xlabel("Variable X")
plt.ylabel("Variable Y")
plt.title("Customized Scatter Plot")
plt.grid(True)

plt.show()
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Create DataFrame
data = pd.DataFrame({
    "Variable X": x,
    "Variable Y": y
})

sns.scatterplot(data=data, x="Variable X", y="Variable Y")

plt.title("Scatter Plot Using Seaborn")
plt.show()

#task1
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("housing_data.csv")
data = {
    "SquareFootage": [1500, 2000, 1800, 2200, 1400, 2500, 1700, 2100],
    "Price": [250000, 320000, 290000, 360000, 230000, 400000, 275000, 340000],
    "Neighborhood": ["A", "B", "A", "B", "C", "B", "C", "A"]
}

df = pd.DataFrame(data)
plt.figure(figsize=(8,6))
sns.scatterplot(data=df, x="SquareFootage", y="Price")

plt.title("Scatter Plot: Square Footage vs Price")
plt.xlabel("Square Footage")
plt.ylabel("Price")
plt.show()


plt.figure(figsize=(8,6))
sns.boxplot(data=df, x="Neighborhood", y="Price")

#
plt.title("Boxplot: Neighborhood vs Price")
plt.xlabel("Neighborhood")
plt.ylabel("Price")
plt.show()
sns.lmplot(data=df, x="SquareFootage", y="Price")
plt.title("Square Footage vs Price with Trend Line")
plt.show()

