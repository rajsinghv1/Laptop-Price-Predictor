import streamlit as st
import pickle
import numpy as np
import pandas as pd

# import the model
pipe = pickle.load(open('pipe.pkl', 'rb'))
df = pickle.load(open('df.pkl', 'rb'))

st.title("Laptop Price Predictor")

# Brand
company = st.selectbox('Brand', df['Company'].unique())

# Type of laptop
laptop_type = st.selectbox('Type', df['TypeName'].unique())

# RAM
ram = st.selectbox('RAM (in GB)', [2, 4, 6, 8, 12, 16, 24, 32, 64])

# Weight
weight = st.number_input('Weight of the Laptop')

# Touchscreen
touchscreen = st.selectbox('Touchscreen', ['No', 'Yes'])

# IPS display
ips = st.selectbox('IPS Display', ['No', 'Yes'])

# Screen Size
screen_size = st.number_input('Screen Size')

# Resolution
resolution = st.selectbox('Screen Resolution', [
    '1920x1080', '1366x768', '1600x900', '3840x2160',
    '3200x1800', '2880x1800', '2560x1600', '2560x1440', '2304x1440'
])

# CPU brand
cpu = st.selectbox('CPU Brand', df['Cpu brand'].unique())

# HDD
hdd = st.selectbox('HDD (in GB)', [0, 128, 256, 512, 1024, 2048])

# SSD
ssd = st.selectbox('SSD (in GB)', [0, 8, 128, 256, 512, 1024])

# GPU brand
gpu = st.selectbox('GPU Brand', df['Gpu brand'].unique())

# Operating System
os = st.selectbox('Operating System', df['os'].unique())

# Predict Button
if st.button('Predict Price'):
    try:
        # Convert inputs
        touchscreen_val = 1 if touchscreen == 'Yes' else 0
        ips_val = 1 if ips == 'Yes' else 0
        X_res = int(resolution.split('x')[0])
        Y_res = int(resolution.split('x')[1])
        ppi = ((X_res ** 2 + Y_res ** 2) ** 0.5) / screen_size

        # Create DataFrame with proper column names
        query_df = pd.DataFrame([{
            'Company': company,
            'TypeName': laptop_type,
            'Ram': ram,
            'Weight': weight,
            'Touchscreen': touchscreen_val,
            'Ips': ips_val,
            'ppi': ppi,
            'Cpu brand': cpu,
            'HDD': hdd,
            'SSD': ssd,
            'Gpu brand': gpu,
            'os': os
        }])

        # Predict and show result
        prediction = pipe.predict(query_df)[0]
        final_price = int(np.exp(prediction))
        st.success(f" Predicted Laptop Price: ₹ {final_price:,}")

    except Exception as e:
        st.error(f" Prediction failed: {e}")
