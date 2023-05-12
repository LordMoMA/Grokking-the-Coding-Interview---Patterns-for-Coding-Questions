class Foo:
    def __call__(self):
        print("Hello, __call___")


foo = Foo()

# OUTPUT: True
print(callable(foo))
# 调用 foo 实例
# OUTPUT: Hello, __call__
foo()
