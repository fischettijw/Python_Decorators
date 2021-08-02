"""
https://www.youtube.com/watch?v=WDMr6WolKUM&list=PLWBKAf81pmOaP9naRiNAqug6EBnkPakvY&index=3
"""
# region 1
import os
os.system("cls")


def dec(func):
    print("in dec", func)
    return func


def f(x):
    print(f"hello {x}")


f(2)
print()
f = dec(f)
print()
f(1)
print()
f(2)
# endregion 1
