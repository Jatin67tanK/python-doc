import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Load the dataset
df = pd.read_csv("smart_city_citizen_activity.csv")

# 2. Select the New Suggested Columns
num_cols = ['Age', 'Steps_Walked', 'Calories_Burned']
data = df[num_cols].dropna()

# 3. Statistical Summary Table
print("\nFrequency / Statistical Summary Table:")
print(data.describe())

# 4. Pair Plot (The Visual Multivariate Tool)
# 'hue' can be added if you want to color code by a category like Gender
sns.pairplot(data, diag_kind='hist', plot_kws={'color':'teal', 'alpha':0.5})

# Adding Professional Title
plt.suptitle("Multivariate Analysis: Age vs. Steps vs. Calories", y=1.02, fontsize=14)
plt.show()      