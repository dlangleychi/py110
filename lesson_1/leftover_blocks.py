'''
Problem:

input: number of blocks
output: number of leftover blocks

explicit:
    top layer is single block
    each block supported by four block in lower layer
    no gaps between blocks

implicit:
    zero input -> zero output

questions:
    what does supported mean?
    does support need to be on the same level?
    what does gap mean?
    is all support above or below?

'''

'''
Examples and test cases:

- zero input -> zero left over
- layers appear to be square
- appear we are looking for a symetric square pyramid
- no excess blocks in layer because you want tallest pyramid
- answer can be zero

'''

'''
Data Structures:

- none

'''

'''
Algorithm:

1. build the structure recording how many block used each level
2. once you don't have enough for next level, return remaining blocks

int layer_size set to 1

while number_blocks >= layer of layer_size
    number_blocks -= layer of layer_size
    layer_size += 1

return number_blocks

'''

def calculate_leftover_blocks(number_blocks):
    layer_size = 1
    
    while number_blocks >= layer_size ** 2:
        number_blocks -= layer_size ** 2
        layer_size += 1

    return number_blocks

print(calculate_leftover_blocks(0) == 0)  # True
print(calculate_leftover_blocks(1) == 0)  # True
print(calculate_leftover_blocks(2) == 1)  # True
print(calculate_leftover_blocks(4) == 3)  # True
print(calculate_leftover_blocks(5) == 0)  # True
print(calculate_leftover_blocks(6) == 1)  # True
print(calculate_leftover_blocks(14) == 0) # True

