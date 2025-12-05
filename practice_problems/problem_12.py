# 10:14
'''
P: given string, return True/False of whether it is a pangram,
    case-insensitive
E: 'abc' -> False
D: dictionary for character counts
A: iterate through string, if it's a letter, record in dictionary
    lowercase version, at the end test if dictionary have 26 keys
C: below
'''

def is_pangram(string):
    counts = {}
    for char in string:
        if char.isalpha():
            lower_char = char.lower()
            counts[lower_char] = counts.get(lower_char, 0) + 1

    return len(counts) == 26

print(is_pangram('The quick, brown fox jumps over the lazy dog!') == True)
print(is_pangram('The slow, brown fox jumps over the lazy dog!') == False)
print(is_pangram("A wizard’s job is to vex chumps quickly in fog.") == True)
print(is_pangram("A wizard’s task is to vex chumps quickly in fog.") == False)
print(is_pangram("A wizard’s job is to vex chumps quickly in golf.") == True)

my_str = 'Sixty zippers were quickly picked from the woven jute bag.'
print(is_pangram(my_str) == True)