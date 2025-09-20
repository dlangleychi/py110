'''
P: input string, return boolean of whether string is palindrome
ignoring non alphanumeric character and case
E: 'Madam' -> True, 'Madam, I'm Adam' -> True
D: none
A: create test string with all lowercase and without non 
alphanumeric characters, apply is_palindrome to test string
C: below
'''

def is_palindrome(string):
    return string == string[::-1]

def convert_string(string):
    result = ''
    for char in string:
        if char.isalnum():
            result += char.casefold()

    return result

def is_real_palindrome(string):
    return is_palindrome(convert_string(string))

print(is_real_palindrome('madam') == True)           # True
print(is_real_palindrome('356653') == True)          # True
print(is_real_palindrome('356635') == False)         # True
print(is_real_palindrome('356a653') == True)         # True
print(is_real_palindrome('123ab321') == False)       # True

# case doesn't matter
print(is_real_palindrome('Madam') == True)           # True

# only alphanumerics matter
print(is_real_palindrome("Madam, I'm Adam") == True) # True