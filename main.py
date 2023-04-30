# import decimal


# class Account:
#     def __init__(self, username, balance):
#         self.username = username
#         self.balance = balance

#     @classmethod
#     def from_string(cls, s):
#         try:
#             username, balance = s.split()
#             balance = decimal.Decimal(float(balance))
#         except ValueError:
#             return NullAccount()

#         if balance < 0:
#             return NullAccount()
#         return cls(username=username, balance=balance)


# class NullAccount:
#     username = ''
#     balance = 0

#     @classmethod
#     def from_string(cls, s):
#         raise NotImplementedError


# accounts_data = [
#     'david 98.5',
#     'cotton 21',
#     'invalid_data',
#     'roland $invalid_balance',
#     'alfred -3',
# ]


# def caculate_total_balance(accounts_data):
#     return sum(Account.from_string(s).balance for s in accounts_data)


# print(caculate_total_balance(accounts_data))

import decimal


class CreateAccountError(Exception):
    """Unable to create a account error"""


class Account:

    def __init__(self, username, balance):
        self.username = username
        self.balance = balance

    @classmethod
    def from_string(cls, s):
        try:
            username, balance = s.split()
            balance = decimal.Decimal(float(balance))
        except ValueError:
            raise CreateAccountError(
                'input must follow pattern "{ACCOUNT_NAME} {BALANCE}"')

        if balance < 0:
            raise CreateAccountError('balance can not be negative')
        return cls(username=username, balance=balance)


def caculate_total_balance(accounts_data):
    result = 0
    for account_string in accounts_data:
        try:
            user = Account.from_string(account_string)
        except CreateAccountError:
            pass
        else:
            result += user.balance
    return result


accounts_data = [
    'piglei 96.5',
    'cotton 21',
    'invalid_data',
    'roland $invalid_balance',
    'alfred -3',
]

print(caculate_total_balance(accounts_data))
