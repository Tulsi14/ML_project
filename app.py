import streamlit as st
import pandas as pd
import numpy as np
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

# Page configuration
st.set_page_config(page_title="Student Performance Prediction", layout="centered")

st.title("Student Performance Indicator")
st.markdown("### Predict student exam performance based on demographic data")

# --- User Input Form ---
with st.form("prediction_form"):
    st.subheader("Enter Student Details:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        gender = st.selectbox("Gender", ["male", "female"])
        ethnicity = st.selectbox("Race/Ethnicity", ["group A", "group B", "group C", "group D", "group E"])
        parental_level_of_education = st.selectbox(
            "Parental Level of Education",
            ["associate's degree", "bachelor's degree", "high school", "master's degree", "some college", "some high school"]
        )
    
    with col2:
        lunch = st.selectbox("Lunch Type", ["standard", "free/reduced"])
        test_preparation_course = st.selectbox("Test Preparation Course", ["none", "completed"])
        reading_score = st.number_input("Reading Score", min_value=0, max_value=100, value=50)
        writing_score = st.number_input("Writing Score", min_value=0, max_value=100, value=50)

    # Submit button
    submit_button = st.form_submit_button(label="Predict Performance")

# --- Prediction Logic ---
if submit_button:
    # 1. Initialize CustomData object
    data = CustomData(
        gender=gender,
        race_ethnicity=ethnicity,
        parental_level_of_education=parental_level_of_education,
        lunch=lunch,
        test_preparation_course=test_preparation_course,
        reading_score=float(reading_score),
        writing_score=float(writing_score)
    )

    # 2. Convert to DataFrame
    pred_df = data.get_data_as_data_frame()
    st.write("Input Dataframe:", pred_df) # Debugging ke liye data dikhayega

    # 3. Predict using Pipeline
    predict_pipeline = PredictPipeline()
    results = predict_pipeline.predict(pred_df)

    # 4. Show Result
    st.success(f"The predicted Student Performance Score is: **{results[0]:.2f}**")