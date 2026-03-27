import pandas as pd

def detect_anomalies():
    df = pd.read_csv("data.csv")

    if len(df) < 10:
        return df

    mean = df["value"].mean()
    std = df["value"].std()

    # Z-score method
    df["anomaly"] = df["value"].apply(
        lambda x: -1 if abs(x - mean) > 2 * std else 1
    )

    return df