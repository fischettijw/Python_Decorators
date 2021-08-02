# import sys
import os
os.system('cls')


def dec_func(orig_func):
    def wrapper(*args, **kwargs):
        print(f"{'#'*18} {orig_func.__name__} {'#'*18}")
        print(f'{"Positional Args":^50}')
        for arg in args:
            print(arg, end=" - ")
        print()
        print(f'{"KeyWord Args":^50}')

        for kwarg in kwargs.items():
            print(kwarg, end=" - ")
        print()

        results = orig_func(*args, **kwargs)

        print(f'\n"{orig_func.__name__}" Returned Result: {results}')
        print('#'*18, orig_func.__name__, '#'*18)
        return results
    return wrapper


@ dec_func
def sum_1_to_n(max):
    sum = 0
    for num in range(1, max+1):
        sum += num
    return sum


def func_args(n):
    sum = 0
    for n in range(1, n+1):
        sum += n
    return sum


def func_args(*args):
    sum = 0
    for arg in args:
        sum += arg
    # print("Printing from 'prime_func()'\n")
    return sum


sum_1_to_n(6)

# func_arg(123, 456, a=2, b=4, c=6)


print()
