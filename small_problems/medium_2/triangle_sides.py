'''
P: take three float length, return what type of triangle if any
    they make
E: 3, 3, 3 -> 'equilateral'
D: none
A: using math.isclose, conditional statements
C: below
'''

from math import isclose

def triangle(a, b, c):

    a, b, c = sorted([a, b, c])
    if isclose(a, 0) or a + b <= c:
        return 'invalid'
    
    if isclose(a, b) and isclose(b, c):
        return 'equilateral'
    elif isclose(a, b) or isclose(b, c) or isclose(a, c):
        return 'isosceles'
    else:
        return 'scalene'
    
print(triangle(3, 3, 3) == "equilateral")  # True
print(triangle(3, 3, 1.5) == "isosceles")  # True
print(triangle(3, 4, 5) == "scalene")      # True
print(triangle(0, 3, 3) == "invalid")      # True
print(triangle(3, 1, 1) == "invalid")      # True