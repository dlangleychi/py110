# 12:09
'''
P: given string of numeric digits (at least 4), compute the max
    product of four consecutive digits
E: '1234' -> 24
D: none
A: product helper function, iterate through string, calling helper on
    each substring, keep track of the max
C: below
'''

def product(digit_string):
    result = 1
    for digit in digit_string:
        result *= int(digit)
    return result

def greatest_product(digit_string):
    result = 0
    for i in range(len(digit_string) - 3):
        result = max(result, product(digit_string[i : i + 4]))

    return result

print(greatest_product('23456') == 360)      # 3 * 4 * 5 * 6
print(greatest_product('3145926') == 540)    # 5 * 9 * 2 * 6
print(greatest_product('1828172') == 128)    # 1 * 8 * 2 * 8
print(greatest_product('123987654') == 3024) # 9 * 8 * 7 * 6