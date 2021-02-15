"""Test output."""
from unittest.mock import Mock, patch

from binance_monitor.pipeline.output import output


@patch('binance_monitor.pipeline.output.logger')
def test_output(mock_logger: Mock) -> None:
    """Test output."""
    data = output({'k': 'v'})
    assert data == {'k': 'v'}
    mock_logger.log_symbol.assert_called_once_with({'k': 'v'})
