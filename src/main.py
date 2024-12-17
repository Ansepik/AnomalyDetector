from database import fetch_transactions
from anomaly_model import detect_anomalies
from visualization import plot_anomalies

def main():
    df = fetch_transactions()
    anomalies = detect_anomalies(df)
    print(f"Found anomalies: {len(anomalies)}")
    plot_anomalies(df, anomalies)

if __name__ == "__main__":
    main()
