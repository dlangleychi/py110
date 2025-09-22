'''
P: input two lists output set of union, don't alter inputs
E: [1, 3, 5], [3, 6, 9] -> {1,3,5, 6, 9}
D: create new set for output
A: pass combination of lists to set constructor
C: below
'''

def union(list1, list2):
    return set(list1 + list2)

print(union([1, 3, 5], [3, 6, 9]) == {1, 3, 5, 6, 9}) # True