from functools import wraps


def decorator(func):
    @wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do something before
        value = func(*args, **kwargs)
        # Do something after
        return value
    return wrapper_decorator


@decorator
def say_hello():
    """Say Hello"""
    print("Konnichiwa!")


say_hello()
