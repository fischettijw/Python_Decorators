def add(*args, **kwargs):
    sum = 0
    for arg in args:
        sum += arg
    sum2 = 0
    for kwarg in kwargs.items():
        sum2 += kwarg[1]
        # print('*', kwarg[1])

    return (sum, sum2, kwargs)


a = 1
b = 2
c = 3
d = 4
e = 5

print(add(a))
print(add(a, b))
print(add(a, b, c))
print(add(a, b, c)[0])
print(add(a, b, c)[1])
print(add(a, b, c, d))
print(add(a, b, c, d, e, ab=9, cd=17))
print(add(a, b, c, d, e, ab=9, cd=17)[0])
print(add(a, b, c, d, e, ab=9, cd=17)[1])
print(add(a, b, c, d, e, ab=9, cd=17)[2])
