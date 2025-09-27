'''
item is assigned to the list element and multiplied by 2
but it is assinged to a list element
'''

def multiply_list(lst):
    for idx in range(len(lst)): #
        lst[idx] *= 2 #

    return lst

print(multiply_list([1, 2, 3]) == [2, 4, 6])