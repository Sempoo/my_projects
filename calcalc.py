a = -2
b = 3

# TODO: problems with negative numbers - try to use abs()
# TODO: and then add back the minus sign


def multiplier_finder(x):
    print('\n-- multiplier_finder(x) --')

    string_version = str(x)
    print('string_version =', string_version)

    if string_version.find('.') > 0:
        print('string has dot')

        if string_version.find('-') == 0:
            print('string has minus')
            digits = len(string_version) - 2
            print('digits =', digits)
            digits_after_dot = digits - string_version.find('.') + 1
            print('digits_after_dot =', digits_after_dot)
            multiplier = int('1' + multiplication(digits_after_dot, '0'))
            print('multiplier =', multiplier)
            return multiplier, digits_after_dot
        else:
            digits = len(string_version) - 1
            print('digits =', digits)
            digits_after_dot = digits - string_version.find('.')
            print('digits_after_dot =', digits_after_dot)
            multiplier = int('1' + multiplication(digits_after_dot, '0'))
            print('multiplier =', multiplier)
            return multiplier, digits_after_dot

    else:
        print('string is integer')
        multiplier = 1
        print('multiplier =', multiplier)
        return multiplier, 0


def multiplication(x, y):
    print('\n-- multiplication(x, y) --')
    z = y
    if x == 0:
        return 0
    if y == 0:
        return 0
    if int(x) != x:
        print('x is float')
        integer_part = int(x)
        print('integer_part =', integer_part)
        float_remainder = round(x - integer_part, multiplier_finder(x)[1])
        print('float_remainder =', float_remainder)
        for i in range(integer_part-1):
            y += z
        if integer_part == 0:
            return round(multiplication(z, float_remainder))
        else:
            return y + round(multiplication(z, float_remainder))
    else:
        print('x is integer')
        integer_part = x
        print('integer_part =', integer_part)
        for i in range(integer_part-1):
            y += z
        return y


def float_result(integer_result, decimal_places):
    print('\n-- float_result(ab_integer_multiplication, length_final) --')
    string_version = str(integer_result)
    print('string version =', string_version)
    print('decimal_places =', decimal_places)
    radix_point_index = - decimal_places
    print('radix_point_index =', radix_point_index)
    if radix_point_index == 0:
        return integer_result
    decimal_part = string_version[:radix_point_index]
    print('decimal_part =', decimal_part)
    fractional_part = string_version.zfill(decimal_places)[radix_point_index:]
    print('fractional_part =', fractional_part)
    number = float(decimal_part + '.' + fractional_part)
    return number


multiplier_a = multiplier_finder(a)[0]
multiplier_b = multiplier_finder(b)[0]
print('multiplier_a =', multiplier_a)
print('multiplier_b =', multiplier_b)

integer_a = multiplication(a, multiplier_a)
integer_b = multiplication(b, multiplier_b)
print('integer_a =', integer_a)
print('integer_b =', integer_b)
print('type of integer_a =', type(integer_a))
print('type of integer_b =', type(integer_b))

length_a = multiplier_finder(a)[1]
length_b = multiplier_finder(b)[1]
print('length_a =', length_a)
print('length_b =', length_b)

length_final = length_a + length_b
print('length_final =', length_final)

ab_integer_multiplication = multiplication(integer_a, integer_b)
print('integer_a =', integer_a)
print('integer_b =', integer_b)
print('ab_integer_multiplication =', ab_integer_multiplication)

final_result = float_result(ab_integer_multiplication, length_final)
print('\na =', a)
print('b =', b)
print('reference result =', a * b)
print('\n__FINAL RESULT__ =', final_result)
