import streamlit as st
import pandas as pd

# CSV file path to save data
csv_file = 'data.csv'

# Streamlit form layout
st.title("🧠 Brain Stroke Risk Data Entry")

s_data = pd.read_csv(csv_file)
st.write("Data")
st.write(s_data.head())

# Layout for form input
col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    age = st.slider("Age", 0, 100, 30)
    hypertension = st.selectbox("Hypertension", ["No", "Yes"])
    heart_disease = st.selectbox("Heart Disease", ["No", "Yes"])
    ever_married = st.selectbox("Ever Married", ["Yes", "No"])
    work_type = st.selectbox("Work Type", ["Private", "Self-employed", "Govt_job", "children", "Never_worked"])
    residence_type = st.selectbox("Residence Type", ["Urban", "Rural"])
    avg_glucose_level = st.number_input("Average Glucose Level", min_value=50.0, max_value=300.0, value=100.0)
    bmi = st.number_input("BMI", min_value=10.0, max_value=60.0, value=25.0)
    smoking_status = st.selectbox("Smoking Status", ["never smoked", "formerly smoked", "smokes", "Unknown"])
    stress_level = st.selectbox("Stress Level", ["low", "medium", "high"])

with col2:
    exercise_frequency = st.selectbox("Exercise Frequency", ["none", "1-2x/wk", "3-5x/wk", "daily"])
    alcohol_intake = st.selectbox("Alcohol Intake", ["none", "occasional", "regular"])
    diet_type = st.selectbox("Diet Type", ["healthy", "average", "unhealthy"])
    sleep_quality = st.selectbox("Sleep Quality", ["poor", "average", "good"])
    stroke_family_history = st.selectbox("Stroke Family History", ["No", "Yes"])
    salt_intake = st.selectbox("Salt Intake", ["low", "moderate", "high"])
    systolic_bp = st.number_input("Systolic BP", min_value=90.0, max_value=200.0, value=120.0)
    diastolic_bp = st.number_input("Diastolic BP", min_value=60.0, max_value=130.0, value=80.0)
    ldl_cholesterol = st.number_input("LDL Cholesterol", min_value=50.0, max_value=300.0, value=120.0)
    hdl_cholesterol = st.number_input("HDL Cholesterol", min_value=10.0, max_value=100.0, value=40.0)

# Convert binary to 0/1
hypertension = 1 if hypertension == "Yes" else 0
heart_disease = 1 if heart_disease == "Yes" else 0
stroke_family_history = 1 if stroke_family_history == "Yes" else 0

# Collect the data and save to CSV
if st.button("Save Data"):
    input_data = pd.DataFrame({
        "gender": [gender],
        "age": [age],
        "hypertension": [hypertension],
        "heart_disease": [heart_disease],
        "ever_married": [ever_married],
        "work_type": [work_type],
        "Residence_type": [residence_type],
        "avg_glucose_level": [avg_glucose_level],
        "bmi": [bmi],
        "smoking_status": [smoking_status],
        "stress_level": [stress_level],
        "exercise_frequency": [exercise_frequency],
        "alcohol_intake": [alcohol_intake],
        "diet_type": [diet_type],
        "sleep_quality": [sleep_quality],
        "stroke_family_history": [stroke_family_history],
        "salt_intake": [salt_intake],
        "systolic_bp": [systolic_bp],
        "diastolic_bp": [diastolic_bp],
        "LDL_cholesterol": [ldl_cholesterol],
        "HDL_cholesterol": [hdl_cholesterol]
    })

    # Append data to the CSV file
    import os

    input_data.to_csv(csv_file, mode='a', header=not os.path.exists(csv_file), index=False)
    st.success("✅ Data saved successfully!")

    #st.success("✅ Data saved successfully!")

    if st.button("Show Saved Data"):
        saved_data = pd.read_csv(csv_file)
        st.write("Saved Data:")
        st.write(saved_data.tail())  # Display last few rows

    
