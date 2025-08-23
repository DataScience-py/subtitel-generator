"""Utils."""

import time
from typing import Any, Callable

from .logger import get_logger

local_logger = get_logger(__name__)


def timer(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    Timer decorator that prints the execution time of the decorated function.

    Parameters
    ----------
    func : Callable[..., Any]
        function to be decorated

    Returns
    -------
    Callable[..., Any]
        decorated function
    """

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        local_logger.debug(
            f"Function {func.__name__} took {end_time - start_time} seconds to\
             execute."
        )
        return result

    return wrapper
