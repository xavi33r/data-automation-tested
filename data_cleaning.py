import pandas as pd

df = pd.read_csv('crypto_weekly_btc_eth.csv')

df['btc_eth_ratio'] = df['btc_price_usd'] / df['eth_price_usd']

summary = df.describe()

print(df)
print(summary)
