'''
Understand the Problem:

input: list of strings
output: new list of strings sorted by highest number adjacent consonants

explicit:
    strings can have spaces
    original order should be retained in case of ties

implicit:
    spaces don't matter 'd f' is adjacent consonants
    function produces new list, not side effects
    
questions:
    what to do about punctuation?
    is 'y' a consonant?
    is sort ascending or descending?
    what exactly does highest adjacent consonant count mean?

'''

'''
Examples and test cases:

- contradicts this is a side effect function, returns new list
- 'y' is still a question, assume it's consonants
- confirms space are ignored
- punctuation, number, etc ... not covered
- empty is not covered, assume it counts as zeron adjacent consonants
- sort is descending order
- single consonants aren't counted

'''

'''
Data Structures:

I'm going to use built in sorted method with custom comparison applied to
original list, so only a new list will be required.

'''

'''
Algorithm:

1. Create new sorted list using built-in sorted method with custom 
comparitor, count_max_adjacent_consonants and set ascending to 
false.

count_max_adjacent_consonants sub-algorithm:

1. initialize a result value to zero
2. initialize adjacent_count to zero
3. create character_string with not spaces:
4. iterate through character_string
    if consonant, increment adjacent_count
        result = max(result, adjacent_count)
    else, adjacent_count = 0
5. if result <= 1 return 0
    else return result

'''

VOWELS = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

def count_max_adjacent_consonants(string):
    result = 0
    adjacent_consonant_count = 0
    character_string = string.replace(' ', '')
    
    for char in character_string:
        if char not in VOWELS:
            adjacent_consonant_count += 1
            result = max(result, adjacent_consonant_count)
        else:
            adjacent_consonant_count = 0

    if result <= 1:
        return 0
    return result

print(count_max_adjacent_consonants('dddaa'))       # 3
print(count_max_adjacent_consonants('ccaa'))        # 2
print(count_max_adjacent_consonants('baa'))         # 0
print(count_max_adjacent_consonants('aa'))          # 0
print(count_max_adjacent_consonants('rstafgdjecc')) # 4

def sort_by_consonant_count(string_list):
    return sorted(
        string_list, 
        key=count_max_adjacent_consonants, 
        reverse=True,
    )

my_list = ['aa', 'baa', 'ccaa', 'dddaa']
print(sort_by_consonant_count(my_list))
# ['dddaa', 'ccaa', 'aa', 'baa']

my_list = ['can can', 'toucan', 'batman', 'salt pan']
print(sort_by_consonant_count(my_list))
# ['salt pan', 'can can', 'batman', 'toucan']

my_list = ['bar', 'car', 'far', 'jar']
print(sort_by_consonant_count(my_list))
# ['bar', 'car', 'far', 'jar']

my_list = ['day', 'week', 'month', 'year']
print(sort_by_consonant_count(my_list))
# ['month', 'day', 'week', 'year']

my_list = ['xxxa', 'xxxx', 'xxxb']
print(sort_by_consonant_count(my_list))
# ['xxxx', 'xxxb', 'xxxa']

