import functools


def log(filename="myfile_log.txt"):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                msg = f'{func.__name__} ok, result: {result}\n'
                _output(msg, filename)
                return result
            except Exception as e:
                msg = f'{func.__name__} error: {type(e).__name__}: {e} (args={args}, kwargs={kwargs})\n'
                _output(msg, filename)
                raise
        return wrapper
    return decorator


def _output(msg, filename):
    if filename:
        with open(filename, 'a') as f:
            f.write(msg)
    else:
        print(msg, end='')
