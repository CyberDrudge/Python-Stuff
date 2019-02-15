def my_decorator(func):
    def decorator(*args, **kwargs):
        print("Something is happening before the function is called.")
        func(*args, **kwargs)
        print("Something is happening after the function is called.")
    return decorator


def say_hello():
    print("Konnichiwa!")


# Decorate function
say_hello = my_decorator(say_hello)
# Call function
say_hello()
