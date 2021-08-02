import os
os.system('cls')


def display(p):
    print(p)


x = True
x = True if x == False else True
print(x)
print('F') if x == False else print('T')
display(False) if x == False else display(True)
print('-'*38, '\n')


str = '123-456-7890'
print(str)
for n in str:
    print(n, end='') if n != '-' else print('', end='')
print()
str = '123-456-7890'
str = str.replace('-', '')
print(str)
print('-'*38, '\n')


x = 7_654_321
print(x)
print('-'*38, '\n')
