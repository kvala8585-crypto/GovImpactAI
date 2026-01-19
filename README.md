# 🏛️ GovImpact-AI: Government Policy Impact Prediction System

##  Project Overview
	GovImpact-AI is an end-to-end Machine Learning & Data Science project that predicts the **overall impact score** and **success level** of government policies based on socio-economic indicators.  
The system helps policymakers, analysts, and researchers simulate policy outcomes **before implementation.

This project covers:
- Synthetic real-world dataset generation
- Data cleaning & EDA
- Regression & Classification model training
- Model deployment using Streamlit


##  Problem Statement
Government policies impact GDP growth, employment, education, healthcare, and poverty.  
However, evaluating policy effectiveness beforehand is challenging.

##Goal: 
Predict:
1. Overall Policy Impact Score (Regression)
2. Policy Success Level (Classification: Low / Medium / High / Very High)

## Key Features

🔐 Secure Login & Signup System

📧 Email OTP Verification (5 min expiry)

🗄️ SQLite Database for Users

🔒 Password Hashing (SHA256)

📊 Policy Impact Score Prediction

🏆 Policy Success Level Classification

⚡ Real-time Streamlit Dashboard



##  Project Folder Structure
GovImpact-AI/
│
├── app.py                          # Streamlit web application
├── generate_policy_impact_dataset.py
│
├── data/
│   └── gov_policy_impact_data.csv  # Generated dataset
│
├── model/
│   ├── impact_score_model.pkl      # Regression model
│   └── policy_success_model.pkl    # Classification model
│
├── notebooks/
│   ├── 01_data_cleaning.ipynb
│   ├── 02_eda_analysis.ipynb
│   └── 03_model_training.ipynb
│
├── README.md
└── requirements.txt

---

## Dataset Description
- Records: 3000+
- Country: India
- States: Gujarat, Maharashtra, Delhi, Rajasthan, Karnataka

### Key Features:
- GDP growth (before & after)
- Inflation rate
- Unemployment rate
- Poverty rate
- Health & Education indices
- Policy budget & duration

### Target Variables:
- `overall_impact_score` (Numeric)

- `policy_success_level` (Categorical)


##  Data Cleaning & EDA
✔ Missing value handling  
✔ Feature type validation  
✔ Outlier detection  
✔ Correlation analysis  
✔ Distribution plots  
✔ Policy-wise impact comparison  

Graphs Used:
- Histograms
- Boxplots
- Heatmaps
- Line & Bar charts

---

##  Model Building
### Regression Model
- Algorithm: Random Forest Regressor

- Target: Overall Impact Score

- Metrics: R² Score, MAE, RMSE

### Classification Model

- Algorithm: Random Forest Classifier

- Target: Policy Success Level (Low / Medium / High)


- Metrics: Accuracy, Precision, Recall, F1-score

🔐 Authentication System

- Signup with Email OTP verification

- OTP valid for 5 minutes

- Secure password hashing using SHA256

- User data stored in SQLite database

- Session-based login control

## Demo Login (For Testing)
Email: rkavi6785@gmail.com
Password: 12345678


## Deployment (Streamlit App)

Interactive web app where users:

- Enter policy parameters
- Simulate impact score
- Predict success level instantly

Run app:
```bash
streamlit run app.py
(Install Dependencies
pip install -r requirements.txt
 Run Streamlit App
streamlit run app.py)

## Tech Stack

- Python

- Pandas, NumPy

- Matplotlib, Seaborn

- Scikit-learn

- Streamlit

- Pickle

🌱 Future Enhancements

- Real government open data integration

- Time-series forecasting

- Deep Learning models

-SHAP-based explainability

- Power BI / Tableau dashboard

-Cloud deployment (AWS / Azure)

👨‍💻 Author
Kavi Vala
Data Science & AI Engineer
