from model import detect_anomalies
import streamlit as st
import time
import matplotlib.pyplot as plt
from model import detect_anomalies
from drift import detect_drift

st.set_page_config(page_title="Anomaly Detection", layout="wide")

st.title("🚨 Real-Time Anomaly Detection System")
st.markdown("### Live Monitoring + ML + Drift Detection")

placeholder = st.empty()

while True:
    try:
        df = detect_anomalies()

        if "anomaly" in df.columns:
            anomalies = df[df["anomaly"] == -1]

            drift_detected, p_value = detect_drift()

            with placeholder.container():

                # 🔥 METRICS
                col1, col2 = st.columns(2)
                col1.metric("Total Data Points", len(df))
                col2.metric("Anomalies", len(anomalies))

                # 🚨 ALERTS
                if not anomalies.empty:
                    st.error(f"🚨 {len(anomalies)} anomalies detected!")

                if drift_detected:
                    st.warning(f"⚠️ Data Drift Detected (p={p_value:.5f})")

                # 📈 GRAPH
                st.subheader("📈 Live Data")

                fig, ax = plt.subplots()
                ax.plot(df["value"], label="Normal Data")

                ax.scatter(anomalies.index,
                           anomalies["value"],
                           color="red",
                           label="Anomaly")

                ax.legend()
                st.pyplot(fig)

                # 📋 TABLE
                st.subheader("📋 Detected Anomalies")
                st.dataframe(anomalies)

        time.sleep(2)

    except Exception as e:
        st.write("Waiting for data...")
        time.sleep(2)