import time
import functools


class DelayFunc:
    def __init__(self,  duration, func):
        self.duration = duration
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f'Wait for {self.duration} seconds...')
        time.sleep(self.duration)
        return self.func(*args, **kwargs)

    def eager_call(self, *args, **kwargs):
        print('Call without delay')
        return self.func(*args, **kwargs)


def delay(duration):
    """装饰器：推迟某个函数的执行。同时提供 .eager_call 方法立即执行
    """
    # 此处为了避免定义额外函数，直接使用 functools.partial 帮助构造
    # DelayFunc 实例
    return functools.partial(DelayFunc, duration)
