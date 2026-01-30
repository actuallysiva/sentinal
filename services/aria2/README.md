# aria2 service

This service provides the download engine for sentinal.

Purpose:
- handle file downloads
- support pause/resume
- run independently of control layer

Notes:
- downloads stored in ~/sentinal/downloads
- logs written to ~/sentinal/logs/aria2.log
- controlled later via RPC

## Starting aria2

Environment variable required:

- ARIA2_SECRET

Start manually:

```bash
./start.sh
