'''
P: input single-spaced string or words, output string with word
having first and last characters swapped
E: 'Abcde' -> 'ebcdA', 'a' -> 'a'
D: none
A:
1. split words into list
2. apply first_last_swap to each word in list
3. return swapped words joined together
C: below
'''

def swap_first_and_last(word):
    if len(word) == 1:
        return word
    return word[-1] + word[1:-1] + word[0]

def swap(words_string):
    words_list = words_string.split(' ')
    for i in range(len(words_list)):
        words_list[i] = swap_first_and_last(words_list[i])
    return ' '.join(words_list)

print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True