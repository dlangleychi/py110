#9:49
'''
P: given string of digits, return number of even_numbered (non-zero)
    substrings, count duplicates
E: '1432' -> 6
D: none
A: only need to test last digit, if even, count number of substrings
    with that ending
C: below
'''

def even_substrings(digit_string):
    result = 0
    for idx, digit in enumerate(digit_string):
        if int(digit) % 2 == 0:
            result += idx + 1

    return result

print(even_substrings('1432') == 6)
print(even_substrings('3145926') == 16)
print(even_substrings('2718281') == 16)
print(even_substrings('13579') == 0)
print(even_substrings('143232') == 12)