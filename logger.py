
"""Logger class.
~~~~~~~~~~~~~~~~~~
"""
import json
from logging import DEBUG, Formatter, getLogger, INFO, StreamHandler
from logging.handlers import RotatingFileHandler
from os import mkdir, path

from config import BACKUP_COUNT, IGNORE_KEYS, LOGS_DIR, MATCH_KEYS, MAX_BYTES


class Logger():
    """Class used to make easier report the function's output."""
    def __init__(self) -> None:
        """Creates a logger instance.
        This logger uses a RotationFileHandler with a limit of max_bytes.
        """
        if not path.isdir(LOGS_DIR):
            mkdir(LOGS_DIR)
        log_console_format = "%(message)s"
        log_file_format = "[%(levelname)s] - %(asctime)s - %(name)s - : %(message)s in %(pathname)s:%(lineno)d"

        logger = getLogger('log_parser')
        logger.setLevel(INFO)

        console_handler = StreamHandler()
        console_handler.setLevel(INFO)
        console_handler.setFormatter(Formatter(log_console_format))

        file_handler = RotatingFileHandler(f"{LOGS_DIR}/debug_logs.log", maxBytes=MAX_BYTES, backupCount=BACKUP_COUNT)
        file_handler.setLevel(DEBUG)
        file_handler.setFormatter(Formatter(log_file_format))

        file_handler_info = RotatingFileHandler(f"{LOGS_DIR}/info_logs.log", maxBytes=MAX_BYTES, backupCount=BACKUP_COUNT)
        file_handler_info.setLevel(INFO)
        file_handler_info.setFormatter(Formatter(log_console_format))

        logger.addHandler(console_handler)
        logger.addHandler(file_handler)
        logger.addHandler(file_handler_info)
        self.logger = logger

    def info(self, message: str) -> None:
        """Logs info message."""
        self.logger.info(message)

    def debug(self, message: str) -> None:
        """Logs info message."""
        self.logger.debug(message)

    def log_symbol(self, result: dict) -> None:
        """Logs connected hostnames."""
        self.info(json.dumps({MATCH_KEYS[k]: v for k, v in result.items() if k not in IGNORE_KEYS}))


logger = Logger()
