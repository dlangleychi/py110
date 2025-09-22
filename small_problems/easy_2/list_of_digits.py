'''
P: input positve int, return list of integer digits
E: 12345 -> [1, 2, 3, 4, 5]
D: new list for output
A: 
1. initialize result
2. while input > 0
    insert at zero position input % 10
    input quotient equal 10
3. return result
C: below
'''

def digit_list(pos_int):
    result = []

    while pos_int:
        result.insert(0, pos_int % 10)
        pos_int //= 10

    return result

def digit_list(pos_int):
    return [int(digit) for digit in str(pos_int)]

print(digit_list(12345) == [1, 2, 3, 4, 5])       # True
print(digit_list(7) == [7])                       # True
print(digit_list(375290) == [3, 7, 5, 2, 9, 0])   # True
print(digit_list(444) == [4, 4, 4])               # True