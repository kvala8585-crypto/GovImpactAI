import pandas as pd
import matplotlib.pyplot as plt
import os

BASE_PATH = r"C:\Users\kavi vala\Desktop\GovImpact-AI"
DATA_PATH = os.path.join(BASE_PATH, "data", "gov_policy_impact_data.csv")

df = pd.read_csv(DATA_PATH)

print(df.info())
print(df.describe())

# Policy type distribution
df["policy_type"].value_counts().plot(kind="bar", title="Policy Type Distribution")
plt.show()

# Average impact score by policy type
df.groupby("policy_type")["overall_impact_score"].mean().plot(
    kind="bar", title="Avg Impact Score by Policy Type"
)
plt.show()

# Before vs After GDP
plt.scatter(df["gdp_growth_before"], df["gdp_growth_after"])
plt.xlabel("GDP Growth Before")
plt.ylabel("GDP Growth After")
plt.title("GDP Growth Impact")
plt.show()

print("✅ EDA & Policy Comparison Completed")
