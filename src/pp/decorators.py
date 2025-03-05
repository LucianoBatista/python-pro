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


# @printlog
# def foo(x):
#     print(x + 2)
#
#
# @printlog_better
# def baz(x, y):
#     print(x + 2, y)


def running_average(func):
    data = {"total": 0, "count": 0}

    def wrapper(*args, **kwargs):
        val = func(*args, **kwargs)
        data["total"] += val
        data["count"] += 1
        print(
            "Average of {} so far: {:.01f}".format(
                func.__name__, data["total"] / data["count"]
            )
        )
        return val

    return wrapper


@running_average
def foo(x):
    return x + 2


foo(1)
foo(2)
foo(30)


def collectstats(func):
    data = {"total": 0, "count": 0}

    def wrapper(*args, **kwargs):
        val = func(*args, **kwargs)
        data["total"] += val
        data["count"] += 1
        return val

    # the lint is recognizing this as a valid transformation
    wrapper.data = data
    return wrapper


@collectstats
def bar(y):
    return y + 2


bar(1)
# the lint is recognizing this as a valid transformation
print(bar.data)
bar(1)
print(bar.data)
