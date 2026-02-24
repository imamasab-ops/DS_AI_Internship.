# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#task 1
import pandas as pd

# Create sample dataset
df = pd.DataFrame({
    "Transmission": ["Automatic", "Manual", "Automatic", "Manual"],
    "Color": ["Red", "Blue", "Green", "Red"]
})

print(df)
#lable encoding 
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
df["Transmission"] = le.fit_transform(df["Transmission"])

print(df)

#one hot encoding 
df = pd.get_dummies(df, columns=["Color"], drop_first=True)

print(df)


#Task 2
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler

# Sample numeric data
data = pd.DataFrame({
    "Age": [25, 30, 35, 40, 45],
    "Salary": [30000, 50000, 70000, 90000, 110000]
})

print("Original Data:\n")
print(data)

# Initialize StandardScaler
scaler = StandardScaler()

# Fit and transform the data
standardized_data = scaler.fit_transform(data)

# Convert back to DataFrame
standardized_df = pd.DataFrame(standardized_data, columns=data.columns)

print("\nStandardized Data (Mean = 0, Std = 1):\n")
print(standardized_df)

# Initialize MinMaxScaler
scaler = MinMaxScaler()

# Fit and transform the data
normalized_data = scaler.fit_transform(data)

# Convert back to DataFrame
normalized_df = pd.DataFrame(normalized_data, columns=data.columns)

print("\nNormalized Data (0 to 1 range):\n")
print(normalized_df)


# ---------------- AFTER Scaling ----------------
plt.figure()
plt.hist(standardized_df["Salary"])
plt.xlabel("Standardized Salary (Mean = 0, Std = 1)")
plt.ylabel("Frequency")
plt.title("Histogram After Standardization")
plt.show()



 #Task 3 
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
# Create synthetic dataset
np.random.seed(42)
X = np.linspace(-10, 10, 100).reshape(-1, 1)
y = 3 * X.flatten() + 5 + np.random.normal(0, 5, 100)  # Linear relationship
# Split into train and test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
# Train Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)
# Predict
y_pred = model.predict(X_test)
# Evaluate
r2 = r2_score(y_test, y_pred)
print("R² Score (Linear Regression - No Curve):", round(r2, 4))
# Create sample feature
X = np.array([[1],
              [2],
              [3],
              [4],
              [5]])
print("Original Feature:\n", X) # Create polynomial features (degree=2)
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)
print("\nPolynomial Features (degree=2):\n", X_poly)
model = LinearRegression()
model.fit(X_poly, [2, 4, 9, 16, 25])  # Example target
print("Model trained on polynomial features.")










