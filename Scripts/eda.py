import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

def box_plot(data, column):
    fig = px.box(data, y=column)
    st.plotly_chart(fig)

def histogram(data, column):
    fig = px.histogram(data, x=column, nbins=30, marginal="box")
    st.plotly_chart(fig)

def kde_plot(data, column):
    fig = px.histogram(data, x=column, nbins=30, histnorm='probability density', marginal="box")
    st.plotly_chart(fig)

def pie_chart(data, column):
    fig = px.pie(data, names=column, title=f"{column} Distribution", hole=0.3)
    st.plotly_chart(fig)

def bar_plot(data, column):
    fig = px.bar(data[column].value_counts().reset_index(), x='index', y=column)
    st.plotly_chart(fig)

def scatter_plot(data, x_column, y_column):
    fig = px.scatter(data, x=x_column, y=y_column, title=f"{x_column} vs {y_column}")
    st.plotly_chart(fig)

def line_plot(data, x_column, y_column):
    fig = px.line(data, x=x_column, y=y_column, title=f"{x_column} vs {y_column}")
    st.plotly_chart(fig)

def multivariate_plot(data, x_column, y_column, color_column):
    fig = px.scatter(data, x=x_column, y=y_column, color=color_column, title=f"{x_column} vs {y_column} colored by {color_column}")
    st.plotly_chart(fig)

def show_eda():
    st.title("Exploratory Data Analysis (EDA)")
    data = pd.read_csv("Data/preprocessing.csv")
    
    global numerical_columns, categorical_columns
    numerical_columns = ['Km_Driven', 'prices', 'Power']
    categorical_columns = ['Title', 'Engine_type', 'Transmission', 'Unit']
    
    analysis_type = st.selectbox("Select Analysis Type:", ["Univariate", "Bivariate", "Multivariate"])
    
    if analysis_type == "Univariate":
        plot_type = st.selectbox("Select Plot Type:", ["Box Plot", "Histogram", "KDE", "Pie Chart", "Bar Plot"])
        applicable_columns = numerical_columns if plot_type in ["Box Plot", "Histogram", "KDE"] else categorical_columns
        column = st.selectbox("Select Column:", applicable_columns)
        if st.button("Generate Plot"):
            if plot_type == "Box Plot":
                box_plot(data, column)
            elif plot_type == "Histogram":
                histogram(data, column)
            elif plot_type == "KDE":
                kde_plot(data, column)
            elif plot_type == "Pie Chart":
                pie_chart(data, column)
            elif plot_type == "Bar Plot":
                bar_plot(data, column)
    
    elif analysis_type == "Bivariate":
        plot_type = st.selectbox("Select Plot Type:", ["Scatter Plot", "Line Plot", "Bar Plot"])
        x_column = st.selectbox("Select X-axis Column:", numerical_columns + categorical_columns)
        y_column = st.selectbox("Select Y-axis Column:", numerical_columns + categorical_columns)
        if st.button("Generate Plot"):
            if plot_type == "Scatter Plot":
                scatter_plot(data, x_column, y_column)
            elif plot_type == "Line Plot":
                line_plot(data, x_column, y_column)
            elif plot_type == "Bar Plot":
                bar_plot(data, x_column)
    
    elif analysis_type == "Multivariate":
        x_column = st.selectbox("Select X-axis Column:", numerical_columns + categorical_columns)
        y_column = st.selectbox("Select Y-axis Column:", numerical_columns + categorical_columns)
        color_column = st.selectbox("Select Color Column:", categorical_columns)
        if st.button("Generate Plot"):
            multivariate_plot(data, x_column, y_column, color_column)
