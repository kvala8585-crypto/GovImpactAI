import pandas as pd
from sklearn.preprocessing import LabelEncoder
import os

BASE_PATH = r"C:\Users\kavi vala\Desktop\GovImpact-AI"
DATA_PATH = os.path.join(BASE_PATH, "data", "gov_policy_impact_data.csv")

df = pd.read_csv(DATA_PATH)

le = LabelEncoder()

for col in df.columns:
    if df[col].dtype == "object":
        df[col] = le.fit_transform(df[col])

df.to_csv(DATA_PATH, index=False)
print("✅ Feature Engineering Completed")
