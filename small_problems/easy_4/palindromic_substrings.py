'''
P: input string, output list of palindromic substring,
    case-sensitive and single characters don't count as palindromes
    sorted by order of begining index
E: 'madam' -> ['madam', 'ada']
D: output list
A: make helper is_palindrome, list comprehension over substring
    filtered by is_palindrome
C: below
'''

def substrings_alt(string):
    return [
        string[start:end] 
        for start in range(len(string)) 
        for end in range(start + 1, len(string) + 1)\
    ]

def is_palindrome(string):
    return (len(string) > 1) and (string[::-1] == string)

def palindromes(string):
    return [
        substring 
        for substring in substrings_alt(string) 
        if is_palindrome(substring)
    ]

print(palindromes('abcd') == [])                  # True
print(palindromes('madam') == ['madam', 'ada'])   # True

print(palindromes('hello-madam-did-madam-goodbye') ==
                  [
                      'll', '-madam-', '-madam-did-madam-',
                      'madam', 'madam-did-madam', 'ada',
                      'adam-did-mada', 'dam-did-mad',
                      'am-did-ma', 'm-did-m', '-did-',
                      'did', '-madam-', 'madam', 'ada', 'oo',
                  ])    # True

print(palindromes('knitting cassettes') ==
                  [
                      'nittin', 'itti', 'tt', 'ss',
                      'settes', 'ette', 'tt',
                  ])    # True