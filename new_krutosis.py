import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import kurtosis

# Load dataset
df = pd.read_csv("smart_city_citizen_activity.csv")

# -------------------------------
# Kurtosis Analysis
# -------------------------------

# Select clean numerical field
social_media = df["Social_Media_Hours"].dropna()

# Calculate kurtosis
# fisher=False → Normal distribution kurtosis = 3
kurt_social = kurtosis(social_media, fisher=False)

print("\nKurtosis Value:")
print("Social_Me:", kurt_social)

# Plot histogram for kurtosis
plt.figure()
plt.hist(social_media, bins=30, edgecolor="black", alpha=0.75)
plt.title("Kurtosis Analysis – Social Media Usage")
plt.xlabel("Social_Me (Daily Hours/Units)")
plt.ylabel("Frequency")
plt.show()