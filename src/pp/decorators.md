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

Valuable decorator pattern rely on using variables inside the decorator function itself. This is not the same as using variables inside the wrapper function.

It is very important to consider the scope where the variable is defined. Usally if you want to have a shared variable between function or methods calling, you'll need to set you variable right before the `wrapper` function definition.

# Accessing Inner Data

What if you want to peek into data? The variable inside the decorator.

Simply assign `data` as an attribue to the wrapper object.

```python
def collectstats(func):
    data = {"total": 0, "count": 0}
    def wrapper(*args, **kwargs):
        val = func(*args, **kwargs)
        data["val"] += val
        data["count"] += 1
        return val
    wrapper.data = data
    return wrapper
```

We can do this because in python a function is just an object, and in python, you can add new attributes to objects by just assigning them.

# Nonlocal decorator state

We have not just the `glogal` keyword, but also the `nonlocal`.

The pattern showed before works because we do not change the same object whe inside the `wrapper` function, but the following listing is a bug

```python
def avg_with_a_bug(func):
    count = 0
    def wrapper(*args, **kwargs):
        global count
        count += 1
        return func(*args, **kwargs)
    return wrapper
```

This works but the count variable is now used for every function that uses this decorator.


```python
def avg_with_a_bug(func):
    count = 0
    def wrapper(*args, **kwargs):
        count += 1
        return func(*args, **kwargs)
    return wrapper
```

This now has a bug, becouse count is changing the integer related to the value. So in this case we need the `nonlocal` keyword.

> [!Important]
> `nonlocal` will search for the **nearest enclosing scope** that defines a variable named count, and use it like it's a global.

The line `count += 1` is actually modifying the value of the `count` variable itself, because it really means `count = count + 1`. **And whenever you modify (instead of just read) a variable that was created in a larger scope**, python requires you to declare thats what you actually want, with `global or nonlocal`.

É como se eu tivesse tentando alterar o valor de uma variável sem ela ser `mutable`. E para o python considerar ela mutable, a gente precisa indicar com `global or nonlocal`.

# Decorators that take arguments

If you want to pass a value to a decorator you need to obey the following pattern:

```python
def add(n) -> DecoratedCallable:
    def decorator(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs) + n
        return wrapper
    return decorator

```

Look that add is not a decorator, this is a function that returns a decorator.

> [!Cite]
> Suppose the python interpreter is parsing your program and encounters the following code:
> - `@add(2) ...`
> 
> Python takes everything between **the @ symbol and the end-of-line character as a single Python expression** - add(2) in this case. That expression is evaluated. This all happens **at compile time**.


> [!Note]
> Difference between "compile time" and "executing at runtime":
> - compile time is when python translates source code into bytecode, before the program actually runs. Decorators are processed during this compilation phase.
> - runtime is when your code is actually executing and your functions are being called.

