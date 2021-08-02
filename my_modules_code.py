import sys
import traceback
import inspect
import os
os.system('cls')

# global print_linenumbers
print_linenumbers = True


def config(is_linenumbers):
    global print_linenumbers
    print_linenumbers = is_linenumbers


def main():
    pprint('hello', 'goodbye', end='\n\n\n')
    pprint('hello', 'goodbye', end='')


def pprint(*args, **kwargs):
    global print_linenumbers
    if(print_linenumbers):
        caller = inspect.getframeinfo(inspect.stack()[1][0])
        print(f"{caller.lineno} -", *args, **kwargs)
    else:
        print(*args, **kwargs)


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


if __name__ == '__main__':
    main()
