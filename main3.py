class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_simple_display(self):
        return f'{self.name}({self.age})'

    def get_long_display(self):
        return f'{self.name} is {self.age} years old.'


piglei = Student('David', '33')
# OUTPUT: David(33)
print(piglei.get_simple_display())
# OUTPUT: piglei is 18 years old.
print(piglei.get_long_display())
