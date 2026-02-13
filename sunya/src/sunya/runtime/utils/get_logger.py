import logging
import os

logger = None


def get_logger():
    global logger
    if logger is None:
        log_level = os.getenv("LOG_LEVEL", "WARNING")
        logging.basicConfig(level=logging.getLevelName(log_level))
        logger = logging.getLogger(__name__)
    return logger
