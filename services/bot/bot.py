import time
import requests
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

API = f"https://api.telegram.org/bot{BOT_TOKEN}"

def send(msg):
    requests.post(
        f"{API}/sendMessage",
        data={"chat_id": CHAT_ID, "text": msg},
        timeout=10
    )

offset = 0
send("🤖 sentinal bot online")

while True:
    try:
        r = requests.get(
            f"{API}/getUpdates",
            params={"offset": offset, "timeout": 30},
            timeout=35
        ).json()

        for u in r.get("result", []):
            offset = u["update_id"] + 1
            msg = u["message"]["text"].strip()

            if msg == "/ping":
                send("✅ alive")

            elif msg == "/status":
                send("🟢 sentinal running")

            else:
                send("❓ unknown command")

    except:
        time.sleep(5)
