'''
The default lst in function definition points to a specific list.
After lst is modified by the first function call, this same list is 
the default argument in the second function call. So, append_to_list(2)
returns [1, 2].

Default mutable arguments are shared between function calls.
'''

def append_to_list(value, lst=None): #
    if lst is None: #``
        lst = [] #
    lst.append(value)
    return lst

print(append_to_list(1) == [1])
print(append_to_list(2) == [2])