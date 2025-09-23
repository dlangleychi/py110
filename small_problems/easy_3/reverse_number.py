'''
P: input postive integer, output int with digits reversed
E: 12345 -> 54321
D: none
A: apply str, reverse, apply int
C: below
'''

def reverse_number(pos_int):
    return int(str(pos_int)[::-1])

print(reverse_number(12345) == 54321)   # True
print(reverse_number(12213) == 31221)   # True
print(reverse_number(456) == 654)       # True
print(reverse_number(1) == 1)           # True
print(reverse_number(12000) == 21)      # True