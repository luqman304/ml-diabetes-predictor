import streamlit as st
from predictor import predict_diabetes

st.title("🧠 Diabetes Risk Predictor")

pregnancies = st.number_input("Pregnancies", 0, 20, step=1)
glucose = st.number_input("Glucose", 0, 200)
bp = st.number_input("Blood Pressure", 0, 150)
skin_thickness = st.number_input("Skin Thickness", 0, 100)
insulin = st.number_input("Insulin", 0, 900)
bmi = st.number_input("BMI", 0.0, 60.0)
dpf = st.number_input("Diabetes Pedigree Function", 0.0, 2.5)
age = st.number_input("Age", 0, 120, step=1)

if st.button("Predict"):
    result = predict_diabetes([pregnancies, glucose, bp, skin_thickness, insulin, bmi, dpf, age])
    if result == 1:
        st.error("⚠️ You may be at risk for diabetes. Please consult a doctor.")
    else:
        st.success("✅ You are likely not at risk.")