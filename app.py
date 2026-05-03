import streamlit as st
import numpy as np
import pickle

# IMPORTANT imports
from sklearn.ensemble import RandomForestClassifier

# load model
model = pickle.load(open("attrition_model.pkl", "rb"))

st.title("Employee Attrition Prediction")

# INPUTS
age = st.number_input("Age", 18, 60)
salary = st.number_input("Salary")

job_role = st.selectbox("Job Role", ["Manager", "Engineer", "HR"])
overtime = st.selectbox("Overtime", ["Yes", "No"])
work_life = st.selectbox("Work-Life Balance (1-4)", [1,2,3,4])

# ENCODING (must match training)
overtime = 1 if overtime == "Yes" else 0

# Example input (update based on your dataset columns)
input_data = np.array([[age, salary, overtime, work_life]])

if st.button("Predict"):
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("⚠️ Employee likely to leave")
    else:
        st.success("✅ Employee likely to stay")