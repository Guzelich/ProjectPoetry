import functools
from typing import Any
from time import time


def log(filename: str = "myfile_log.txt") -> Any:
    def decorator(func) -> Any:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                start_time = time()
                result = func(*args, **kwargs)
                end_time = time()
                duration = end_time - start_time
                msg = f"{func.__name__} ok, result: {result}, time: {duration:.6f}, sec\n"
                _output(msg, filename)
                return result
            except Exception as e:
                msg = f"{func.__name__} error: {type(e).__name__}: {e} (args={args}, kwargs={kwargs})\n"
                _output(msg, filename)
                raise

        return wrapper

    return decorator


def _output(msg: Any, filename: Any) -> None:
    if filename is not None:
        with open(filename, "a") as f:
            f.write(msg)
    else:
        print(msg, end="")
