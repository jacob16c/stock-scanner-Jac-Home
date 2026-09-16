import yfinance as yf
import pandas as pd
import requests
import os
 
TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
 
WATCHLIST = [
"AAPL",
"MSFT",
"NVDA",
"AMD",
"AMZN",
"PLTR",
"TSLA"
]
 
def calculate_rsi(data, period=14):
delta = data.diff()
 
gain = delta.where(delta > 0, 0)
loss = -delta.where(delta < 0, 0)
 
avg_gain = gain.rolling(period).mean()
avg_loss = loss.rolling(period).mean()
 
rs = avg_gain / avg_loss
 
return 100 - (100 / (1 + rs))
 
results = []
 
for ticker in WATCHLIST:
 
try:
df = yf.download(
ticker,
period="6mo",
progress=False
)
 
close = df["Close"]
 
current = close.iloc[-1]
rsi = calculate_rsi(close).iloc[-1]
 
ma50 = close.rolling(50).mean().iloc[-1]
 
if rsi < 40 and current > ma50:
 
results.append(
f"{ticker}\n"
f"Price: ${current:.2f}\n"
f"RSI: {rsi:.1f}\n"
)
 
except:
pass
 
message = "Daily Stock Scanner\n\n"
 
if len(results) == 0:
message += "No stocks matched today."
else:
message += "\n".join(results)
 
requests.post(
f"https://api.telegram.org/bot{TOKEN}/sendMessage",
data={
"chat_id": CHAT_ID,
"text": message
}
)
