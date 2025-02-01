import streamlit as st

def main_p():
    st.title("PakWheels Car Price Predictor 🚗")
    
    st.subheader("🚗 Welcome to the Car Price Predictor!")
    
    st.markdown(
        """
        This application allows users to estimate the price of a used car based on its specifications.
        The dataset used for this model was collected from PakWheels in 2024 and contains details such as:
        - Car model year
        - Engine capacity
        - Fuel type
        - Transmission type
        - Kilometers driven
        
        ### Explore the App:
        - **Report Page**: Provides insights into the dataset, including its features and key statistics.
        - **Exploratory Data Analysis (EDA) Page**: Visualizes important trends in the dataset through graphs and charts.
        - **Prediction Page**: Allows users to input car details and get an estimated price prediction.
        
        Navigate using the sidebar to explore different sections of the app!
        """
    )