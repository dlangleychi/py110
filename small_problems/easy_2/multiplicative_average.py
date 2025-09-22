'''
P: input: list of positive integers (assume non empty)
    output: product divided by len a string with rounded
    to three decimal places, showing three decimal places
E: [3,5] -> '7.500'
D: none
A: take product with loop, return f string with product
    divided by length and correct formating
C: below
'''

def multiplicative_average(int_list):
    product = 1
    
    for num in int_list:
        product *= num

    return f'{product/len(int_list):.3f}'

# All of these examples should print True
print(multiplicative_average([3, 5]) == "7.500")
print(multiplicative_average([2, 5, 8]) == "26.667")
print(multiplicative_average([2, 5]) == "5.000")
print(multiplicative_average([1, 1, 1, 1]) == "0.250")
print(multiplicative_average([2, 5, 7, 11, 13, 17]) == "28361.667")