'''
P: input list, output print list elements and number of occurences
    case sensitive
E:
['car', 'car', 'truck', 'car', 'SUV', 'truck',
    'motorcycle', 'motorcycle', 'car', 'truck']
->
car => 4
truck => 3
SUV => 1
motorcycle => 2
D: dictionary for occurences
A: create count dictionary, loop through list, 
    update count with each occurence, iterate through count and 
    print element and ouccrences in desired format

    extra credit: apply casefold method to elements, assume we only get
    string elements
C: below
'''

def count_occurrences(lst):
    count = {}

    for element in lst:
        count[element] = count.get(element, 0) + 1

    print_occurrences(count)

def print_occurrences(count_dict):
    for element, occurrences in count_dict.items():
        print(f'{element} => {occurrences}')

vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
            'motorcycle', 'motorcycle', 'car', 'truck']

count_occurrences(vehicles)

print()

def count_case_insensitive_occurrences(lst):
    count = {}

    for element in lst:
        lower_case_element = element.casefold()
        count[lower_case_element] = count.get(lower_case_element, 0) + 1

    print_occurrences(count)

count_case_insensitive_occurrences(vehicles)