import streamlit as st 
import pandas as pd 
import numpy as np 
import joblib


st.title("Laptop Price Predictor")


nav = st.sidebar.radio("Nav Bar", ["Hoime" , "Predictor" , "Contact Us"])
if nav =="Hoime":
    st.write("# Habbibi !! Welcome !  Jai Balayya")
    st.write("## Head over to predictor on left  to know your Lappy Price ! ")


if nav== "Predictor":
    speed = st.slider('speed', min_value=1.0, max_value=5.0, step=0.1)
    ram = st.slider('ram', min_value=1, max_value=32)
    storage_capacity = st.slider('capacity', min_value=128, max_value=2048, step=128)
    screen_size = st.slider('size', min_value=10.0, max_value=17.0, step=0.1)
    weight = st.slider('weight', min_value=1.0, max_value=5.0, step=0.1)


    acer = st.checkbox(' Acer')
    asus = st.checkbox('Asus')
    dell = st.checkbox('Dell')
    hp = st.checkbox(' HP')
    lenovo = st.checkbox('Lenovo')
    input_data ={
        speed   :"speed",
        ram         :"ram",
     storage_capacity   :"capacity",
        screen_size       :"size",
        weight           :"weight",
        acer        :"acer",
        asus        :"asus",
        dell        :"dell",
        hp          :"hp",
        lenovo      :"lenovo"
    }
    input_df= pd.DataFrame([input_data])
    if st.button("Predict"):
        model_path=r"C:\Users\Administrator\Desktop\laptop_price_regressor"
        model = joblib.load(model_path)
        predict_price = model.predict(input_df)[0]
        st.write("Price could be :", predict_price)
if nav=="Contact Us":
    st.write("Akkado AKkada unata le nekku anduku mowa")