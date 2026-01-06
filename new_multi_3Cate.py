import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Load the specific project dataset
df = pd.read_csv(r"e:\jatin - python\final_cleaned_dataset.csv")

# 2. CREATE THE Age_Group COLUMN
def categorize_age(age):
    if age < 30: return 'Young'
    elif age < 60: return 'Adult'
    else: return 'Senior'

df['Age_Group'] = df['Age'].apply(categorize_age)

# 3. Create a combined column for a single X-axis view
# This merges Activity and Age so we can see everything in one plot
df['Activity_Age'] = df['Activity_Pattern'] + " (" + df['Age_Group'] + ")"

# 4. Select Categorical Attributes
cat_cols = ['Activity_Age', 'Satisfaction_Level']
data = df[cat_cols].dropna()

# 5. Statistical Summary Table (Cross-tabulation)
print("\nFrequency Table: Consolidated Activity & Age vs Satisfaction")
summary = pd.crosstab(data['Activity_Age'], data['Satisfaction_Level'])
print(summary)

# 6. Consolidated Grouped Bar Chart (One Single Plot)
plt.figure(figsize=(12, 7))
sns.countplot(
    data=data, 
    x="Activity_Age", 
    hue="Satisfaction_Level", 
    palette="viridis",
    edgecolor='black'
)

# 7. Professional Formatting
plt.title("Consolidated Multivariate Analysis: Activity & Age vs. Satisfaction", fontsize=15, pad=20)
plt.xlabel("Activity Pattern (Age Group)", fontsize=12)
plt.ylabel("Number of Citizens", fontsize=12)
plt.xticks(rotation=45) # Rotate labels for better readability
plt.legend(title="Satisfaction Level", loc='upper right')
plt.grid(axis='y', linestyle='--', alpha=0.3)
plt.tight_layout()
plt.show()