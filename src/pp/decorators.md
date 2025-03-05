# Intro

- A decorator works by *adding behavior around a function*. Meaning, lines of code which are executed before that function begins, after it returns, or both.
- It does not alter any lines of code inside the function.

# The basic decorator

- This is what happen whe we run a function with a decorator in python

```python
# what you code ....
@some_decorator
def some_function(arg):
    ...

# what happens .....
some_function = some_decorator(some_function)
```

- A docorator is just a function that returns another function
- Decorators for functions and decorators for methods

For functions:
```python
def printlog_better(func):
    def wrapper(*args, **kwargs):
        print("Calling: " + func.__name__)
        return func(*args, **kwargs)

    return wrapper

```

For methods
```python
def printlog_better(func):
    def wrapper(self, *args, **kwargs):
        print("Calling: " + func.__name__)
        return func(self, *args, **kwargs)

    return wrapper

```

- Just pass the `self` arg when you have a clear use for the `self`. Otherwise just use `*args and **kwargs`, and the self will be passed anyway

# Data in Decorators


