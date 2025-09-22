'''
P: input list, output list of two lists first half in first
    second half in second, if odd number first list is one larger
    don't alert original
E: [1, 2, 3, 4] -> [[1,2], [3,4]]
D: new list created for output and its two element lists
A: slice with (len + 1) // 2 as the breaking point
C: below
'''

def halvsies(ls):
    split_point = (len(ls) + 1) // 2
    return [ls[:split_point], ls[split_point:]]

# All of these examples should print True
print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
print(halvsies([5]) == [[5], []])
print(halvsies([]) == [[], []])