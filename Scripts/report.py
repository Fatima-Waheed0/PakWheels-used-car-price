import streamlit as st

def show_report():
    st.title("PakWheels Cars Dataset Report")
    
    st.header("1. Introduction")
    st.write("""
    This report provides an overview of the PakWheels Used Cars Dataset, which aims to help car buyers 
    estimate the best price for a used car based on its specifications. The dataset was collected in 2024 
    through web scraping techniques and contains detailed information on used cars listed on PakWheels, 
    a leading online automotive marketplace in Pakistan.
    """)
    
    st.header("2. Problem Statement")
    st.write("""
    Many car enthusiasts struggle to find the best price for a vehicle. This report supports the development 
    of an AI-powered car price prediction model that allows users to input specific car details and receive an 
    estimated price. By analyzing trends and relationships within the dataset, we aim to improve car buyers' decision-making.
    """)
    
    st.header("3. Dataset Overview")
    st.subheader("Features in the Dataset")
    st.write("""
    - **Title**: Car listing title as displayed on PakWheels.
    - **Model**: The year of manufacture of the car.
    - **CC (Engine Capacity)**: The displacement of the engine in cubic centimeters (CC).
    - **Engine Type**: The type of fuel used in the engine (e.g., Petrol, Diesel, Hybrid, Electric).
    - **Transmission**: The type of transmission (e.g., Automatic, Manual).
    - **Km Driven**: The total distance driven by the car in kilometers.
    - **Prices**: The car’s listed price in Pakistani Rupees (PKR) in lakhs.
    """)
    
    st.header("4. Why This Dataset?")
    st.write("""
    PakWheels is a trusted automotive marketplace in Pakistan with a large database of used cars. 
    The platform is widely used by buyers and sellers, ensuring reliable and competitive pricing. 
    This dataset provides an excellent foundation for building an AI model to predict car prices based on historical data and market trends.
    """)
    
    st.header("5. Data Collection Process")
    st.write("""
    - The dataset was collected in 2024 using web scraping techniques.
    - Data was gathered from verified listings on PakWheels.
    - The dataset was cleaned to remove irrelevant and duplicate entries.
    """)
    
    st.header("6. Observations")
    st.subheader("Data Types")
    st.write("""
    - The dataset contains 5 categorical columns (Object datatype) and 2 numerical columns.
    - The following columns required datatype adjustments:
      - Model: Converted to Object datatype.
      - CC: Converted to Integer datatype.
      - Km_Driven: Converted to Integer datatype.
    """)
    
    st.subheader("Feature Insights")
    
    st.markdown("**Model Column:**")
    st.write("Most cars were manufactured between 2000 and 2021. A histogram of model years indicates a significant increase in listings during this period.")
    st.image("images/model.jpg")

    
    st.markdown("**Engine Type Column:**")
    st.write("This column consists of the following six fuel types:")
    st.write("""
    - Petrol: 52,035 cars
    - Hybrid: 4,931 cars
    - Diesel: 2,647 cars
    - CNG: 447 cars
    - Electric: 439 cars
    - LPG: 56 cars
    """)
    st.image("images/engine_type.jpg")
    
    
    st.markdown("**Transmission Column:**")
    st.write("The dataset contains two transmission types: Automatic and Manual.")
    
    st.markdown("**CC Column:**")
    st.write("""
    - CC for fuel-powered vehicles.
    - kWh for electric cars.
    - To improve clarity, the column was split into two separate columns:
    - Power: Numerical engine capacity.
    - Unit: The measurement unit (CC/kWh).
    """)
    st.image("images/transmission.jpg")
    
    st.header("7. Summary")
    st.write("""
    This dataset is valuable for developing a car price prediction model. It includes essential car details such as 
    engine size, model year, fuel type, and mileage, all of which influence pricing. Through Exploratory Data Analysis 
    (EDA) and Machine Learning (ML) models, we can derive useful insights that help users make informed car-buying decisions.
    """)
