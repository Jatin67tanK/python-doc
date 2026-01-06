import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the pre-cleaned dataset
df = pd.read_csv("smart_city_citizen_activity.csv")

# 2. Select relevant columns
# We analyze Carbon Footprint across different Transport Modes
data = df[['Mode_of_Transport', 'Carbon_Footprint_kgCO2']].dropna()

# 3. Calculate average Carbon Footprint per Transport Mode
avg_carbon = data.groupby('Mode_of_Transport')['Carbon_Footprint_kgCO2'].mean()
print("--- Average Carbon Footprint by Transport Mode ---")
print(avg_carbon)

# 4. Generate a Box Plot
# A Box Plot is ideal for showing distribution and outliers across categories
plt.figure(figsize=(10, 6))
df.boxplot(column='Carbon_Footprint_kgCO2', by='Mode_of_Transport', patch_artist=True, grid=False)

# 5. Customizing the Visualization
plt.title('Distribution of Carbon Footprint by Transport Mode', fontsize=14)
plt.suptitle('')  # Removes the default pandas title for a cleaner look
plt.xlabel('Mode of Transport', fontsize=12)
plt.ylabel('Carbon Footprint (kgCO2)', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()