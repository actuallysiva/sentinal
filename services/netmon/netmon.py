import time
import requests
import os
from datetime import datetime

CHECK_INTERVAL = 15

BASE = os.path.expanduser("~/sentinal/logs")
LOG_FILE = os.path.join(BASE, "netmon.log")
STATE_FILE = os.path.join(BASE, "netmon.state")

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

API = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

def log(msg):
    os.makedirs(BASE, exist_ok=True)
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
    except:
        return False

def read_state():
    if os.path.exists(STATE_FILE):
        try:
            with open(STATE_FILE) as f:
                return float(f.read().strip())
        except:
            return None
    return None

def write_state(ts):
    with open(STATE_FILE, "w") as f:
        f.write(str(ts))

def clear_state():
    if os.path.exists(STATE_FILE):
        os.remove(STATE_FILE)

log("netmon started")

while True:
    online = internet_ok()
    down_since = read_state()

    if not online and down_since is None:
        write_state(time.time())
        log("internet down detected (state saved)")

    if online and down_since is not None:
        duration = int(time.time() - down_since)
        mins = duration // 60
        notify(f"🌐 Internet restored after {mins} minutes")
        log(f"internet restored after {mins} minutes")
        clear_state()

    time.sleep(CHECK_INTERVAL)
