'''
P: given string of lowercase letters, return length of longest vowel
    substring
E: 'aate' -> 2
D: none
A: iterate through characters tracking consecutive vowels
C: below
'''

VOWELS = 'aeiou'

def longest_vowel_substring(string):
    result = 0
    starting_vowel = None
    for idx, char in enumerate(string):
        if char in VOWELS:
            if starting_vowel is None:
                starting_vowel = idx
        else:
            if starting_vowel is not None:
                result = max(result, idx - starting_vowel)
                starting_vowel = None
    if starting_vowel is not None:
        result = max(result, len(string) - starting_vowel)
    return result

print(longest_vowel_substring('cwm') == 0)
print(longest_vowel_substring('many') == 1)
print(longest_vowel_substring('launchschoolstudents') == 2)
print(longest_vowel_substring('eau') == 3)
print(longest_vowel_substring('beauteous') == 3)
print(longest_vowel_substring('sequoia') == 4)
print(longest_vowel_substring('miaoued') == 5)