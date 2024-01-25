#import statements
import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier
from PIL import Image, ImageFilter, ImageEnhance
import os

#start
st.write("""
# Penguin Prediction App
- This app predicts the species of Palmer penguins found in Antarctica using Machine Learning!
- App built by Pranav Sawant and Anshuman Shukla of Team Skillocity.
- Dataset credits: Dr.Kristen Gorman and Palmer Station, Antarctica LTER and Allison Horst.
- Note: User inputs for features are taken from the sidebar. It is located at the top left of the page (arrow symbol). The values of parameters can be changed from the sidebar.
""")

st.sidebar.header('User Input Features')

#inputs
def user_input_features():
    island = st.sidebar.selectbox('Island', ('Biscoe', 'Dream', 'Torgersen'))
    sex = st.sidebar.selectbox('Sex', ('male', 'female'))
    bill_length_mm = st.sidebar.slider('Bill length (mm)', 32.1, 59.6, 43.9)
    bill_depth_mm = st.sidebar.slider('Bill depth (mm)', 13.1, 21.5, 17.2)
    flipper_length_mm = st.sidebar.slider('Flipper length (mm)', 172.0, 231.0, 201.0)
    body_mass_g = st.sidebar.slider('Body mass (g)', 2700.0, 6300.0, 4207.0)
