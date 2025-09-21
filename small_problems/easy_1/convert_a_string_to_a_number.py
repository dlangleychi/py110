'''
P: input unsigned integer string, output integer
E: '4321' - > 4321
D: none
A:
1. initialize result to 0
2. iterate through characters of input string,
    each time multiply result by 10 and adding ord(char) - ord('0')
3. return result
C: below
'''

def string_to_integer(integer_string):
    result = 0
    for char in integer_string:
        result = result * 10 + ord(char) - ord('0')
    return result

print(string_to_integer("4321") == 4321)  # True
print(string_to_integer("570") == 570)    # True

def hexadecimal_to_integer(hex_string):
    result = 0
    for char in hex_string:
        if ord('0') <= ord(char) <= ord('9'):
            result = result * 16 + ord(char) - ord('0')
        else:
            result = result * 16 + ord(char.upper()) - ord('A') + 10
    return result

print(hexadecimal_to_integer('4D9f') == 19871)  # True