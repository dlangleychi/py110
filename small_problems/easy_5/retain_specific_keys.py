'''
P: input dictionary and key list
    output dictionary with keys in that list
E: {'a': 1, 'b': 2}, ['a'] -> {'a': 1}
D: output dictionary
A: dictionary comprehension with filter
C: below
'''

def keep_keys(input_dict, keys):
    return {
        key: value 
        for key, value in input_dict.items() 
        if key in keys
    }

def keep_keys(input_dict, keys):
    return {
        key : input_dict[key]
        for key in keys
        if key in input_dict
    }

input_dict = {
    'red': 1,
    'green': 2,
    'blue': 3,
    'yellow': 4,
}

keys = ['red', 'blue']
expected_dict = {'red': 1, 'blue': 3}
print(keep_keys(input_dict, keys) == expected_dict) # True