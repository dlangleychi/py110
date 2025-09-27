'''
P: input two integer lists, same length (assume non-empty)
    output list of element-wise products
E: [1, 2], [3, 4] -> [3, 8]
D: output list
A: list comprehension of product iterating over zip of inputs
C: below
'''

def multiply_items(lst1, lst2):
    return [val1 * val2 for val1, val2 in zip(lst1, lst2)]

list_a = [1, 2, 3]
list_b = [4, 5, 6]
print(multiply_items(list_a, list_b) == [4, 10, 18]) # True