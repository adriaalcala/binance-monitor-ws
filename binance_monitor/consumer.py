"""Binance consumer module."""
from datetime import datetime, timedelta
import json
from random import randint
import ssl
from time import sleep

from websocket import create_connection  # type:ignore

from binance_monitor.pipeline.main import process_data
from config import BASE_URI, PONG_PERIOD, SECONDS_TO_RENEW_CONNECTION, SLEEP_TIME
from logger import logger


def monitor_symbol(symbol: str, min_price: float) -> None:
    """Create a websocket connection to binance and monitor `symbol`.

    Args:
        symbol: The symbol to be monitored.
        min_price: The min price to be monitored.
    """
    ws = create_connection(BASE_URI, sslopt={"cert_reqs": ssl.CERT_NONE})
    connection_id = randint(1, 10**6)
    data = {'method': 'SUBSCRIBE', 'params': [f'{symbol}@aggTrade'], 'id': connection_id}
    ws.send(json.dumps(data))
    logger.debug(f'Connected to channel {symbol}@aggTrade')
    start = datetime.now()
    next_pong = start + timedelta(seconds=PONG_PERIOD)
    refresh_connection = start + timedelta(seconds=SECONDS_TO_RENEW_CONNECTION)
    while True:
        if datetime.now() > refresh_connection:
            data = {'method': 'UNSUBSCRIBE', 'params': [f'{symbol}@aggTrade'], 'id': connection_id}
            ws.send(json.dumps(data))
            ws = create_connection(BASE_URI, sslopt={"cert_reqs": ssl.CERT_NONE})
            data = {'method': 'SUBSCRIBE', 'params': [f'{symbol}@aggTrade'], 'id': connection_id}
            ws.send(json.dumps(data))
            logger.debug('Connection refreshed')
            refresh_connection = datetime.now() + timedelta(seconds=SECONDS_TO_RENEW_CONNECTION)
        if datetime.now() > next_pong:
            ws.send_frame('pong')
            logger.debug('Pong frame send')
            next_pong = datetime.now() + timedelta(seconds=PONG_PERIOD)
        result = ws.recv()
        process_data(symbol, min_price, result)
        sleep(SLEEP_TIME)
