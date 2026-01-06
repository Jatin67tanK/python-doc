import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("./smart_city_citizen_activity.csv")

# Select Mode_of_Transport column and remove missing values
transport = df["Mode_of_Transport"].dropna()

# Count frequency of each transport mode
transport_counts = transport.value_counts()
print("Univariate Analysis of Mode of Transport:")
print(transport_counts)

# Plot pie chart
plt.figure(figsize=(7,7))
plt.pie(transport_counts, labels=transport_counts.index, autopct='%1.1f%%', startangle=140)
plt.title("Distribution of Transport Modes Among Citizens")
plt.show()