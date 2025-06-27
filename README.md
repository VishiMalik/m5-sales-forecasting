# M5 Forecasting: Walmart Daily Sales Prediction (LightGBM)

A time-series machine learning project to predict daily item sales across Walmart stores using the M5 dataset.

## 📊 Objective
Build a model to forecast future sales using:
- Calendar info
- Prices
- Historical sales
- Event information

## 📂 Data Used
- sales_train_validation.csv
- sell_prices.csv
- calendar.csv  
(From M5 Forecasting - Accuracy Kaggle dataset)

## ⚙️ Methods
- Data cleaning & joining with DuckDB
- Feature engineering (lags, rolling stats, time features)
- Train/validation split
- LightGBM regression with early stopping

## ✅ Results
- Validation RMSE: **2.92**
- Model trained on ~6,700 samples

## 📌 Key Features Engineered
- Lag features (`lag_7`, `lag_28`)
- Rolling mean/std
- Event flags
- Normalized & % change in price

## 📈 Next Steps
- Add more months of data
- Compare XGBoost/CatBoost
- Deploy a simple Streamlit dashboard

## 🧠 Skills Demonstrated
- Time-series ML
- DuckDB for SQL on pandas
- Feature engineering
- Model evaluation
