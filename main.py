s = '''--
example
--'''


def strip_hyphen(s):
    yield s.strip()


print(strip_hyphen(s))
