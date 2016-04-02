# I want it to be a special calculator, which is entirely based on addition;
# so for example multiplication is a repeated form of addition, and so on...


def addition(x, y):
    z = x + y
    return z


def multiplication(a, b):
    c = b
    if int(a) != a:
        integer_part = int(a)
        float_remainder = a - integer_part
        for i in range(integer_part-1):
            b = b + c
        return b + multiplication(integer_part, float_remainder)
    else:
        integer_part = a
        for i in range(integer_part-1):
            b = b + c
        return b

a = 1.1
b = 0.2
print('ref =', a*b)
print('     ', multiplication(a, b))
