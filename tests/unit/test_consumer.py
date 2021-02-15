"""Test suite for main."""
import json
from unittest.mock import Mock, patch

from pytest import raises

from binance_monitor.consumer import monitor_symbol
from config import SLEEP_TIME


class SleepException(Exception):
    """Exception used to stop unlimited parser."""
    pass


@patch("binance_monitor.consumer.create_connection")
@patch("binance_monitor.consumer.process_data")
@patch("binance_monitor.consumer.sleep")
def test_main(mock_sleep: Mock, mock_pipeline: Mock, mock_create_connection: Mock) -> None:
    """Test main."""
    def _sleep_side_effect(time: int) -> None:
        raise SleepException

    mock_ws = Mock()
    mock_create_connection.return_value = mock_ws
    mock_sleep.side_effect = _sleep_side_effect
    response = {
        "e": "aggTrade", "E": "time", "s": "BTCUSDT", "a": "agg_id", "p": "4", "q": "0.02",
        "f": "trade_id", "l": "trade_id", "T": "time", "m": False, "M": True
    }
    mock_ws.recv = Mock(return_value=json.dumps(response))
    with raises(SleepException):
        monitor_symbol("BTCUSDT", 2)
    mock_sleep.assert_called_with(SLEEP_TIME)
    mock_pipeline.assert_called_once_with("BTCUSDT", 2, json.dumps(response))
