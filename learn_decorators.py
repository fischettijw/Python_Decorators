# import sys
import os
os.system('cls')


def dec_func(orig_func):
    def wrapper(*args, **kwargs):
        print("Printing from wrapper func => BEFORE func call\n")
        results = orig_func(*args, **kwargs)
        print("Printing from wrapper func => AFTER func call\n")
        return results
    return wrapper


@dec_func
def prime_func(num):
    print("Printing from 'prime_func()'\n")
    return 2*num


print(prime_func(123))


# @dec_func
# def prime_func():
#     print("Printing from 'prime_func()'\n")
#     return 321


# print(dec_func(prime_func))
# print(dec_func(lambda: prime_func(123)))

print()
