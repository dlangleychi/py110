'''
P: input int count (non negative), int start number
    output list of count multiple of start
E: 4, -7 -> [-7, -14, -21, -28]
D: list created for output
A: list comprehension with expression start * i, 
    iterable range(1, count + 1)
C: below
'''

def sequence(count, start):
    return [start * i for i in range(1, count + 1)]

print(sequence(5, 1) == [1, 2, 3, 4, 5])          # True
print(sequence(4, -7) == [-7, -14, -21, -28])     # True
print(sequence(3, 0) == [0, 0, 0])                # True
print(sequence(0, 1000000) == [])                 # True