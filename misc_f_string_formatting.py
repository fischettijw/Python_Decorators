import os
os.system('cls')

# https://saralgyaan.com/posts/f-string-in-python-usage-guide/#Calculations
num = 123
print(f'{num}')
print(f'{num=}')
print(f'{num = }')
print('-'*38, '\n')


num = 123.456
print(f'{num}')
print(f'{num:.2f}')
print(f'{num:15.2f}')
print(f'{num:>15.2f}')
print(f'{num:<15.2f}')
print(f'{num:^15.2f}')
print('-'*38, '\n')


print(f'{8.7:08}')
print(f'{8:08}')
print(f'{8:8}')
print('-'*38, '\n')


print(f'{"My Grocery List":^38s}')
print(f'{"="*38}')
print(f'{"Apples"}\t{3:10d}\t\t${1.5:>5.2f}')
print(f'{"Bread"}\t{4:10d}\t\t${6:>5.2f}')
print(f'{"Chesse"}\t{2:10d}\t\t${4.5:>5.2f}')
print(f'{"Total:":>19s}\t\t${13.5:>4.2f}')
print('-'*38, '\n')
