'''
P: given int and number of digits, rotate the last number digits
    by move left most digit to end, return in
E: 1234, 2 -> 1243
D: none
A: concatenate three pieces
C: below
'''

def rotate_rightmost_digits(num, count):
    str_num = str(num)
    front, back = str_num[:-count], str_num[-count:]
    new_back = back[1:] + back[0]
    return int(front+ new_back)

print(rotate_rightmost_digits(735291, 2) == 735219)  # True
print(rotate_rightmost_digits(735291, 3) == 735912)  # True
print(rotate_rightmost_digits(735291, 1) == 735291)  # True
print(rotate_rightmost_digits(735291, 4) == 732915)  # True
print(rotate_rightmost_digits(735291, 5) == 752913)  # True
print(rotate_rightmost_digits(735291, 6) == 352917)  # True
print(rotate_rightmost_digits(1200, 3) == 1002)      # True