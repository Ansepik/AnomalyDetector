from sklearn.ensemble import IsolationForest
import pandas as pd

def detect_anomalies(df):
    model = IsolationForest(contamination=0.01, random_state=42)
    df["is_anomaly"] = model.fit_predict(df[["amount"]])
    anomalies = df[df["is_anomaly"] == -1]
    return anomalies
