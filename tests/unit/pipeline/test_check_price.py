"""Test check_price."""
from pytest import raises

from binance_monitor.exceptions import StopProcessing
from binance_monitor.pipeline.check_price import check_price


def test_check_price_ok() -> None:
    """Test check_price with price above min_price."""
    data = check_price(min_price=1, data={'p': 2.0})
    assert data == {'p': 2.0}


def test_check_price_exception() -> None:
    """Test check_price with price not above min_price."""
    with raises(StopProcessing):
        check_price(min_price=4, data={'p': 2.0})
