import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

import json
import requests

#Title
st.markdown("<h1 style='text-align: center; color: White; font-size:50px; '>Marketing Dashboard</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: Center; color: White; font-size:20px; '>This dashboard will help you get more information about the Marketing datasets and their output</h2>",unsafe_allow_html=True)

#Background Image
import base64
def add_bg_from_local(image_file):
    with open(image_file,"rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-Image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>""",
    unsafe_allow_html=True
    )
add_bg_from_local('Background Image.png')
        
#Separating orderbook and trade columns
df=pd.read_json('data.json')

l0 = df.columns
l1 = []
l2 = []

i=0
for i,x in enumerate (l0) :
    if 'orderbook' in x :
        l1.append(x)
    elif 'trade' in x:
        l2.append(x)
    i += 1

df1 = pd.DataFrame(l1)
df2 = pd.DataFrame(l2) 

# Functions for each of the pages
#All types of charts

#Adding dataframe in a button to show

st.sidebar.title("Selecting Visual Charts")
st.sidebar.markdown("Selecting the Charts accordingly.")

st.sidebar.markdown("<h3 style='text-align: left; color: Black; font-size:15px; '>Show Analysis Status</h1>", unsafe_allow_html=True)
Dataset = st.sidebar.checkbox("Show Status", False, key = 1)


if Dataset:     
    st.write(df)

#data = pd.read_json(r"D:\Excelr DataScience\Deployment\Marketing Dashboard\data.json")
chart_visual = st.sidebar.selectbox('Select Visual Charts', ('Select Option','Pie Chart', 'Line Chart', 'Bar Chart'))
    
def interactive_plot1(l0):
    st.markdown("<h2 style='text-align: center; color: White; font-size:25px; '>Line Chart</h2>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    x_axis_val = col1.selectbox('', options=df1)
    y_axis_val = col2.selectbox('', options=df2)
    
    plot = px.line(df, x=x_axis_val, y=y_axis_val)
    st.plotly_chart(plot)
    
def interactive_plot2(l0):
    st.markdown("<h2 style='text-align: center; color: White; font-size:25px; '>Bar Chart</h2>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    
    x_axis_val = col1.selectbox('Select the X-axis', options=df1)
    y_axis_val = col2.selectbox('Select the Y-axis', options=df2)

    plot = px.bar(df, x=x_axis_val, y=y_axis_val)
    st.plotly_chart(plot)
    
def interactive_plot3(l0):
    st.markdown("<h2 style='text-align: center; color: White; font-size:25px; '>Pie Chart</h2>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    
    x = col1.selectbox('Select the X-axis', options=df1)
    y = col2.selectbox('Select the Y-axis', options=df2)

    plot = px.pie(df, x, y)
    st.plotly_chart(plot)
    
#Sidebar navigation
#st.sidebar.title('Navigation')
#option=st.sidebar.radio('Select what you want to display:',['Line Chart','Bar Chart','Area Chart','Scatter Chart'])

# Navigation options
if chart_visual == 'Line Chart':
  interactive_plot1(df)
elif chart_visual == 'Bar Chart':
  interactive_plot2(df)
elif chart_visual == 'Pie Chart':
  interactive_plot3(df)


