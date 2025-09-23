'''
P: input string, output string with consonants repeated, 
    other chars unchanged
E: 'String' -> 'SSttrrinngg'
D: none
A: join comprehension with conditional in expression
C: below
'''

CONSONANTS = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'

def double_consonants(string):
    return ''.join(char * 2 if char in CONSONANTS \
        else char for char in string)

# All of these examples should print True
print(double_consonants('String') == "SSttrrinngg")
print(double_consonants('Hello-World!') == "HHellllo-WWorrlldd!")
print(double_consonants('July 4th') == "JJullyy 4tthh")
print(double_consonants('') == "")