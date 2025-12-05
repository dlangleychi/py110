# 12:05
'''
P: given integer, return sum of multiples of 7 or 11 that are less,
    double multiples only count once
E: 12 -> 18
D: none
A: iterate ints less than input, tally multiples of 7 or 11
C: below
'''

def seven_eleven(num):
    result = 0
    for i in range(1,num):
        if i % 7 == 0 or i % 11 == 0:
            result += i
    return result

print(seven_eleven(10) == 7)
print(seven_eleven(11) == 7)
print(seven_eleven(12) == 18)
print(seven_eleven(25) == 75)
print(seven_eleven(100) == 1153)
print(seven_eleven(0) == 0)
print(seven_eleven(-100) == 0)