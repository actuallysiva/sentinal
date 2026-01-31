import time
import requests
import os
from datetime import datetime

CHECK_INTERVAL = 15
LOG_FILE = os.path.expanduser("~/sentinal/logs/netmon.log")

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

API = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

def log(msg):
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.now()} - {msg}\n")

def internet_ok():
    try:
        requests.get("https://1.1.1.1", timeout=5)
        return True
    except:
        return False

def notify(msg):
    try:
        requests.post(API, data={"chat_id": CHAT_ID, "text": msg}, timeout=10)
    except:
        pass

down_since = None

log("netmon started")

while True:
    online = internet_ok()

    if not online and down_since is None:
        down_since = time.time()
        log("internet down detected")

    if online and down_since is not None:
        duration = int(time.time() - down_since)
        mins = duration // 60
        notify(f"🌐 Internet restored after {mins} minutes")
        log(f"internet restored after {mins} minutes")
        down_since = None

    time.sleep(CHECK_INTERVAL)
