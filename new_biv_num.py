import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Load the dataset
df = pd.read_csv("smart_city_citizen_activity.csv")

# 2. Clean data by removing rows with missing values in our target columns
# Beginner tip: .dropna() ensures our calculations don't return 'NaN'
clean_data = df[['Steps_Walked', 'Calories_Burned']].dropna()

x = clean_data['Steps_Walked']
y = clean_data['Calories_Burned']

# 3. Descriptive Statistics (Simple method)
print("--- Summary Statistics ---")
print(clean_data.describe())

# 4. Correlation Analysis (Simplest method using Pandas)
correlation = x.corr(y)
print(f"\nPearson Correlation: {correlation:.4f}")

# 5. Trend Line Calculation (Using simple NumPy polyfit)
# This finds the slope (m) and intercept (c) for the line: y = mx + c
slope, intercept = np.polyfit(x, y, 1)

# 6. Visualization
plt.figure(figsize=(8, 6))

# Create the scatter plot
plt.scatter(x, y, color='forestgreen', alpha=0.5, label='Citizen Data')

# Create the Red Trend Line
# We calculate y-values for the start and end points of the line
line_x = np.array([x.min(), x.max()])
line_y = slope * line_x + intercept
plt.plot(line_x, line_y, color='red', linewidth=3, label='Trend Line')

# Labels and Titles
plt.title('Bivariate Analysis: Steps vs Calories', fontsize=14)
plt.xlabel('Steps Walked', fontsize=12)
plt.ylabel('Calories Burned', fontsize=12)
plt.legend()
plt.grid(True, alpha=0.3)

plt.show()