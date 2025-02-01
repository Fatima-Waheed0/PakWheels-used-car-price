import streamlit as st
import pickle
import numpy as np
import pandas as pd
from Scripts.utils import car_models, company_name

@st.cache_data
def load_model():
    with open('predictive_model.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

model = load_model()



def predict_price(model_year, engine_type, transmission, km_driven, power, unit, company, model_name):
    # Create a DataFrame with the correct column names as expected by the model
    features = pd.DataFrame([{
        'Model': model_year,
        'Engine_type': engine_type,
        'Transmission': transmission,
        'Km_Driven': km_driven,
        'Power': power,
        'Unit': unit,
        'Company': company,
        'Model_name': model_name
    }])
    
    # Predict the price using the model
    predicted_price = model.predict(features)[0]
    
    return predicted_price

def show_prediction():
    st.title("Car Price Prediction")
    
    st.markdown("Enter the details of the car to estimate its price:")
    
    years = [str(year) for year in range(1980, 2026)]  
    year = years[::-1]
    model_year = st.selectbox("Model Year", year)
    model_year = int(model_year)  # Convert the selected year to an integer

    fuel_type = st.selectbox("Fuel Type", ["Petrol", "Hybrid", "Diesel", "CNG", "Electric", "LPG"])
    transmission = st.selectbox("Transmission Type", ["Automatic", "Manual"])
    
    km_driven = st.number_input("Kilometers Driven")
    power = st.number_input("Power (in kW)")
    
    unit = st.selectbox("Unit", ["CC", "kWh"])
    company = st.selectbox("Car Company", company_name)
    model_name = st.selectbox("Model Name", car_models)
    
    if st.button("Predict Price"):
        predicted_price = predict_price(model_year, fuel_type, transmission, km_driven, power, unit, company, model_name)
        st.success(f"Estimated Car Price: PKR {predicted_price:,.2f} Lakhs")


