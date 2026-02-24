# -*- coding: utf-8 -*-
"""
@author: Dell
"""
#Task 1
#loading libraries & creating datasets
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
np.random.seed(42)
# Normal distribution → Human Heights (cm)
heights = pd.Series(np.random.normal(loc=170, scale=10, size=1000))
# Right-skewed distribution → Household Incomes
incomes = pd.Series(np.random.lognormal(mean=10, sigma=0.8, size=1000))
# Left-skewed distribution → Easy Exam Scores
scores = pd.Series(100 - np.random.lognormal(mean=2, sigma=0.5, size=1000))
#Function to Plot Histogram + KDE & Compare Mean/Median
def analyze_distribution(data, title):
    mean = data.mean()
    median = data.median()

    plt.figure(figsize=(6,4))
    sns.histplot(data, kde=True)
    plt.axvline(mean, color='red', linestyle='--', label=f"Mean = {mean:.2f}")
    plt.axvline(median, color='green', linestyle='-', label=f"Median = {median:.2f}")
    plt.title(title)
    plt.legend()
    plt.show()

    print(f"{title}")
    print(f"Mean   : {mean:.2f}")
    print(f"Median : {median:.2f}")
    print("-" * 40)
#Analyze Each Dataset
#Human Heights (Normal Distribution)
analyze_distribution(heights, "Human Heights (Normal Distribution)")
#Household Incomes (Right-Skewed)
analyze_distribution(incomes, "Household Incomes (Right-Skewed)")
#Easy Exam Scores (Left-Skewed)
analyze_distribution(scores, "Easy Exam Scores (Left-Skewed)")

#Task 2
#loading libraries & creating datasets
import pandas as pd
import numpy as np
# Sample dataset (e.g., student scores)
data = {
    "student": ["A","B","C","D","E","F","G","H"],
    "score": [65, 70, 72, 68, 75, 73, 150, 69]  # 150 is extreme
}
df = pd.DataFrame(data)
print(df)
#Calculating  Mean (μ) and Standard Deviation (σ)
mean = df["score"].mean()
std = df["score"].std()
print("Mean (μ):", mean)
print("Standard Deviation (σ):", std)
#Creating the Z-Score Column
df["z_score"] = (df["score"] - mean) / std
print(df)
#Identify Statistical Outliers
outliers = df[df["z_score"].abs() > 3]
print("Outliers:")
print(outliers)


#Task 3
#load libraries
import numpy as np
import matplotlib.pyplot as plt
#Create a Heavily Skewed Dataset
np.random.seed(42)
# Skewed population (e.g., incomes)
population = np.random.lognormal(mean=10, sigma=1.0, size=100_000)
#Repeated Sampling (The Key Experiment)
sample_means = []
for _ in range(1000):
    sample = np.random.choice(population, size=30, replace=False)
    sample_means.append(sample.mean())
#Plot Histogram of Sample Means
plt.figure(figsize=(7,4))
plt.hist(sample_means, bins=30)
plt.title("Distribution of Sample Means (n = 30, samples = 1000)")
plt.xlabel("Sample Mean")
plt.ylabel("Frequency")
plt.show()

