import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Load the dataset
df = pd.read_csv("smart_city_citizen_activity.csv")


# 2. Define the target columns (Updated based on your provided list)
# Note: Ensure these names match the printed list in your terminal
skew_columns = ['Home_Energy_Consumption_kWh', 'Steps_Walked', 'Charging_Station_Usage']

# 3. Calculate Skewness and Interpret Results
print("\n--- Smart City Skewness Report ---")
for col in skew_columns:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')
        s_val = df[col].skew()
        
        if s_val > 0.5:
            category = "Positive Skew (Right-Tailed)"
        elif s_val < -0.5:
            category = "Negative Skew (Left-Tailed)"
        else:
            category = "Symmetric (Balanced)"
            
        print(f"{col}: {s_val:.3f} | Result: {category}")
    else:
        print(f"Column '{col}' not found! Check spelling in your CSV.")

# 4. Generate Visual Distributions
plt.figure(figsize=(15, 5))
plot_count = 1
for col in skew_columns:
    if col in df.columns:
        plt.subplot(1, 3, plot_count)
        sns.histplot(df[col].dropna(), kde=True, color="darkcyan", bins=15)
        plt.title(f"{col}\nSkewness: {df[col].skew():.2f}")
        plot_count += 1

plt.tight_layout()
plt.show()