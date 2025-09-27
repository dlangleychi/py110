'''
We made a shallow copy.  The copied list elements are the sames lists
as the original.  To solve the problem make deepcopy.
'''

import copy

original = [[1], [2], [3]]
copied = copy.deepcopy(original) #

original[0][0] = 99

print(copied[0] == [1])