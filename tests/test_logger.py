"""Test suite for logger."""
import json
from os import path
from shutil import rmtree
from tempfile import TemporaryDirectory
from unittest.mock import patch
from uuid import uuid4

from logger import Logger


def test_logger_log_symbol() -> None:
    """Test log connected hostnamees."""
    with TemporaryDirectory() as tmpdir:
        with patch("logger.LOGS_DIR", tmpdir):
            logger = Logger()
        logger.log_symbol(
            {
                "e": "e", "E": "E", "s": "s", "a": "a", "p": "p", "q": "q",
                "f": "f", "l": "l", "T": "T", "m": "m", "M": "M"
            }
        )
        expected_json = {
            "Event type": "e", "Event time": "E", "Symbol": "s", "Aggregate trade ID": "a", "Price": "p",
            "Quantity": "q", "First trade ID": "f", "Last trade ID": "l", "Trade time": "T",
            "Is the buyer the market maker?": "m"
        }
        expected_lines = [json.dumps(expected_json) + '\n']
        with open(f"{tmpdir}/info_logs.log") as f:
            assert expected_lines == f.readlines()


def test_create_dir_if_not_exists() -> None:
    """Check that logger creates dir if not exists."""
    mock_logs_dir = str(uuid4())
    assert not path.isdir(mock_logs_dir)
    with patch("logger.LOGS_DIR", mock_logs_dir):
        Logger()
    assert path.isdir(mock_logs_dir)
    rmtree(mock_logs_dir)
