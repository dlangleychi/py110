'''
P: given number of digits, reutrn index of first fibonacci with
    that number of digits
E: 2 -> 7
D: none
A: while loop fib < limit, compute the next fib, increment index
    after it breaks return index
C: below
'''

import sys

sys.set_int_max_str_digits(50_000)

def find_fibonacci_index_by_length(length):
    if length == 1:
        return 1
    a, b = 1, 1
    index = 2
    limit = 10 ** (length - 1)
    while b < limit:
        a, b, = b, a + b
        index += 1
    return index
    
# All of these examples should print True
# The first 12 fibonacci numbers are: 1 1 2 3 5 8 13 21 34 55 89 144
print(find_fibonacci_index_by_length(2) == 7)
print(find_fibonacci_index_by_length(3) == 12)
print(find_fibonacci_index_by_length(10) == 45)
print(find_fibonacci_index_by_length(16) == 74)
print(find_fibonacci_index_by_length(100) == 476)
print(find_fibonacci_index_by_length(1000) == 4782)

# Next example might take a little while on older systems
print(find_fibonacci_index_by_length(10000) == 47847)