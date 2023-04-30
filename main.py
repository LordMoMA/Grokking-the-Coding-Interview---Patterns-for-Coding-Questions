import decimal


class Account:
    # def __init__ 已省略... ...

    @classmethod
    def from_string(cls, s):
        """从字符串初始化一个账号

        :returns: 如果输入合法，返回 Account object，否则返回 NullAccount
        """
        try:
            username, balance = s.split()
            balance = decimal.Decimal(float(balance))
        except ValueError:
            return NullAccount()

        if balance < 0:
            return NullAccount()
        return cls(username=username, balance=balance)


class NullAccount:
    username = ''
    balance = 0

    @classmethod
    def from_string(cls, s):
        raise NotImplementedError
