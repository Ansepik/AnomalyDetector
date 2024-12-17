import pandas as pd
import random
import numpy as np

def generate_transaction_data():
    data = []
    user_ids = [123, 124, 125, 126]
    transaction_types = ["debit", "credit"]

    for i in range(1, 1001):  # 1000 transaction
        user_id = random.choice(user_ids)
        amount = round(np.random.normal(100, 50), 2)
        transaction_type = random.choice(transaction_types)
        timestamp = pd.Timestamp.now() - pd.Timedelta(minutes=random.randint(0, 10000))
        
        if random.random() < 0.01:  # 1% anomaly
            amount = round(amount * random.randint(10, 50), 2)

        data.append([i, user_id, amount, transaction_type, timestamp])
    
    df = pd.DataFrame(data, columns=["transaction_id", "user_id", "amount", "transaction_type", "timestamp"])
    df.to_csv("data/transactions.csv", index=False)

if __name__ == "__main__":
    generate_transaction_data()
    print("File transactions.csv is ready")
