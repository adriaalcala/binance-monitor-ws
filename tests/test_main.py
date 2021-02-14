"""Test suite for main."""
import json
from unittest.mock import Mock, patch

from pytest import raises

from config import SLEEP_TIME
from main import monitor_symbol


class SleepException(Exception):
    """Exception used to stop unlimited parser."""
    pass


@patch("main.create_connection")
@patch("main.logger")
@patch("main.sleep")
def test_main(mock_sleep: Mock, mock_logger: Mock, mock_create_connection: Mock) -> None:
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
    mock_logger.log_symbol.assert_called_once_with(response)
