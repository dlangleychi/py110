'''
P: input string, return dictionary with keys word length
and values frequency, punctuation is counted in length
E: 'Four score and seven.' -> {4: 1, 5: 1, 3: 1, 6: 1}
D: none
A: split string and loop through words, use dict.get to update
frequency in dictionary
C: below
'''

def word_sizes(string):
    result_dict = {}
    for word in string.split():
        result_dict[len(word)] = result_dict.get(len(word), 0) + 1
    return result_dict

# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 1, 3: 1, 6: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 1, 7: 2})

string = 'Humpty Dumpty sat on a wall'
print(word_sizes(string) == {6: 2, 3: 1, 2: 1, 1: 1, 4: 1})

string = "What's up doc?"
print(word_sizes(string) == {6: 1, 2: 1, 4: 1})

print(word_sizes('') == {})