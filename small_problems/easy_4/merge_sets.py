'''
P: input two list, output set of union of all elements
E: [1, 2], [3, 4] -> {1, 3, 2, 4} (for example)
D: new sets created
A: pass lists to set constructor, then apply | operator
C: below
'''

def merge_sets(lst1, lst2):
    return set(lst1) | set(lst2)

list1 = [3, 5, 7, 9]
list2 = [5, 7, 11, 13]
print(merge_sets(list1, list2) == {3, 5, 7, 9, 11, 13})
# Prints True