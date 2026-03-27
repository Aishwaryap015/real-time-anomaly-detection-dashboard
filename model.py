import pandas as pd
from sklearn.ensemble import IsolationForest

def detect_anomalies():
    df = pd.read_csv("data.csv")

    if len(df) < 10:
        return df

    model = IsolationForest(contamination=0.05)
    df["anomaly"] = model.fit_predict(df[["value"]])

    return df