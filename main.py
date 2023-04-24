import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

# Add a title widget
st.title("In Search for Happiness")

# Add two selectboxes
x_axis = st.selectbox("Select the data for the X-axis", ("GDP", "Happiness", "Generosity"))

y_axis = st.selectbox("Select the data for the Y-axis", ("GDP", "Happiness", "Generosity"))

# Load the dataframe
df = pd.read_csv("happy.csv")

match x_axis:
    case "Happiness":
        x_array = df["happiness"]
    case "GDP":
        x_array = df["gdp"]
    case "Generosity":
        x_array = df["generosity"]

match y_axis:
    case "Happiness":
        y_array = df["happiness"]
    case "GDP":
        y_array = df["gdp"]
    case "Generosity":
        y_array = df["generosity"]

st.subheader(f"{x_axis} and {y_axis}")

figure = px.scatter(x = x_array, y = y_array, labels={"x": x_axis, "y": y_axis})
st.plotly_chart(figure)