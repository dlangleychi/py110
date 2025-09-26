'''
P: input two lists, output frozenset of intersection
E: [1, 2], [2, 3] -> frozenset({2})
D: new frozenset for output
A: frozenset constructors and & operator
C: below
'''

def intersection(list1, list2):
    return frozenset(list1) & frozenset(list2)

list1 = [2, 4, 6, 8]
list2 = [1, 3, 5, 7, 8]
expected_result = frozenset({8})
print(intersection(list1, list2) == expected_result) # True