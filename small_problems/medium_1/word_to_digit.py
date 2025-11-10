'''
P: take space seperate string, convert string number to numercials
    return new string, handle punctuation a the end of word,
    assume no more than one punctuation mark
E: 'a one two' -> 'a 1 2'
D: dictionary of string to digit conversion
A: split, loop through making conversions, join
C: below
'''

import string

PUNCTUATION = string.punctuation

STRING_TO_DIGIT = {
    'zero' : '0', 
    'one' : '1', 
    'two' : '2', 
    'three' : '3', 
    'four' : '4', 
    'five' : '5', 
    'six' : '6',
    'seven' : '7',
    'eight' : '8',
    'nine' : '9',
}

def word_to_digit(string):
    string_list = string.split()
    for i ,word in enumerate(string_list):
        if word[-1] in PUNCTUATION:
            word, punctuation = word[:-1], word[-1]
        else:
            punctuation = ''
        word = STRING_TO_DIGIT.get(word, word)
        string_list[i] = word + punctuation
    return ' '.join(string_list)

message = 'Please call me at five five five one two three four'
print(word_to_digit(message) == "Please call me at 5 5 5 1 2 3 4")
# Should print True

message = 'Please call me at five, five, five, one, two, three, four.'
print(word_to_digit(message) == "Please call me at 5, 5, 5, 1, 2, 3, 4.")
# Should print True