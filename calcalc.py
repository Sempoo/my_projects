# I want it to be a special calculator, which is entirely based on addition;
# so for example multiplication is a repeated form of addition, and so on...

#

x = int(input('x = '))
y = int(input('y = '))


def or_gate(a, b):
    if a == b == 0:
        return 0
    elif a < b:
        return b
    elif a > b:
        return a
    else:
        return a


def xor_gate(a, b):
    if a == b == 0:
        return 0
    elif a < b:
        return b
    elif a > b:
        return a
    else:
        return 0


def and_gate(a, b):
    if a == b == 0:
        return 0
    elif a < b:
        return a
    elif a > b:
        return b
    else:
        return a

carry = and_gate(x, y)
sum = xor_gate(x, y)


def half_adder(a, b):
    return [carry, sum]


def full_adder(a, b, c):
    pass

print(half_adder(x, y))

half_adder_return_list = half_adder(x, y)

result = str(half_adder_return_list[0]) + str(half_adder_return_list[1])

print(result)