import pandas as pd, random
from datetime import datetime, timedelta

num_trades = 1000
symbols = ["APPLE", "NIFT", "GOOGLE", "AMZN", "TESLA", "TCS", "DELL"]
traders = ["T001", "T002", "T003", "T004", "T005"]

data = [{
 "trade_id": f"TR{i+1:05d}",
 "trader_id": random.choice(traders),
 "symbol": random.choice(symbols),
 "quantity": random.randint(1, 100),
 "price": round(random.uniform(100, 1000), 2),
 "side": random.choice(["BUY", "SELL"]),
 "trade_date": (datetime.now() - timedelta(days=random.randint(0,1))).strftime("%Y-%m-%d")
} for i in range(num_trades)]

df = pd.DataFrame(data)
df.to_csv("trades.csv", index=False)
print("File created")
