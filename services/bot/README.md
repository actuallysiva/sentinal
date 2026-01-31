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


## Running the bot

Required environment variables:
- BOT_TOKEN
- CHAT_ID

Start manually:

```bash
./start.sh
