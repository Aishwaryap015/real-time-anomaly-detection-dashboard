import pandas as pd

def detect_drift():
    df = pd.read_csv("data.csv")

    if len(df) < 50:
        return False, 0.0

    old_mean = df["value"][:len(df)//2].mean()
    new_mean = df["value"][len(df)//2:].mean()

    drift = abs(new_mean - old_mean)

    drift_detected = drift > 20  # threshold

    return drift_detected, drift