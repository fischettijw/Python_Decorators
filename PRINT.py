import inspect
import os
os.system('cls')

print_linenumbers = True


def pprint(*args, **kwargs):
    global print_linenumbers
    if(print_linenumbers):
        caller = inspect.getframeinfo(inspect.stack()[1][0])
        print(f"{caller.lineno} -", *args, **kwargs)
    else:
        print(*args, **kwargs)


pprint('hello', 'goodbye', end='\n\n\n')

pprint('hello', 'goodbye', end='')
