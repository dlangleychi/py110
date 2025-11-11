'''
P: given integer, return difference between square of sum and
    and the sum of squares of digits up to and including input
E: 3 -> 22
D: none
A: calculate quantities and their difference
C: below
'''

def sum_square_difference(num):
    square_of_sum = int(num *(num + 1)/2) ** 2
    sum_of_squares = 0
    for i in range(1, num + 1):
        sum_of_squares += i ** 2

    return square_of_sum - sum_of_squares

print(sum_square_difference(3) == 22)          # True
# 22 --> (1 + 2 + 3)**2 - (1**2 + 2**2 + 3**2)

print(sum_square_difference(10) == 2640)       # True
print(sum_square_difference(1) == 0)           # True
print(sum_square_difference(100) == 25164150)  # True

# Further Exploration: there would be a collision with the
# built-in sum function, which the given solution uses