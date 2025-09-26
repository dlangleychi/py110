'''
P: input two lists, output set of elements in first 
    but not in second
E: [1, 2], [2, 3] -> {1}
D: set created for output
A: apply set constructors then difference operator
C: below
'''

def unique_from_first(list1, list2):
    return set(list1) - set(list2)

list1 = [3, 6, 9, 12]
list2 = [6, 12, 15, 18]
print(unique_from_first(list1, list2) == {9, 3})