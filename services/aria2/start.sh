#!/data/data/com.termux/files/usr/bin/sh

# aria2 start script for sentinal

aria2c \
  --conf-path="$HOME/sentinal/services/aria2/aria2.conf" \
  --rpc-secret="$ARIA2_SECRET"
