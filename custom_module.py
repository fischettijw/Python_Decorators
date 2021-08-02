# C:\Users\fisch\AppData\Roaming\Python\Python39\site-packages\jwf

from my_modules.func_jwf import pprint, config, exception_handler

import os
os.system('cls')

config(True)

pprint('joe', end='\n\n\n')
pprint('test', end='\n\n')


@exception_handler
def area_square(length):
    pprint('area_square -', length * length)


@ exception_handler
def area_circle(radius):
    pprint('area_square -', 3.14 * radius * radius)


@ exception_handler
def division(length, breadth):
    pprint('divisione -', length / breadth)


area_square(2)
area_circle(2)
division(2, 1)
print()
area_square('string')
area_circle()
division(5, 0)
print()
