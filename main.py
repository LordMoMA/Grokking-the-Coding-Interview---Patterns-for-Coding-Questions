import time
import random
import functools


def timer(wrapped):
    # 将 wrapper 函数的真实签名赋值到 decorated 上
    @functools.wraps(wrapped)
    def decorated(*args, **kwargs):
        st = time.time()
        ret = wrapped(*args, **kwargs)
        print('execution take: {} seconds'.format(time.time() - st))
        return ret
    return decorated


@timer
def random_sleep():
    """随机睡眠一小会"""
    time.sleep(random.random())


print(random_sleep.__name__)
# 输出 'decorated'
print(random_sleep.__doc__)
# 输出 None
