'''
P: given a string, return the most common character,
    case-insensitive, and break ties by first occurence
E: 'ab' -> 'a'
D: dictionary for occurences (will keep order)
A: loop through string incrementing dictionary of counts
C: below
'''

def most_common_char(string):
    counts = {}
    for char in string:
        if char.isalpha():
            counts[char.lower()] = counts.get(char.lower(), 0) + 1

    result = None
    for char, count in counts.items():
        if result is None or count > counts[result]:
            result = char

    return result

print(most_common_char('Hello World') == 'l')
print(most_common_char('Mississippi') == 'i')
print(most_common_char('Happy birthday!') == 'h')
print(most_common_char('aaaaaAAAA') == 'a')

my_str = 'Peter Piper picked a peck of pickled peppers.'
print(most_common_char(my_str) == 'p')

my_str = 'Peter Piper repicked a peck of repickled peppers. He did!'
print(most_common_char(my_str) == 'e')