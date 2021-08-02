import sys
import traceback
import os
os.system('cls')


def exception_handler(func):
    def inner_function(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            tb = traceback.extract_tb(exc_tb)[-1]
            print(f"{func.__name__} - {e}")
            print(f'Line Number: {tb[1]}\n')
    return inner_function


@exception_handler
def area_square(length):
    print('area_square -', length * length)


@ exception_handler
def area_circle(radius):
    print('area_square -', 3.14 * radius * radius)


@ exception_handler
def division(length, breadth):
    print('divisione -', length / breadth)


area_square(2)
area_circle(2)
division(2, 1)
print()
area_square('string')
area_circle()
division(5, 0)
print()
