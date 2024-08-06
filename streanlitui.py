import streamlit as st
from keras.models import load_model
from keras.preprocessing import image
import numpy as np
import os

# Load the pre-trained model
model_path = 'gender_recognition.h5'
model = load_model(model_path)


# Function to classify image
def classify_image(img):
    img = img.resize((150, 150))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0

    prediction = model.predict(img_array)
    if prediction[0][0] > 0.5:
        return 'Male', prediction[0][0]
    else:
        return 'Female', 1 - prediction[0][0]


# Streamlit UI
st.title("Gender Recognition Model")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    img = image.load_img(uploaded_file)
    st.image(img, caption='Uploaded Image', use_column_width=True)
    label, confidence = classify_image(img)
    st.write(f"Prediction: {label} with {confidence:.2f} confidence")