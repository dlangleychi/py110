'''
P:
    input: nonempty list of positive integers
    output: average of list truncated to integer part
E: [1, 5, 87, 45, 8, 8] -> 25
D: none
A: return quotient of sum input and len input
C: below
'''

def average(int_list):
    return sum(int_list) // len(int_list)

print(average([1, 5, 87, 45, 8, 8]) == 25)        # True
print(average([9, 47, 23, 95, 16, 52]) == 40)     # True
print(average([7]) == 7)                          # True