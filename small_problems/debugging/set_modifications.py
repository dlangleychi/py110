'''
The problem is modifing data_set while iterating over it.
Put a list constructor around data_set, that way the iteration sequence
won't be changed by the modification.
'''

data_set = {1, 2, 3, 4, 5}

for item in list(data_set): #
    if item % 2 == 0:
        data_set.remove(item)

data_set = {num for num in data_set if num % 2 != 0}

print(data_set)