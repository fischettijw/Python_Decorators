# https://www.youtube.com/watch?v=OPYL34LmB7s&list=PL6cactdCCnTIps8-67AWHzH0ErFlOJTdw&index=5
# https://www.youtube.com/watch?v=762mFeD2SlU
# Why @Wraps(fn)   https://www.youtube.com/watch?v=6LZeIeoa5kI
# https://www.youtube.com/watch?v=WDMr6WolKUM&list=PLWBKAf81pmOaP9naRiNAqug6EBnkPakvY&index=3
# Decorator withour arguments    https://www.youtube.com/watch?v=FsAPt_9Bf3U&t=38s
# Decorator with arguments    https://www.youtube.com/watch?v=KlBPCzcQNU8

import time as tm
from functools import wraps
import os
os.system('cls')


print('\n***** DECORATORS *****')


def speed_test(fn):
    @wraps(fn)    # https://www.youtube.com/watch?v=6LZeIeoa5kI
    def wrapper(*args, **kwargs):
        start_time = tm.time()
        result = fn(*args, **kwargs)
        end_time = tm.time()
        print()
        print(f'Executing {fn.__name__}')
        print(f'Time Elapsed: {end_time - start_time}')
        return result
    return wrapper


@speed_test
def sum_nums_gen():
    return sum(x for x in range(10_000_000))


@speed_test
def sum_nums_list():
    return sum([x for x in range(10_000_000)])


print(sum_nums_gen())
print(sum_nums_list())
print()
print('*'*40)
