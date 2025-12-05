# 9:55
'''
P: given string of lowercase characters, return repeat tuple
E: 'xyz' -> ('xyz', 1)
D: none
A: starting with divisor = 1, if divisor divides len string,
    test if substring * quotient equals string
C: below
'''

def repeated_substring(string):
    string_len = len(string)

    ans = None

    for divisor in range(1, string_len + 1):
        if string_len % divisor == 0:
            sub_len = string_len // divisor
            if string[:sub_len] * divisor == string:
                ans = (string[:sub_len], divisor)

    return ans

print(repeated_substring('xyzxyzxyz') == ('xyz', 3))
print(repeated_substring('xyxy') == ('xy', 2))
print(repeated_substring('xyz') == ('xyz', 1))
print(repeated_substring('aaaaaaaa') == ('a', 8))
print(repeated_substring('superduper') == ('superduper', 1))