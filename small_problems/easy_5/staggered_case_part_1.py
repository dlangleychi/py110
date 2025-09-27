'''
P: input string
    output string with alternating uppercase and lower case
    (spaces and punctuation count), start with upper case
E: 'dog' -> 'DoG'
D: none
A: iterate through index and characters adding to result
    if index is even apply upper, if odd apply lower
C: below
'''

def staggered_case(string):
    result = ''
    for idx, char in enumerate(string):
        if idx % 2 == 0:
            result += char.upper()
        else:
            result += char.lower()

    return result

def staggered_case(string):
    result = ''
    for idx, char in enumerate(string):
        func = char.upper if idx % 2 == 0 else char.lower
        result += func()

    return result

string = 'I Love Launch School!'
result = "I LoVe lAuNcH ScHoOl!"
print(staggered_case(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_CaPs"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")          # True