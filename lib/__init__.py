from functools import wraps
from timeit import default_timer


def timed_run(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = default_timer()
        result = func(*args, **kwargs)
        print(f'{func.__name__}: {default_timer() - start}')
        return result

    return wrapper
