'''
P: given string, return number of case insensitive characters that
    occurs more than once, only count alphabeticaly and numeric
E: 'aab11' -> 2
D: dictionary for character counts
A: iterate through string, count character occurences in dict 
    if alphanum, case insensitive, iterate through dictionary
    count number of characters that occur more than once
C: below
'''

def distinct_multiples(string):
    counts = {}
    for char in string:
        if char.isalnum():
            counts[char.lower()] = counts.get(char.lower(), 0) + 1
    
    result = 0
    for char, count in counts.items():
        if count > 1:
            result += 1

    return result


print(distinct_multiples('xyz') == 0)               # (none)
print(distinct_multiples('xxyypzzr') == 3)          # x, y, z
print(distinct_multiples('xXyYpzZr') == 3)          # x, y, z
print(distinct_multiples('unununium') == 2)         # u, n
print(distinct_multiples('multiplicity') == 3)      # l, t, i
print(distinct_multiples('7657') == 1)              # 7
print(distinct_multiples('3141592653589793') == 4)  # 3, 1, 5, 9
print(distinct_multiples('2718281828459045') == 5)  # 2, 1, 8, 4, 5