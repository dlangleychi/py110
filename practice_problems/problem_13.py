# 11:53
'''
P: given two strings of lowercase characters, 
    return T/F if the second string can be created, from characters in
    the first string
E: 'ab', 'a' -> True
D: two character count dictionaries
A: record character counts for each string, iterate through the second
    string character counts, if the number in string 1 counts is less,
    return False, if you make it to the end return True
'''

def character_counts(string):
    result = {}
    for char in string:
        result[char] = result.get(char, 0) + 1
    return result

def unscramble(string1, string2):
    counts1, counts2 = character_counts(string1), character_counts(string2)
    for char, count in counts2.items():
        if counts1.get(char, 0) < count:
            return False
    return True

print(unscramble('ansucchlohlo', 'launchschool') == True)
print(unscramble('phyarunstole', 'pythonrules') == True)
print(unscramble('phyarunstola', 'pythonrules') == False)
print(unscramble('boldface', 'coal') == True)
print(unscramble('olc', 'cool') == False)