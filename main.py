from itertools import takewhile

numbers = [2, 4, 5, 6, 7, 8, 9, 10]


def is_even(num):
    return num % 2 == 0


even_numbers = takewhile(is_even, numbers)

for num in even_numbers:
    print(num)
