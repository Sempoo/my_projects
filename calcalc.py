# I want it to be a special calculator, which is entirely based on addition;
# so for example multiplication is a repeated form of addition, and so on...

a = 0.1
b = 1

print('a =', a)
print('b =', b)
print('reference_result =', a * b)


def multiplier_finder(x):
    string_version = str(x)
    dot_index = string_version.find('.') + 1
    num_length = len(string_version)
    print('###')
    print('string_version =', string_version)
    print('string_version[0] =', string_version[0])
    print('dot_index =', dot_index)
    print('num_length =', num_length)
    print('###')
    if string_version.find('.') >= 0:
        multiplier = '1' + multiplication((num_length-dot_index), '0')
        print('multiplier =', multiplier)
        print('###')
        return int(multiplier), len(multiplier)-1
    if string_version[0] == '0':
        multiplier = '1' + multiplication((num_length-dot_index), '0')
        return int(multiplier), len(multiplier)
    else:
        return 1, 0




def multiplication(a, b):
    c = b
    if a == 0:
        return 0
    if b == 0:
        return 0
    print('str(a)[0] =', (str(a)[0]))
    if str(a)[0] == '0':
        return b
    if int(a) != a:
        integer_part = int(a)
        float_remainder = a - integer_part
        for i in range(integer_part-1):
            b += c

        return b + multiplication(c, float_remainder)
    else:
        integer_part = a
        for i in range(integer_part-1):
            b += c
        return b


def float_result(integer_result, decimal_places):
    string_version = str(integer_result)
    radix_point_index = -decimal_places
    if radix_point_index == 0:
        return integer_result
    decimal_part = string_version[:radix_point_index]
    fractional_part = string_version[radix_point_index:]
    number = float(decimal_part + '.' + fractional_part)
    print('###')
    print('string_version =', string_version)
    print('radix_point_index =', radix_point_index)
    print('decimal_part =', decimal_part)
    print('fractional_part =', fractional_part)
    print('###')
    return number




multiplier_a = multiplier_finder(a)
multiplier_b = multiplier_finder(b)
print('multiplier_a =', multiplier_a[0])
print('multiplier_b =', multiplier_b[0])

integer_a = int(multiplication(a, multiplier_a[0]))
integer_b = int(multiplication(b, multiplier_b[0]))
print('integer_a =', integer_a)
print('integer_b =', integer_b)

length_a = multiplier_a[1]
length_b = multiplier_b[1]
print('length_a =', length_a)
print('length_b =', length_b)

integers_multiplication = multiplication(integer_a, integer_b)
print('integers_multiplication =', integers_multiplication)

length_final = length_a + length_b
print('length_final =', length_final)

final_result = float_result(integers_multiplication, length_final)
print('\n\nfinal_result =', final_result)
