# 📦 M5 Forecasting: Walmart Daily Sales Prediction (LightGBM)

A full end-to-end **time-series forecasting project** using the **M5 Walmart dataset**, focused on predicting daily item-level sales using **LightGBM regression**.

---

## 📊 Objective
Build a highly accurate ML model that predicts future sales using:
- Calendar features  
- Price features  
- Historical lag features  
- Event and holiday information  

This project demonstrates **retail demand forecasting**, **feature engineering**, and **model evaluation**.

---

## 📂 Dataset
From **M5 Forecasting – Accuracy (Kaggle)**:

- `sales_train_validation.csv` – historical sales  
- `sell_prices.csv` – item-store weekly prices  
- `calendar.csv` – date mapping + events  

---

## ⚙️ Workflow / Methods
- Performed **data cleaning** and SQL-style joins using **DuckDB**
- Generated advanced **time-series features**  
- Created lag and rolling statistics  
- Split the dataset into **train / validation sets**
- Trained a **LightGBM Regressor** with early stopping
- Evaluated using **RMSE (Root Mean Squared Error)**

---

## 🧮 Model Results
- **Validation RMSE:** 2.92  
- Model trained on ~6,700 samples (subset for demonstration)
- Early stopping used to prevent overfitting

---

## 🧱 Key Features Engineered
- **Lag Features:**  
  - `lag_7`, `lag_28`
- **Rolling Statistics:**  
  - `rolling_mean_7`, `rolling_std_7`
- **Price Features:**  
  - Normalized price  
  - % change in price  
- **Calendar Features:**  
  - Day of week, month, year  
  - Event names / event types  
- **One-hot / categorical encodings**

---

## 📈 Next Steps
- Train on the **full dataset** (all 30,490 items)
- Add more lag windows (14, 60, 90)
- Compare with:
  - **XGBoost**
  - **CatBoost**
  - **Deep Learning (LSTM / TFT)**
- Build a **Streamlit dashboard** for interactive forecasting

---

## 🧠 Skills Demonstrated
- Time-series ML  
- Feature engineering  
- SQL on Pandas with DuckDB  
- Model training & tuning  
- RMSE evaluation  
- Deployment using Streamlit  

---

## 🚀 Live Demo (Streamlit App)
https://m5-sales-forecasting.streamlit.app/

---

## 📌 Tech Stack
- Python  
- Pandas / NumPy  
- DuckDB  
- LightGBM  
- Scikit-learn  
- Streamlit  

---

## 📄 Project Structure
