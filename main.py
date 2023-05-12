import time
import random


def timer(wrapped):
    """装饰器：记录并打印函数耗时"""
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
