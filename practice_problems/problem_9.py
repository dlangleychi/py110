'''
P: given a string and substring, return number non-overlapping occurences
E: 'babab', 'bab' -> 1
D: none
A: while loop, count occurences, everytime you get a match leep forward
C: below 
'''

def count_substrings(string, sub):
    result = 0
    m = len(sub)
    n = len(string)
    i = 0
    while i < n - m + 1:
        if string[i: i + m] == sub:
            result += 1
            i += m
        else:
            i += 1

    return result

print(count_substrings('babab', 'bab') == 1)
print(count_substrings('babab', 'ba') == 2)
print(count_substrings('babab', 'b') == 3)
print(count_substrings('babab', 'x') == 0)
print(count_substrings('babab', 'x') == 0)
print(count_substrings('', 'x') == 0)
print(count_substrings('bbbaabbbbaab', 'baab') == 2)
print(count_substrings('bbbaabbbbaab', 'bbaab') == 2)
print(count_substrings('bbbaabbbbaabb', 'bbbaabb') == 1)