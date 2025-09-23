'''
P: input int (assumed positive), 
    output list with 1 up to and including input
E: 5 -> [1, 2, 3, 4, 5]
D: the list created for output
A: list of range(1, input + 1)
C: below
'''

def sequence(limit):
    return list(range(1, limit + 1))

print(sequence(5) == [1, 2, 3, 4, 5])   # True
print(sequence(3) == [1, 2, 3])         # True
print(sequence(1) == [1])               # True