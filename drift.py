import pandas as pd
from scipy.stats import ks_2samp

def detect_drift():
    df = pd.read_csv("data.csv")

    if len(df) < 50:
        return False, 1.0

    old = df["value"][:len(df)//2]
    new = df["value"][len(df)//2:]

    stat, p_value = ks_2samp(old, new)

    drift = p_value < 0.05

    return drift, p_value