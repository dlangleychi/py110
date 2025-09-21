'''
P: input possibly signed integer_string, output integer string
represents
E: '-570'
D: none
A:
1. if first character is '-', return -1 * conversion 
    of remaining characters
2. if first character is '+' return conversion remaining
3. else return conversion
C: below
'''

def string_to_signed_integer(integer_string):
    if integer_string[0] == '-':
        return -1 * string_to_integer(integer_string[1:])
    if integer_string[0] == '+':
        return string_to_integer(integer_string[1:])
    return string_to_integer(integer_string)

def string_to_integer(integer_string):
    result = 0
    for char in integer_string:
        result = result * 10 + ord(char) - ord('0')
    return result

print(string_to_signed_integer("4321") == 4321)  # True
print(string_to_signed_integer("-570") == -570)  # True
print(string_to_signed_integer("+100") == 100)   # True