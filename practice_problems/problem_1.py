'''
P: given list return list of how many unique numbers are less than
    each entry
E: [1, 1, 2] -> [0, 0, 1]
D: new list for output
A: make a sorted list of unique numbers, call index in a list 
    comprehension
C: below
'''

def smaller_numbers_than_current(ls):
    unique_sorted = sorted(set(ls))
    return [unique_sorted.index(num) for num in ls]


print(smaller_numbers_than_current([8, 1, 2, 2, 3]) == [3, 0, 1, 1, 2])
print(smaller_numbers_than_current([7, 7, 7, 7]) == [0, 0, 0, 0])
print(smaller_numbers_than_current([6, 5, 4, 8]) == [2, 1, 0, 3])
print(smaller_numbers_than_current([1]) == [0])

my_list = [1, 4, 6, 8, 13, 2, 4, 5, 4]
result   = [0, 2, 4, 5, 6, 1, 2, 3, 2]
print(smaller_numbers_than_current(my_list) == result)