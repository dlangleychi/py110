'''
P: input string, output string with every character twice
E: 'Hello' -> 'HHeelllloo'
D: none
A: join list comprehension with every char twice
C: below
'''

def repeater(string):
    return ''.join(char * 2 for char in string)

print(repeater('Hello') == "HHeelllloo")              # True
print(repeater('Good job!') == "GGoooodd  jjoobb!!")  # True
print(repeater('') == "")                             # True
