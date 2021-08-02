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


if __name__ == '__main__':
    main()
