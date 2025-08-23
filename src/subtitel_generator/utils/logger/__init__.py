"""Init method when return logger instance."""

import logging


def get_logger(name: str, level: int = logging.DEBUG) -> logging.Logger:
    """
    get_logger initialize logger with name.

    Parameters
    ----------
    name : str
        Name of logger

    Returns
    -------
    Logger
        Logger instance
    """
    logger = logging.getLogger(name)

    logger.setLevel(level=level)

    stream_handler = logging.StreamHandler()

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    stream_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)

    return logger


__all__ = ["get_logger"]
