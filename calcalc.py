# TODO: write functions documentation


def addition(x, y):
    return x + y


def subtraction(x, y):
    return x - y


def multiplier_finder(x):
    string_version = str(abs(x))
    if string_version.find('.') > 0:
        digits = len(string_version) - 1
        digits_after_dot = digits - string_version.find('.')
        multiplier = int('1' + sub_multiplication(digits_after_dot, '0'))
        return multiplier, digits_after_dot
    else:
        return 1, 0


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


def float_result(integer_result, decimal_places, x, y):
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

    multiplication_result = float_result(xy_integer_multiplication, length_final, x, y)

    return multiplication_result


a = 23.77
b = 3.14

print('ref result     =', a * b)
print('multiplication =', multiplication(a, b))


def sub_division(numerator, denominator):
    if denominator == 0:
        return 'illegal division by zero'
    if denominator < 0:
        quotient, remainder = sub_division(numerator, -denominator)
        return -quotient, remainder
    if numerator < 0:
        quotient, remainder = sub_division(-numerator, denominator)
        if remainder == 0:
            return -quotient, 0
        else:
            return -quotient-1, denominator-remainder
    quotient = 0
    remainder = numerator
    while remainder >= denominator:
        quotient += 1
        remainder -= denominator
    return quotient, remainder


def long_division(numerator, denominator, decimal_places=16):
    num = numerator
    den = denominator
    numerator = abs(numerator)
    denominator = abs(denominator)

    num_string = str(numerator) + sub_multiplication(decimal_places, '0')
    decimal_dot = len(str(numerator))
    quotient = ''
    index = 0
    c = 1
    quotient_digit = sub_division(int(num_string[index]), denominator)[0]
    difference = int(num_string[index:c])

    while quotient_digit == 0:
        quotient += str(quotient_digit)
        c += 1
        difference = int(num_string[index:c])
        quotient_digit = sub_division(difference, denominator)[0]

    quotient += str(quotient_digit)

    while True:
        if len(quotient) == len(num_string):
            break
        index += 1
        subtrahend = multiplication(quotient_digit, denominator)
        diff_part = difference - subtrahend
        difference = int(str(diff_part) + num_string[c])
        c += 1
        if difference == 0:
            break
        quotient_digit = sub_division(difference, denominator)[0]
        quotient += str(quotient_digit)

    quotient = list(quotient)
    quotient.insert(decimal_dot, '.')
    quotient = ''.join(quotient)
    quotient = quotient.lstrip('0')
    quotient = float(quotient)

    if abs(num) == num and abs(den) == den:
        return quotient
    elif abs(num) == num or abs(den) == den:
        return -quotient
    else:
        return quotient


def final_division(pre_division, length_final, x, y):
    print('pre_division =', pre_division)
    print('length_final =', length_final)
    print('x =', x)
    print('y =', y)
    if length_final == 0:
        if abs(x) == x and abs(y) == y:
            return pre_division
        elif abs(x) == x or abs(y) == y:
            return -pre_division
        else:
            return pre_division

    else:
        # TODO: get rid of ** - exponentiation
        #
        result = multiplication(pre_division, 10**length_final)

        if abs(x) == x and abs(y) == y:
            return result
        elif abs(x) == x or abs(y) == y:
            return -result
        else:
            return result


def division(x, y, decimal_places):
    multiplier_x = multiplier_finder(x)[0]
    multiplier_y = multiplier_finder(y)[0]

    integer_x = sub_multiplication(x, multiplier_x)
    integer_y = sub_multiplication(y, multiplier_y)

    length_x = multiplier_finder(x)[1]
    length_y = multiplier_finder(y)[1]

    length_final = length_y - length_x

    pre_division = long_division(integer_x, integer_y, decimal_places)

    division_result = final_division(pre_division, length_final, x, y)

    return division_result


a = -2.1
b = -3
precision = 5  # >7 may result in very long computing times


print('ref result    =', round(a / b, precision-1))
# print('long_division =', long_division(a, b))

print('division      =', division(a, b, precision))
