'''
P: input string, output list of all substrings (continuous)
    starting with first character of string, shortest to longest
    no empty string
E: 'abc' -> ['a', 'ab', 'abc']
D: list created for output
A: list comprehension with slicing in output expression
    interator 1 to len
C: below
'''

def leading_substrings(string):
    return [string[:end] for end in range(1, len(string) + 1)]

# All of these examples should print True
print(leading_substrings('abc') == ['a', 'ab', 'abc'])
print(leading_substrings('a') == ['a'])
print(leading_substrings('xyzy') == ['x', 'xy', 'xyz', 'xyzy'])