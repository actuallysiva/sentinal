import time
import requests
import os
from datetime import datetime

CHECK_INTERVAL = 10
LOG_FILE = os.path.expanduser("~/sentinal/logs/netmon.log")

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

API = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

def log(msg):
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.now()} - {msg}\n")

def notify(msg):
    try:
        requests.post(API, data={"chat_id": CHAT_ID, "text": msg}, timeout=10)
        log(f"telegram sent: {msg}")
    except Exception as e:
        log(f"telegram error: {e}")

def internet_ok():
    try:
        requests.get("https://api.telegram.org", timeout=5)
        return True
    except Exception as e:
        log(f"internet check failed: {e}")
        return False

down_since = None

log("netmon started")

while True:
    online = internet_ok()
    log(f"internet status: {online}")

    if not online and down_since is None:
        down_since = time.time()
        log("internet DOWN detected")

    if online and down_since is not None:
        duration = int(time.time() - down_since)
        mins = duration // 60
        notify(f"🌐 Internet restored after {mins} minutes")
        log("internet RESTORED event sent")
        down_since = None

    time.sleep(CHECK_INTERVAL)

