import random


def provide_number(min_num, max_num):
    """装饰器：随机生成一个在 [min_num, max_num] 范围的整数，追加为函数的第一个位置参数
    """
    def wrapper(func):
        def decorated(*args, **kwargs):
            num = random.randint(min_num, max_num)
            # 将 num 作为第一个参数追加后调用函数
            return func(num, *args, **kwargs)
        return decorated
    return wrapper


@provide_number(1, 100)
def print_random_number(num):
    print(num)


# 输出 1-100 的随机整数
# OUTPUT: 72
print_random_number()
