import matplotlib.pyplot as plt
import seaborn as sns

def plot_anomalies(df, anomalies):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x="transaction_id", y="amount", label="Normal")
    sns.scatterplot(data=anomalies, x="transaction_id", y="amount", color="red", label="Anomalies")
    plt.legend()
    plt.savefig("report/anomalies.png")
    plt.show()
