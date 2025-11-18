# 📦 M5 Forecasting: Walmart Daily Sales Prediction (LightGBM)

A full end-to-end **time-series forecasting project** using the M5 Walmart dataset, focused on predicting daily item-level sales with **LightGBM regression**.

---

## 📊 Objective
Build a machine learning model to forecast future sales using:
- Calendar information  
- Price features  
- Historical sales lags  
- Event indicators  

---

## 📂 Dataset
From **M5 Forecasting – Accuracy (Kaggle)**:

- `sales_train_validation.csv`  
- `sell_prices.csv`  
- `calendar.csv`

---

## ⚙️ Workflow
- Data cleaning and joining using **DuckDB**
- Time-series feature engineering  
- Train/validation split based on dates  
- LightGBM regression with early stopping  
- Evaluation using RMSE  

---

## ✅ Model Results (Corrected)
- **Validation RMSE:** **2.0733**
- **Training data used:**
  - **5,674,189 samples**  
  - **9 features**
- **Validation data used:**
  - **73,176 samples**  
  - **9 features**
- Early stopping (50 rounds) used to avoid overfitting

---

## 🧱 Key Features Engineered
- Lag features: `lag_7`, `lag_28`
- Rolling stats: `rolling_mean_7`, `rolling_std_7`
- Price movement: normalized price, % change
- Calendar-based: day, week, month, event flags

---

## 📈 Next Steps
- Train on full 30k+ SKU dataset  
- Try XGBoost / CatBoost  
- Add more lag windows (14, 60, 90)  
- Deploy an advanced interactive Streamlit dashboard  

---

## 🧠 Skills Demonstrated
- Feature engineering for time-series ML  
- DuckDB for fast SQL joins  
- LightGBM model training  
- RMSE-based evaluation  
- Deployment with Streamlit  

---

## 🚀 Live Streamlit App  
https://m5-sales-forecasting.streamlit.app/

---

## 📄 Project Structure
