import pandas as pd
from scipy.stats import ks_2samp

def detect_drift():
    df = pd.read_csv("data.csv")

    if len(df) < 50:
        return False, 0.0

    # Split data into old vs new
    old_data = df["value"][:len(df)//2]
    new_data = df["value"][len(df)//2:]

    # Kolmogorov-Smirnov Test
    stat, p_value = ks_2samp(old_data, new_data)

    drift_detected = p_value < 0.05

    return drift_detected, p_value