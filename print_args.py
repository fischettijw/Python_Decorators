import os
os.system('cls')

arguments_on = True


def arguments(func):
    global arguments_on

    def wrapper(*args, **kwargs):
        if arguments_on == True:
            print()
            n = 1
            for arg in args:
                print(f'arg-{n} = {arg}')
                n += 1
            for key, value in kwargs.items():
                print(f'key = {key}    value = {value}')
            print()
        return func(*args, **kwargs)
    return wrapper


@arguments
def add_sub(*args, sub=0):
    sum = 0
    for num in args:
        sum += num
    return sum-sub


print(f'ad_sub = {add_sub(4, 2, 2, 1, 5)}\n\n')
print(f'ad_sub = {add_sub(4, 2, 2, 1, 5, sub = 11)}\n\n')
