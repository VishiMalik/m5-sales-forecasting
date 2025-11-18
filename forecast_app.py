
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import pickle

st.set_page_config(layout="wide")
st.title("M5 Sales Forecasting Dashboard")

# Load pre-trained LightGBM model
model = pickle.load(open("lgbm_model.pkl", "rb"))

# Load validation data (small sample)
data = pd.read_csv("sample_input.csv")

# Sidebar filters
item_id = st.sidebar.selectbox("Select Item", sorted(data['id'].unique()))
store_id = st.sidebar.selectbox("Select Store", sorted(data['store_id'].unique()))

# Filter data
filtered = data[(data['id'] == item_id) & (data['store_id'] == store_id)]

if not filtered.empty:
    X = X = filtered[['lag_7', 'lag_28', 'dayofweek', 'month', 'is_event',
              'rolling_mean_7', 'rolling_std_7', 'price_norm', 'price_change']]
    y_true = filtered['sales']
    y_pred = model.predict(X)

    # Line plot
    st.subheader("Forecast vs Actual")
    plot_df = pd.DataFrame({
        'Date': filtered['date'],
        'Actual Sales': y_true,
        'Predicted Sales': y_pred
    })
    plot_df.set_index('Date', inplace=True)
    st.line_chart(plot_df)

    # Feature importance (optional)
    st.subheader("Feature Importances")
    importances = model.feature_importances_
    feature_names = X.columns
    imp_df = pd.DataFrame({'Feature': feature_names, 'Importance': importances}).sort_values(by='Importance', ascending=False)
    st.bar_chart(imp_df.set_index('Feature'))
else:
    st.warning("No data available for selected item and store.")
