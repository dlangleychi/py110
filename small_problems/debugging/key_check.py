'''
It isn't checking where the key exist, but rather if the key's
value is truthy
'''

# def get_key_value(my_dict, key):
#     if my_dict[key]:
#         return my_dict[key]
#     else:
#         return None

def get_key_value(my_dict, value):
    return my_dict.get(value)

print(get_key_value({"a": 1}, "b"))