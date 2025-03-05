def printlog(func):
    def wrapper(arg):
        print("Calling: " + func.__name__)
        return func(arg)

    return wrapper


# a better version
def printlog_better(func):
    # the place where we will use this decorator
    # can have any number of params
    def wrapper(*args, **kwargs):
        print("Calling: " + func.__name__)
        return func(*args, **kwargs)

    return wrapper


@printlog
def foo(x):
    print(x + 2)


@printlog_better
def baz(x, y):
    print(x + 2, y)


foo(2)
baz(2, 6)
