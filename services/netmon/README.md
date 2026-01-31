# netmon service

Monitors internet connectivity and sends a Telegram message
when internet connectivity is restored.

Why restore-only alerts:
- no connectivity during outage
- guarantees delivery
- avoids alert spam

Logs:
- ~/sentinal/logs/netmon.log

Environment variables required:
- BOT_TOKEN
- CHAT_ID
