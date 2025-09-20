'''
P: input string, return dict or word size frequency, omitting
non alphanumeric characters
E: 'Four score and seven.' -> {4: 1, 5: 2, 3: 1}
D: none
A: create helper to count alnum characters, loop through
populating dictionary of word size frequencies
C: below
'''

def alpha_count(word):
    result = 0
    for char in word:
        result += char.isalpha()
    return result

def word_sizes(string):
    result_dict = {}
    for word in string.split():
        word_size = alpha_count(word)        
        result_dict[word_size] = result_dict.get(word_size, 0) + 1
    return result_dict

# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 2, 3: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 3})

string = 'Humpty Dumpty sat on a w@ll'
print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})

string = "What's up doc?"
print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

print(word_sizes('') == {})