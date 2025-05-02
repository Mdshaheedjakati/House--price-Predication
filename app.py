import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Load dataset
@st.cache_data
def load_data():
    data = pd.read_csv("USA_Housing.csv")
    return data

st.set_page_config(page_title="House Price Predictor", layout="centered")

# Title
st.markdown("### 🏠 House Price Predictor")
st.markdown("---")

# Load and clean data
data = load_data()
if "Address" in data.columns:
    data = data.drop(columns=["Address"])

# Simulate location
locations = ["New York", "California", "Texas", "Florida", "Illinois"]
data['Location'] = data.index % len(locations)  # Convert to numeric for modeling

# Sidebar Inputs
location = st.selectbox("📍 Location:", locations)
sqft = st.number_input("📐 Square Feet:", min_value=300, max_value=10000, value=1500, step=50)
bedrooms = st.slider("🛏️ Bedrooms:", min_value=1, max_value=10, value=3)
bathrooms = st.slider("🚿 Bathrooms:", min_value=1, max_value=10, value=2)
parking = st.number_input("🚗 Parking Space:", min_value=0, max_value=5, value=1)

# Map inputs to model input (include Location)
input_df = pd.DataFrame({
    "Avg. Area Income": [70000 + locations.index(location) * 5000],
    "Avg. Area House Age": [7],
    "Avg. Area Number of Rooms": [bedrooms + bathrooms],
    "Avg. Area Number of Bedrooms": [bedrooms],
    "Area Population": [30000 + sqft * 0.2],
    "Location": [locations.index(location)]  # include Location
})

# Model training
X = data.drop(columns=["Price"])
y = data["Price"]
model = LinearRegression()
model.fit(X, y)

# Prediction
if st.button("🔮 Predict Price"):
    prediction = model.predict(input_df)[0]
    st.success(f"💰 Predicted Price: ${prediction:,.0f}")

# Optional: Data Visualization
st.markdown("---")
st.subheader("📊 Data Visualization (Optional)")

# Avg price by fake location
avg_prices = data.groupby('Location')['Price'].mean()
avg_prices.index = locations  # map back to readable names

fig, ax = plt.subplots()
avg_prices.plot(kind='bar', ax=ax, color='skyblue')
plt.ylabel("Average Price")
plt.title("Average House Price by Location")
st.pyplot(fig)
