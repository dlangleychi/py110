'''
P: input integer, output string representation of input
    sign only present for negatives, positive, but not zero
E: -123 -> '-123', 4321 -> '+4321'
D: none
A:
1. if input < 0, return '-' + conversion of -1 * input
2. if input > 0, return '+' + conversion
3. otherwise return '0'
C: below
'''

def signed_integer_to_string(integer):
    if integer < 0:
        return '-' + integer_to_string(-1 * integer)
    if integer > 0:
        return '+' + integer_to_string(integer)
    return '0'

def integer_to_string(integer):
    if integer == 0:
        return '0'
    
    result = ''

    while integer:
        result = chr((integer % 10) + ord('0')) + result
        integer //= 10

    return result

print(signed_integer_to_string(4321) == "+4321")  # True
print(signed_integer_to_string(-123) == "-123")   # True
print(signed_integer_to_string(0) == "0")         # True