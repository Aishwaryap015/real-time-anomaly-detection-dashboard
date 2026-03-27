import streamlit as st
import pandas as pd
import time
import matplotlib.pyplot as plt
from model import detect_anomalies
from drift import detect_drift
from generate_data import generate_once

st.set_page_config(page_title="Anomaly Detection", layout="wide")

st.title("🚨 Real-Time Anomaly Detection System")
st.markdown("### Monitoring live system behavior and detecting anomalies using Machine Learning")

# Run continuously using Streamlit rerun
for _ in range(1000):  # acts like loop safely

    generate_once()  # generate live data

    df = detect_anomalies()

    if "anomaly" in df.columns:
        anomalies = df[df["anomaly"] == -1]

        drift_detected, p_value = detect_drift()

        col1, col2 = st.columns(2)
        col1.metric("Total Data Points", len(df))
        col2.metric("Anomalies Detected", len(anomalies))

        if not anomalies.empty:
            st.error(f"🚨 {len(anomalies)} anomalies detected!")

        if drift_detected:
            st.warning(f"⚠️ Data Drift Detected! (p-value: {p_value:.5f})")

        st.subheader("📈 Live Data with Anomalies")

        st.subheader("📈 Live Data with Anomalies")

chart_data = df.copy()
chart_data["anomaly"] = df["value"]
chart_data.loc[df["anomaly"] != -1, "anomaly"] = None

st.line_chart(chart_data[["value", "anomaly"]])

st.subheader("🚨 Detected Anomalies")
st.dataframe(anomalies)

    time.sleep(1)
    st.experimental_rerun()