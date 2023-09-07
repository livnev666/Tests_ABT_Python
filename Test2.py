from functools import wraps


# Test 2
def cls_method_decorator(param):
    def inner_dec(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if param:
                result = func(*args, **kwargs)
                return param + result
        return wrapper
    return inner_dec


class SomeClass:
    some_var: int

    def __init__(self, some_var: int):
        self.some_var = some_var

    def increment_var(self, increment: int):
        self.some_var += increment

    @cls_method_decorator(30)
    def some_func(self, condition=None):
        return self.some_var

    def print_var(self):
        print(self.some_var)


sml = SomeClass(10)
sml.increment_var(10)
print(sml.some_func())