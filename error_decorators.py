import os
os.system('cls')


def exception_handler(func):
    print(6, func.__name__)

    def inner_function(*args, **kwargs):
        print(9, func.__name__)
        try:
            func(*args, **kwargs)
        except Exception as e:
            print(f"ERROR: {func.__name__} - {e}")
    print(14, func.__name__)
    return inner_function


@exception_handler
def area_square(length):
    print(f'area_square - {length * length}')


@ exception_handler
def area_circle(radius):
    print(f'area_circle - {3.14159 * radius * radius}')


@ exception_handler
def division(numerator, denominator):
    print(f'division - {numerator / denominator}')


print(33)
area_square(2)
# area_circle(2)
# division(2, 1)
# print()
# area_square('string')
# area_circle()
# division(5, 0)
# division(5)
# division(5, 1, 2)
# print()
