import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the dataset
df = pd.read_csv("smart_city_citizen_activity.csv")

# 2. Select columns and remove missing values
# We focus on Gender and Mode_of_Transport
data = df[['Gender', 'Mode_of_Transport']].dropna()

# 3. Create a Frequency Table (Crosstab)
# This shows the count of each transport mode for every gender
count_table = pd.crosstab(data['Gender'], data['Mode_of_Transport'])

print("--- Gender vs Mode of Transport (Frequency Table) ---")
print(count_table)

# 4. Generate a Stacked Bar Chart
# Beginner Tip: 'stacked=True' makes it easy to compare parts of a whole
count_table.plot(kind='bar', stacked=True, figsize=(10, 6), color=['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6'])

# 5. Adding Professional Labels
plt.title('Relationship: Gender vs Mode of Transport', fontsize=14)
plt.xlabel('Gender Group', fontsize=12)
plt.ylabel('Number of Citizens', fontsize=12)
plt.xticks(rotation=0)  # Keeps gender names horizontal for better readability
plt.legend(title='Transport Mode', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(axis='y', linestyle='--', alpha=0.3)

plt.tight_layout()
plt.show()