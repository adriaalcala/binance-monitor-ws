"""Check price processor."""
from typing import Any

from logger import logger


def output(data: dict, **kwargs: Any) -> dict:
    """Output data."""
    logger.log_symbol(data)
    return data
