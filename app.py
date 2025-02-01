import streamlit as st

# Set page config as the first Streamlit command
st.set_page_config(page_title='PakWheel Car Price', page_icon='🚗')

# Now import other modules
from Scripts.report import show_report
from Scripts.eda import show_eda
from Scripts.main_page import main_p
from Scripts.prediction import show_prediction

st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Go to", [ "Main Page" ,"EDA", "Report", "Prediction"])

if page == "Main Page":
    main_p()
elif page == "Report":
    show_report()
elif page == "EDA":
    show_eda()
elif page == "Prediction":
    show_prediction()
