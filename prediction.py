import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier
from PIL import Image,ImageFilter,ImageEnhance
import os

st.write("""
# Penguin Prediction App
- This app predicts the species of Palmer penguins found in Antarctica using Machine Learning!
- App built by Pranav Sawant and Anshuman Shukla of Team Skillocity.
- Dataset credits: Dr.Kristen Gorman and Palmer Station, Antarctica LTER and Allison Horst.
- Note: User inputs for features are taken from the sidebar. It is located at the top left of the page (arrow symbol). The values of parameters can be changed from the sidebar.
""")

st.sidebar.header('User Input Features')


def user_input_features():
        island = st.sidebar.selectbox('Island',('Biscoe','Dream','Torgersen'))
        sex = st.sidebar.selectbox('Sex',('male','female'))
        bill_length_mm = st.sidebar.slider('Bill length (mm)', 32.1,59.6,43.9)
        bill_depth_mm = st.sidebar.slider('Bill depth (mm)', 13.1,21.5,17.2)
        flipper_length_mm = st.sidebar.slider('Flipper length (mm)', 172.0,231.0,201.0)
        body_mass_g = st.sidebar.slider('Body mass (g)', 2700.0,6300.0,4207.0)
        data = {'island': island,
                'bill_length_mm': bill_length_mm,
                'bill_depth_mm': bill_depth_mm,
                'flipper_length_mm': flipper_length_mm,
                'body_mass_g': body_mass_g,
                'sex': sex}
        features = pd.DataFrame(data, index=[0])
        return features
input_df = user_input_features()
  
st.subheader('User Input parameters')
st.write(input_df)
        

penguins_raw = pd.read_csv('penguins_cleaned.csv')
penguins = penguins_raw.drop(columns=['species'])
df = pd.concat([input_df,penguins],axis=0)


encode = ['sex','island']
for col in encode:
    dummy = pd.get_dummies(df[col], prefix=col)
    df = pd.concat([df,dummy], axis=1)
    del df[col]
df = df[:1] # Selects only the first row (the user input data)





load_clf = pickle.load(open('penguins_clf.pkl', 'rb'))


prediction = load_clf.predict(df)
prediction_proba = load_clf.predict_proba(df)



st.subheader('Prediction')
penguins_species = np.array(['Adelie','Chinstrap','Gentoo'])
st.write(penguins_species[prediction])

st.subheader('Prediction Probability')
st.write(prediction_proba)

@st.cache
def load_image(img):
    im =Image.open(os.path.join(img))
    return im

if penguins_species[prediction] == 'Chinstrap':
    st.text("Showing Chinstrap Penguin")
    st.image(load_image('chinstrap.jpg'))
elif penguins_species[prediction] == 'Gentoo':
    st.text("Showing Gentoo Penguin")
    st.image(load_image('gentoo.jpg'))
elif penguins_species[prediction] == 'Adelie':
    st.text("Showing Adelie Penguin")
    st.image(load_image('adelie.jpg'))
