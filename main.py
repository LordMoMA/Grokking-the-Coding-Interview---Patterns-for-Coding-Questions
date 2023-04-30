def remove_even(numbers):
    for number in numbers:
        if number % 2 != 0:
            yield number


numbers = [1, 2, 7, 4, 8, 11]
numbers = list(remove_even(numbers))
print(numbers)
