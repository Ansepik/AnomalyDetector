import pandas as pd
import sqlite3

def fetch_transactions():
    conn = sqlite3.connect(":memory:")
    df = pd.read_csv("data/transactions.csv")
    df.to_sql("transactions", conn, index=False, if_exists="replace")
    
    query = "SELECT * FROM transactions"
    transactions = pd.read_sql(query, conn)
    conn.close()
    return transactions

if __name__ == "__main__":
    df = fetch_transactions()
    print(df.head())
