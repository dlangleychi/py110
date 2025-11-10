'''
P: given int iteratively rotate digits 
    after each iteration fix one more on the left, return int
E: 735291 -> 321579
D: none
A: apply rightmost rotate n times each time decreasing count
C: below
'''

def rotate_rightmost_characters(string, count):
    front, back = string[:-count], string[-count:]
    new_back = back[1:] + back[0]
    return front + new_back

def max_rotation(num):
    str_num = str(num)
    for count in range(len(str_num), 0, -1):
        str_num = rotate_rightmost_characters(str_num, count)
    return int(str_num)

print(max_rotation(735291) == 321579)          # True
print(max_rotation(3) == 3)                    # True
print(max_rotation(35) == 53)                  # True
print(max_rotation(8703529146) == 7321609845)  # True

# Note that the final sequence here is `015`. The leading
# zero gets dropped, though, since we're working with
# an integer.
print(max_rotation(105) == 15)                 # True