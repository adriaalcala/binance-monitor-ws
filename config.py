import os

LOGS_DIR = os.getenv('LOGS_DIR', 'logs')
MAX_BYTES = int(os.getenv('MAX_BYTES', 10**6))
BACKUP_COUNT = int(os.getenv('BACKUP_COUNT', 5))

BASE_URI = 'wss://stream.binance.com:9443/ws'
MATCH_KEYS = {
    "e":"Event type",
    "E": "Event time",
    "s": "Symbol",
    "a": "Aggregate trade ID",
    "p": "Price",
    "q": "Quantity",
    "f": "First trade ID",
    "l": "Last trade ID",
    "T": "Trade time",
    "m": "Is the buyer the market maker?",
    "M": "Ignore",
}
IGNORE_KEYS = ["M",]
# MAX ALLOWED ARE 5 per second
SLEEP_TIME = 0.3
# MAX ALLOWED ARE 24 hours
SECONDS_TO_RENEW_CONNECTION = 60 * 60 * 20
# PING every 3 minutes, max waiting 10 minutes
PONG_PERIOD = 60 * 5
