'''
P: input string
    output string with alternating upper and lower case characters
    (ignore spaces) start with upper case
E: 'a dog' -> 'A dOg'
D: none
A: set next_is_upper = True, iterate through chars
    if char is alpha, add upper or lower based on variable,
        alternate variable
    else add char
C: below
'''

def staggered_case(string):
    result = ''
    next_is_upper = True

    for char in string:
        if char.isalpha():
            func = char.upper if next_is_upper else char.lower
            result += func()
            next_is_upper = not next_is_upper
        else:
            result += char

    return result

string = 'I Love Launch School!'
result = "I lOvE lAuNcH sChOoL!"
print(staggered_case(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_cApS"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")          # True