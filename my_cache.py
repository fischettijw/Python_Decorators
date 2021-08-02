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
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


for i in range(10):
    print(i, fib(i))

# f = 499
# print(f, fib(f))
print(cache)
