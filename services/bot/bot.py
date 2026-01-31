import time
import requests
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
ARIA2_SECRET = os.getenv("ARIA2_SECRET")

API = f"https://api.telegram.org/bot{BOT_TOKEN}"
ARIA2_RPC = "http://localhost:6800/jsonrpc"

def send(msg):
    requests.post(
        f"{API}/sendMessage",
        data={"chat_id": CHAT_ID, "text": msg},
        timeout=10
    )

def aria2_call(method, params=None):
    if params is None:
        params = []

    payload = {
        "jsonrpc": "2.0",
        "id": "sentinal",
        "method": method,
        "params": [f"token:{ARIA2_SECRET}"] + params
    }

    r = requests.post(ARIA2_RPC, json=payload, timeout=10)
    return r.json()

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
            text = u["message"]["text"].strip()

            if text.startswith("/add "):
                url = text.split(" ", 1)[1]
                res = aria2_call("aria2.addUri", [[url]])
                gid = res.get("result")
                send(f"✅ Download added\nGID: {gid}")

            elif text == "/ping":
                send("✅ alive")

            elif text == "/status":
                send("🟢 sentinal running")

            else:
                send("❓ unknown command")

    except Exception as e:
        time.sleep(5)
