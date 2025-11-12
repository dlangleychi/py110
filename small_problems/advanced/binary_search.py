'''
P: given a stored list and a potential element, using binary search,
    return the elements index or -1
E: [1, 2, 3], 2 -> 1
D: none
A: left and right pointers, mid is their average,
    if ls[mid] == target, return -1
    if ls[mid] < target, left = mid +1
    if ls[mid] > target, right = mid - 1
    if pointers cross return -1
C: below
'''

def binary_search(ls, target):
    left, right = 0, len(ls) - 1
    while left <= right:
        mid = (left + right) // 2
        if ls[mid] == target:
            return mid
        if ls[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# All of these examples should print True
businesses = ['Apple Store', 'Bags Galore', 'Bike Store',
              'Donuts R Us', 'Eat a Lot', 'Good Food',
              'Pasta Place', 'Pizzeria', 'Tiki Lounge',
              'Zooper']
print(binary_search(businesses, 'Pizzeria') == 7)
print(binary_search(businesses, 'Apple Store') == 0)

print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 77) == -1)
print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 89) == 6)
print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 5) == 1)

names = ['Alice', 'Bonnie', 'Kim', 'Pete', 'Rachel', 'Sue',
         'Tyler']
print(binary_search(names, 'Peter') == -1)
print(binary_search(names, 'Tyler') == 6)