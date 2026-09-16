import requests
import os

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

print("Bot Token Found:", TOKEN is not None)
print("Chat ID Found:", CHAT_ID is not None)

requests.post(
    f"https://api.telegram.org/bot{TOKEN}/sendMessage",
    data={
        "chat_id": CHAT_ID,
        "text": "✅ GitHub Action Test Successful"
    }
)

print("Success")
