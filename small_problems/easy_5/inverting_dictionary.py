'''
P: input dictionary with unique keys and values
    output dictionary with values as keys and keys as values
E: {'a': 1} -> {1: 'a'}
D: output dictionary
A: dictionary comprehension with keys and values reversed
C: below
'''

def invert_dict(dictionary):
    return {value: key for key, value in dictionary.items()}

print(invert_dict({
          'apple': 'fruit',
          'broccoli': 'vegetable',
          'salmon': 'fish',
      }) == {
          'fruit': 'apple',
          'vegetable': 'broccoli',
          'fish': 'salmon',
      })  # True