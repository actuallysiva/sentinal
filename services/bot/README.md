# Telegram control bot

This service provides remote control for sentinal via Telegram.

Initial features:
- /ping
- /status

Design goals:
- reliability on Android
- short-lived network operations
- no background heavy tasks

Secrets required:
- BOT_TOKEN
- CHAT_ID
