import functools


def counter(func):
    """装饰器：记录并打印调用次数"""
    count = 0

    @functools.wraps(func)
    def decorated(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"Count: {count}")
        return func(*args, **kwargs)
    return decorated


@counter
def foo():
    pass


foo()
