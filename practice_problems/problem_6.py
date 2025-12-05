'''
P: give a string, return a dictionary of lower case occurences
E: 'ABc' -> {'c': 1}
D: dictionary for answer
A: loop through string recording occurence if character is lowercase
C: below
'''

def count_letters(string):
    result = {}
    for char in string:
        if char.islower():
            result[char] = result.get(char, 0) + 1
    
    return result

expected = {'w': 1, 'o': 2, 'e': 3, 'b': 1, 'g': 1, 'n': 1}
print(count_letters('woebegone') == expected)

expected = {'l': 1, 'o': 1, 'w': 1, 'e': 4, 'r': 2,
            'c': 2, 'a': 2, 's': 2, 'u': 1, 'p': 2}
print(count_letters('lowercase/uppercase') == expected)

expected = {'u': 1, 'o': 1, 'i': 1, 's': 1}
print(count_letters('W. E. B. Du Bois') == expected)

print(count_letters('x') == {'x': 1})
print(count_letters('') == {})
print(count_letters('!!!') == {})