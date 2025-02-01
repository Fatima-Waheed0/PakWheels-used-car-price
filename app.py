import streamlit as st

# Set page config first
st.set_page_config(page_title='PakWheel Car Price', page_icon='🚗', layout="wide")

# Import other modules
from Scripts.report import show_report
from Scripts.eda import show_eda
from Scripts.main_page import main_p
from Scripts.prediction import show_prediction

# Apply custom CSS for UI enhancements
st.markdown("""
    <style>
        /* Sidebar Styling */
        [data-testid="stSidebar"] {
            background: linear-gradient(135deg, #1e3c72, #2a5298);
            color: white;
        }
        
        /* Sidebar Title */
        .sidebar-title {
            font-size: 24px;
            font-weight: bold;
            text-align: center;
            margin-bottom: 10px;
            color: white;
        }

        /* Fix for Sidebar Dropdown (Selectbox) */
        div[data-baseweb="select"] {
            background-color: white !important;
            color: black !important;
            border-radius: 10px;
            padding: 5px;
        }

        /* Gradient Title */
        .main-title {
            font-size: 40px;
            font-weight: bold;
            text-align: center;
            background: -webkit-linear-gradient(left, #12c2e9, #c471ed, #f64f59);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: fadeIn 2s ease-in-out;
        }

        /* Smooth Hover Effects */
        div[data-testid="stSidebarNav"] > div > button {
            transition: all 0.3s ease-in-out;
            padding: 10px;
            border-radius: 8px;
        }

        div[data-testid="stSidebarNav"] > div > button:hover {
            transform: scale(1.05);
            background: white !important;
            color: black !important;
            font-weight: bold;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
        }

        /* Keyframe Animations */
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }

    </style>
""", unsafe_allow_html=True)

# Sidebar Design
st.sidebar.image('images/log.png', use_container_width =True)
st.sidebar.markdown('<div class="sidebar-title">Select Page</div>', unsafe_allow_html=True)
st.sidebar.write("You can select a page from here:")

# Sidebar Navigation
page = st.sidebar.selectbox("", ["Main Page", "EDA", "Report", "Prediction"])

# Title with Gradient Effect
st.markdown('<h1 class="main-title">PakWheel Car Price Prediction</h1>', unsafe_allow_html=True)

# Load Pages Dynamically
if page == "Main Page":
    main_p()
elif page == "Report":
    show_report()
elif page == "EDA":
    show_eda()
elif page == "Prediction":
    show_prediction()
