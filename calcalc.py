a = 0.00034
b = 53453.53455


def addition(x, y):
    return x + y


def multiplier_finder(x):
    string_version = str(abs(x))
    if string_version.find('.') > 0:
        digits = len(string_version) - 1
        digits_after_dot = digits - string_version.find('.')
        multiplier = int('1' + sub_multiplication(digits_after_dot, '0'))
        return multiplier, digits_after_dot
    else:
        multiplier = 1
        return multiplier, 0


def sub_multiplication(x, y):
    x = abs(x)
    z = y
    if x == 0:
        return 0
    if y == 0:
        return 0
    if int(x) != x:
        integer_part = int(x)
        float_remainder = round(x - integer_part, multiplier_finder(x)[1])
        for i in range(integer_part-1):
            y += z
        if integer_part == 0:
            return round(sub_multiplication(z, float_remainder))
        else:
            return y + round(sub_multiplication(z, float_remainder))
    else:
        integer_part = x
        for i in range(integer_part-1):
            y += z
        return y


def final_result(integer_result, decimal_places, x, y):
    string_version = str(integer_result)
    radix_point_index = - decimal_places
    if radix_point_index == 0:
        if abs(x) == x and abs(y) == y:
            return integer_result
        elif abs(x) == x or abs(y) == y:
            return -integer_result
        else:
            return integer_result
    decimal_part = string_version[:radix_point_index]
    fractional_part = string_version.zfill(decimal_places)[radix_point_index:]
    number = float(decimal_part + '.' + fractional_part)
    if abs(x) == x and abs(y) == y:
        return number
    elif abs(x) == x or abs(y) == y:
        return -number
    else:
        return number


def multiplication(x, y):
    multiplier_x = multiplier_finder(x)[0]
    multiplier_y = multiplier_finder(y)[0]

    integer_x = sub_multiplication(x, multiplier_x)
    integer_y = sub_multiplication(y, multiplier_y)

    length_x = multiplier_finder(x)[1]
    length_y = multiplier_finder(y)[1]

    length_final = length_x + length_y

    xy_integer_multiplication = sub_multiplication(integer_x, integer_y)

    the_final_result = final_result(xy_integer_multiplication, length_final, x, y)

    print('\nx =', x)
    print('y =', y)
    print('reference result =', x * y)
    print('\n__FINAL RESULT__ =', the_final_result)
    print(type(the_final_result))


multiplication(a, b)
