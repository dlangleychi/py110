'''
P: input two equal length non empty lists, output list of all elements
    taken in alteration
E: [1, 2, 3], [4, 5, 6] -> [1, 4, 2, 5, 3, 6]
D: output list
A:
1. initialize result list
2. loop through zip of lists
    append element from first
    append element from second
C: below
'''

def interleave(lst1, lst2):
    result = []

    for element1, element2 in zip(lst1, lst2):
        result.append(element1)
        result.append(element2)

    return result

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
expected = [1, "a", 2, "b", 3, "c"]
print(interleave(list1, list2) == expected)      # True