# Identification of missing values using isnull()
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("smart_city_citizen_activity.csv")

# Check for missing values per column
missing_values = df.isnull().sum()
print("Missing values per column:\n", missing_values)

# Visualize missing values using a Heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(df.isnull(), cbar=False, cmap="viridis")
plt.title("Heatmap of Missing Values")
plt.show()