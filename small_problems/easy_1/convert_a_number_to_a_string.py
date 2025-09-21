'''
P: input non negative integer, output string representation
E: 4321 -> '4321'
D: none
A:
1. if input is 0, output '0'
2. set result = ''
3. while input > 0
    a. left concatenate chr of input mod 10 + ord('0') to result
    b. input to input quotient 10
4. return result
C: below
'''

def integer_to_string(integer):
    if integer == 0:
        return '0'
    
    result = ''

    while integer:
        result = chr((integer % 10) + ord('0')) + result
        integer //= 10

    return result

print(integer_to_string(4321) == "4321")              # True
print(integer_to_string(0) == "0")                    # True
print(integer_to_string(5000) == "5000")              # True
print(integer_to_string(1234567890) == "1234567890")  # True
