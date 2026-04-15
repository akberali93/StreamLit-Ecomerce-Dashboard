import streamlit as st #streamlit -Frontend framework
import pandas as pd # data wrangling library in python
import plotly.express as px # Dynamic Visualization library in python

st.title("E-Commerce Sales Analysis Dashboard") 
# data=pd.read_csv("supermarket_sales.csv") 
# st.dataframe(data)

def load_data(file_path):
    data=pd.read_csv(file_path)
    return data
data_path="./supermarket_sales.csv"  
data=load_data(data_path) 
st.dataframe(data)

select_branch=st.sidebar.multiselect("Select Branch", options=data["Branch"].unique())
select_product_line=st.sidebar.multiselect("Select Product Line", options=data["Product line"].unique())
select_customer_type=st.sidebar.multiselect("Select Customer Type", options=data["Customer type"].unique())

filtered_data=data[(data["Branch"].isin(select_branch)) & (data["Product line"].isin(select_product_line)) & (data["Customer type"].isin(select_customer_type))]
st.dataframe(filtered_data)
 