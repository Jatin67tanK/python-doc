import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Load the specific project dataset
df = pd.read_csv(r"e:\jatin - python\final_cleaned_dataset.csv")

# 2. Select Attributes for Multivariate Analysis
# Analyzing how Age and Resource Score interact across different Lifestyles
num_cols = ['Age', 'Total_Resource_Score']
cat_col = 'Activity_Pattern'
data = df[num_cols + [cat_col]].dropna()

# 3. Statistical Summary Table (Grouped Mean)
print("\nAverage Resource Score by Age and Activity Pattern:")
summary = data.groupby('Activity_Pattern')[['Age', 'Total_Resource_Score']].mean()
print(summary)

# 4. Multivariate Visualization (Scatter Plot with Hue)
plt.figure(figsize=(12, 7))
sns.scatterplot(
    data=data, 
    x="Age", 
    y="Total_Resource_Score", 
    hue="Activity_Pattern", 
    style="Activity_Pattern", 
    palette="viridis", 
    s=100, 
    alpha=0.6
)

# 5. Adding Professional Documentation Title
plt.title("Multivariate Analysis: Age vs. Resource Score by Activity Pattern", fontsize=15)
plt.xlabel("Age (Years)", fontsize=12)
plt.ylabel("Total Resource Score", fontsize=12)
plt.legend(title="Activity Pattern", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True, linestyle='--', alpha=0.4)
plt.tight_layout()
plt.show()