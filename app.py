import streamlit as st
import pandas as pd
import numpy as np
import pickle
from utils.preprocess import extract_features
from services.analyzer import analyze_behavior
from services.scorer import risk_score, adjust_premium

st.set_page_config(page_title="Telematics Insurance", layout="centered")

st.title("Telematics-Based Usage Insurance System")
st.markdown("Enter your driving data to get risk analysis and premium adjustment.")

# Input form
with st.form("telematics_form"):
    speed = st.number_input("Vehicle Speed (km/h)", min_value=0.0)
    rpm = st.number_input("Engine RPM", min_value=0.0)
    throttle = st.number_input("Throttle Position (%)", min_value=0.0, max_value=100.0)
    ax = st.number_input("Acceleration X (m/s²)", format="%.2f")
    ay = st.number_input("Acceleration Y (m/s²)", format="%.2f")
    az = st.number_input("Acceleration Z (m/s²)", format="%.2f")
    submitted = st.form_submit_button("Analyze Risk")

if submitted:
    try:
        data = {
            "Vehicle speed": speed,
            "ENGINE RPM": rpm,
            "THROTTLE POSITION": throttle,
            "ACCELERATION X": ax,
            "ACCELERATION Y": ay,
            "ACCELERATION Z": az
        }

        features = extract_features(data)
        prediction = analyze_behavior(features)
        score = risk_score(prediction)
        premium = adjust_premium(base_premium=5000, risk_factor=score)

        st.success("✅ Analysis Complete!")
        st.markdown(f"**Risk Level:** `{prediction}`")
        st.markdown(f"**Risk Score:** `{score}`")
        st.markdown(f"**Adjusted Premium:** `₹{premium:.2f}`")

    except Exception as e:
        st.error(f"An error occurred: {e}")
