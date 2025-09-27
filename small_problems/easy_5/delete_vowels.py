'''
P: input list of strings
    output list of strings with vowels deleted
E: ['dog', 'cat'] -> ['dg', 'ct']
D: ouput list
A: helper function that deletes vowels for word,
    list comprehension applies it to string list
C: below
'''

VOWELS = 'aeiouAEIOU'

def remove_string_vowels(string):
    return ''.join([char for char in string if char not in VOWELS])

def remove_vowels(string_list):
    return [remove_string_vowels(string) for string in string_list]

# All of these examples should print True
original = ['abcdefghijklmnopqrstuvwxyz']
expected = ['bcdfghjklmnpqrstvwxyz']
print(remove_vowels(original) == expected)        # True

original = ['green', 'YELLOW', 'black', 'white']
expected = ['grn', 'YLLW', 'blck', 'wht']
print(remove_vowels(original) == expected)        # True

original = ['ABC', 'AEIOU', 'XYZ']
expected = ['BC', '', 'XYZ']
print(remove_vowels(original) == expected)        # True