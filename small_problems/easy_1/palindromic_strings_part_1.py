'''
P: input string, outputs boolean of whether input is palindrome
E: 'madam' -> True, '356635' -> False
D: none
A: two pointer; front and back of string iterate till they meet or
point to unequal characters, meeting -> True, unequal -> False
C: below
'''

def is_palindrome(string):
    i, j = 0, len(string) - 1

    while i < j:
        if string[i] != string[j]:
            return False
        i += 1
        j -= 1

    return True

def is_palindrome(string):
    return string == string[::-1]

# All of these examples should print True

print(is_palindrome('madam') == True)
print(is_palindrome('356653') == True)
print(is_palindrome('356635') == False)

# case matters
print(is_palindrome('Madam') == False)

# all characters matter
print(is_palindrome("madam i'm adam") == False)