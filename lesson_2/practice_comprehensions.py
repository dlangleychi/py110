# 1

munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}

total_male_age = 0

for data in munsters.values():
    if data['gender'] == 'male':
        total_male_age += data['age']

# print(total_male_age)

# print(sum([data['age'] for data in munsters.values() 
#            if data['gender'] == 'male']))

# 2

lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]

new_lst = []
for sub_lst in lst:
    new_lst.append(sorted(sub_lst))

# print(new_lst)

new_lst = [sorted(sub_lst) for sub_lst in lst]
# print(new_lst)

# 3

lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]

new_lst = [sorted(sub_lst, key=str) for sub_lst in lst]
# print(new_lst)

# 4

lst = [
    ['a', 1],
    ['b', 'two'],
    ['sea', {'c': 3}],
    ['D', ['a', 'b', 'c']]
]

new_dict = {key: value for key, value in lst}

import pprint

# pprint.pprint(new_dict, sort_dicts=False, width=30)

# 5

lst = [[1, 6, 7], [1, 5, 3], [1, 8, 3]]

def odd_sum(lst):
    return sum([num for num in lst if num % 2 == 1])

new_lst = sorted(lst, key=odd_sum)

# print(new_lst)

# 6

lst = [{'a': 1}, {'b': 2, 'c': 3}, {'d': 4, 'e': 5, 'f': 6}]

incr_lst = [{key: value + 1 for key, value in sub_dict.items()} 
            for sub_dict in lst]

# print(incr_lst)

# 7

lst = [[2], [3, 5, 7, 12], [9], [11, 15, 18]]

new_lst = [[num for num in sub_lst if num % 3 == 0] for sub_lst in lst]

# print(new_lst)

def divisible_by_3(lst):
    return [num for num in lst if num % 3 == 0]

new_lst = [divisible_by_3(sub_lst) for sub_lst in lst]

# print(new_lst)

# 8

dict1 = {
    'grape': {
        'type': 'fruit',
        'colors': ['red', 'green'],
        'size': 'small',
    },
    'carrot': {
        'type': 'vegetable',
        'colors': ['orange'],
        'size': 'medium',
    },
    'apricot': {
        'type': 'fruit',
        'colors': ['orange'],
        'size': 'medium',
    },
    'marrow': {
        'type': 'vegetable',
        'colors': ['green'],
        'size': 'large',
    },
}

lst = []

for food_attributes in dict1.values():
    if food_attributes['type'] == 'fruit':
        lst.append([color.capitalize() for color 
                    in food_attributes['colors']])
    elif food_attributes['type'] == 'vegetable':
        lst.append(food_attributes['size'].upper())

# print(lst)

def format_info(data_dict):
    if data_dict['type'] == 'fruit':
        return [color.capitalize() for color in data_dict['colors']]
    return data_dict['size'].upper()

lst = [format_info(food_data) for food_data in dict1.values()]

# print(lst)

# 9

lst = [
    {'a': [1, 2, 3]},
    {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]},
    {'e': [8], 'f': [6, 10]},
]

new_lst = [dictionary for dictionary in lst 
           if all([all([num % 2 == 0 for num in dict_lst]) 
                   for dict_lst in dictionary.values()])]

# print(new_lst)

def list_is_even(lst):
    return all([num % 2 == 0 for num in lst])

def all_lists_even(dictionary):
    return all([list_is_even(sub_lst) 
                for sub_lst in dictionary.values()])

new_lst = [dictionary for dictionary in lst 
           if all_lists_even(dictionary)]

# print(new_lst)

# 10

from random import randint, choice

UUID_PATTERN = [8, 4, 4, 4, 12]

HEX_CHARS = '0123456789abcdef'

def random_hex_digit():
    return hex(randint(0,15))[2:]

def random_hex_number(length):
    return ''.join([random_hex_digit() for _ in range(length)])

def random_UUID():
    return '-'.join([random_hex_number(length) 
                     for length in UUID_PATTERN])

# print(random_UUID())
# print(random_UUID())
# print(random_UUID())

def rand_hex_number(length):
    return ''.join([choice(HEX_CHARS) for _ in range(length)])

def generate_uuid():
    return '-'.join([rand_hex_number(length) 
                     for length in UUID_PATTERN])

# print(generate_uuid())
# print(generate_uuid())
# print(generate_uuid())

# 11

dict1 = {
    'first':  ['the', 'quick'],
    'second': ['brown', 'fox'],
    'third':  ['jumped'],
    'fourth': ['over', 'the', 'lazy', 'dog'],
}

VOWELS = 'aeiou'

list_of_vowels = [char for string_list in dict1.values() 
               for string in string_list 
               for char in string if char in VOWELS]

print(list_of_vowels)
# ['e', 'u', 'i', 'o', 'o', 'u', 'e', 'o', 'e', 'e', 'a', 'o']
