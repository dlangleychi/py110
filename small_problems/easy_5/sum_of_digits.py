'''
P: input positive integer
    output sum of digits
E: 123 -> 6
D: none
A: while input, result += input % 10 input //= 10
C: below 
'''

def sum_digits(pos_int):
    result = 0
    while pos_int:
        result += pos_int % 10
        pos_int //= 10

    return result

def sum_digits(pos_int):
    return sum([int(digit) for digit in str(pos_int)])

print(sum_digits(23) == 5)              # True
print(sum_digits(496) == 19)            # True
print(sum_digits(123456789) == 45)      # True