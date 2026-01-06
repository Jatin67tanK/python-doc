# Handle missing values 
import pandas as pd

df = pd.read_csv("smart_city_citizen_activity.csv")  

# Fill missing numerical values with median
num_cols = df.select_dtypes(include=['float64','int64']).columns
for col in num_cols:
    df[col].fillna(df[col].median(), inplace=True)

# Fill missing categorical values with mode (e.g., Gender)
cat_cols = df.select_dtypes(include=['object']).columns
for col in cat_cols:
    df[col].fillna(df[col].mode()[0], inplace=True)

# Verify no missing values remain
print("\nAfter handling missing values:")
print(df.isnull().sum())