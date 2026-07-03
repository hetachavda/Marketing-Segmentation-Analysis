import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Python Code for Market Segmentation Project

import pandas as pd
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

# 1. Initial Dataset Exploration
# Load the uploaded Excel file to review its structure
file_path = '/mnt/data/Group Presentation_market_segmentation_data-3.xlsx'
excel_data = pd.ExcelFile(file_path)

# Display sheet names to understand the structure of the file
print(excel_data.sheet_names)

# Load the data from the sheet to inspect its structure
sheet_data = excel_data.parse('Sheet1')

# Display the first few rows of the dataset to understand its structure
print(sheet_data.head())

# 2. Segmentation Logic Implementation
# Sample Data
data = {
    "Customer ID": [1, 2, 3, 4],
    "Age": [25, 65, 40, 70],
    "Often Engaged (%)": [60, 65, 35, 20]
}

df = pd.DataFrame(data)

# Define a function for segmentation
def assign_segment(row):
    if 18 <= row["Age"] <= 30 and row["Often Engaged (%)"] >= 50:
        return "Young Professionals"
    elif row["Age"] >= 60 and row["Often Engaged (%)"] >= 50:
        return "Wealthy Seniors"
    elif 31 <= row["Age"] <= 59 and 30 <= row["Often Engaged (%)"] <= 50:
        return "Moderately Engaged Prof."
    elif row["Age"] >= 60 and row["Often Engaged (%)"] < 30:
        return "Low-Income Retirees"
    else:
        return "Other"

# Apply the segmentation logic
df["Segment Assignment"] = df.apply(assign_segment, axis=1)

# Display the result
print(df)

# 3. Summary Statistics Calculation
# Assuming the original DataFrame 'sheet_data' contains numeric columns
# Calculate summary statistics for key columns
summary_stats = sheet_data.describe()

# Display the summary statistics
print(summary_stats)

# 4. Clustering with K-Means
# Selecting the relevant columns for clustering
columns = ["Age", "Income"]  # Example numerical columns
data_for_clustering = sheet_data[columns].dropna()

# Applying K-Means Clustering
kmeans = KMeans(n_clusters=4, random_state=42)
clusters = kmeans.fit_predict(data_for_clustering)

# Adding the cluster labels to the original dataset
sheet_data["Cluster"] = clusters

# Display the dataset with cluster assignments
print(sheet_data.head())

# 5. Data Visualization (Scatter Plot)
# Scatter plot of Age vs. Income colored by cluster
plt.figure(figsize=(10, 6))
for cluster in range(4):
    clustered_data = data_for_clustering[sheet_data["Cluster"] == cluster]
    plt.scatter(clustered_data["Age"], clustered_data["Income"], label=f"Cluster {cluster}")

plt.title("Age vs. Income by Cluster")
plt.xlabel("Age")
plt.ylabel("Income")
plt.legend()
plt.show()

