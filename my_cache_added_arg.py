import sys
import os
os.system('cls')

# sys.setrecursionlimit = 501
# print(sys.getrecursionlimit())
cache = {}


def cached(func):
    # cache = {}
    global cache

    def wrapper(*args):
        signature = (func, args)
        if signature in cache:
            results = cache[signature]
        else:
            results = func(*args)
            cache[signature] = results
        return results
    return wrapper


@cached
def fib(n, w):
    if n <= 1:
        return n
    return fib(n - 1, w) + fib(n - 2, w)


for i in range(498):
    print(i, fib(i, 99))

# f = 499
# print(f, fib(f))
print(cache)
