def strict(func):
    def wrapper(*args):
        annotations = func.__annotations__
        for arg, expected_type in zip(args, annotations.values()):
            if not isinstance(arg, expected_type):
                raise TypeError(f"Expected {expected_type}, got {type(arg)}")
        return func(*args)
    return wrapper

@strict
def sum_two(a: int, b: int) -> int:
    return a + b