"""Check price processor."""
from typing import Any

from binance_monitor.exceptions import StopProcessing


def check_price(min_price: float, data: dict, **kwargs: Any) -> dict:
    """Check if price is above min_price."""
    price = float(data.get('p', 0))
    if price <= min_price:
        raise StopProcessing()
    return data
