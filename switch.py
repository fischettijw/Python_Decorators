import os
os.system('cls')


def add(a, b):
    return a+b


def sub(a, b):
    return a-b


def mult(a, b):
    return a*b


def div(a, b):
    return a/b


def xxx():
    return '123456'


f = 'a'
x = 9
y = 3

math_func = {'a': lambda: add(x, y), 's': lambda: sub(x, y),
             'm': lambda: mult(x, y), 'd': lambda: div(x, y),
             'x': xxx}
func = math_func.get(f)
print()
print(f'{func.__name__}  -  {math_func.get(f)}')
print(math_func.get(f))
print(func.__name__, func())
print()
