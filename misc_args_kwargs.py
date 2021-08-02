import os
os.system('cls')


def sum1(a, b, c):              # 3 positional arguments
    return a+b+c


def sum2(*args):                # any number of positional arguments
    sum = 0
    for arg in args:
        sum += arg
    return sum


def sum3(**kwargs):             # any number of keyword arguments
    sum = 0
    for kwarg in kwargs.values():
        sum += kwarg
    return sum


def sum4(*args, **kwargs):      # any number of positional & keywords arguments
    sum = 0
    for arg in args:
        sum += arg
    for kwarg in kwargs.values():
        sum += kwarg
    return sum


print('sum1:', sum1(2, 4, 6), '\n')
print('sum2:', sum2(2, 4, 6), '\n')
print('sum3: ', sum3(x=2, y=4, z=6), '\n')

print('sum4: ', sum4(2, y=4, z=6), '\n')
print('sum4: ', sum4(y=4, z=6), '\n')
print('sum4: ', sum4(2), '\n')
print('sum4: ', sum4(), '\n')
