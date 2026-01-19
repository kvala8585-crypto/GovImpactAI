import pandas as pd
import os
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

BASE_PATH = r"C:\Users\kavi vala\Desktop\GovImpact-AI"
DATA_PATH = os.path.join(BASE_PATH, "data", "gov_policy_impact_data.csv")
MODEL_PATH = os.path.join(BASE_PATH, "model", "impact_score_model.pkl")

df = pd.read_csv(DATA_PATH)

TARGET = "overall_impact_score"
X = df.drop(TARGET, axis=1)
y = df[TARGET]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)

pred = model.predict(X_test)
print("R2 Score:", r2_score(y_test, pred))

with open(MODEL_PATH, "wb") as f:
    pickle.dump(model, f)

print("✅ Regression Model Trained & Saved")
