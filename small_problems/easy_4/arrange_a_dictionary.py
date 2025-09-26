'''
P: input dictionary (assumed all values comparable type),
    output list of keys sorted by corresponding values
E: {'a': 1, 'b': 0} -> ['b', 'a']
D: new list output
A: apply sorted to keys with comparator dictionary.get
C: below
'''

def order_by_value(dictionary):
    return sorted(dictionary.keys(), key=dictionary.get)

my_dict = {'p': 8, 'q': 2, 'r': 6}
keys = ['q', 'r', 'p']
print(order_by_value(my_dict) == keys)  # True