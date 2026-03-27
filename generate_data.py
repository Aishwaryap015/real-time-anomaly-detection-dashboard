import random
import time
import csv

def generate_data():
    with open("data.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["timestamp", "value"])

        while True:
    try:
        df = detect_anomalies()

        if "anomaly" in df.columns:
            anomalies = df[df["anomaly"] == -1]

            drift_detected, p_value = detect_drift()

            with placeholder.container():

                col1, col2 = st.columns(2)
                col1.metric("Total Data Points", len(df))
                col2.metric("Anomalies Detected", len(anomalies))

                if not anomalies.empty:
                    st.error(f"🚨 {len(anomalies)} anomalies detected!")

                if drift_detected:
                    st.warning(f"⚠️ Data Drift Detected!")

                st.line_chart(df["value"])

                st.subheader("Detected Anomalies")
                st.write(anomalies)

        time.sleep(2)   # ✅ aligned with try

    except Exception as e:
        st.write("Waiting for data...")
        time.sleep(2)

if __name__ == "__main__":
    generate_data()