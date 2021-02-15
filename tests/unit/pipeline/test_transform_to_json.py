"""Test transform."""
from binance_monitor.pipeline.transform_to_json import transform_to_json


def test_transform_to_json() -> None:
    """Test transform to json."""
    data = transform_to_json(data='{"k": "v"}')
    assert data == {'k': 'v'}
