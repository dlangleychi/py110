'''
There a name collision between sum the defined function and sum the
built-in function.  Change the name of the defined function to 
multiply_sum.
'''

def multipy_sum(numbers, factor): #
    return factor * sum(numbers)

numbers = [1, 2, 3, 4]
print(multipy_sum(numbers, 2) == 20)