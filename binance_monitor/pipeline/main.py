"""Pipeline module."""
from binance_monitor.exceptions import StopProcessing
from binance_monitor.pipeline.check_price import check_price
from binance_monitor.pipeline.output import output
from binance_monitor.pipeline.transform_to_json import transform_to_json
from logger import logger

PROCESSORS = [
    ('transform_to_json', transform_to_json),
    ('check_price', check_price),
    ('output', output),
]


def process_data(symbol: str, min_price: float, data: str) -> None:
    """Launch pipeline."""
    actual_processor = None
    try:
        for processor, fun in PROCESSORS:
            actual_processor = processor
            data = fun(symbol=symbol, min_price=min_price, data=data)  # type:ignore
    except StopProcessing:
        logger.debug(f'Pipeline finished with StopProcessing in {actual_processor}')

    logger.debug('Pipeline done all steps')
