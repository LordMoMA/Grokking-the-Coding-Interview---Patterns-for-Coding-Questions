class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __format__(self, format_spec):
        if format_spec == 'long':
            return f'{self.name} is {self.age} years old.'
        elif format_spec == 'simple':
            return f'{self.name}({self.age})'
        raise ValueError('invalid format spec')


david = Student('david', '33')
print('{0:simple}'.format(david))
print('{0:long}'.format(david))
