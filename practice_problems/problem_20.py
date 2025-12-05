'''
P: given list of a least 3 numbers, where all are the same except one,
    return the number which is different
E: [1, 1, 2] -> 2
D: count dictionary
A: iterate through input, record number of times each element occurs,
    iterate through count dictionary, return the element with a count of 1
C: below
'''

def what_is_different(num_list):
    counts = {}
    for num in num_list:
        counts[num] = counts.get(num, 0) + 1

    return min(counts, key=counts.get)


print(what_is_different([0, 1, 0]) == 1)
print(what_is_different([7, 7, 7, 7.7, 7]) == 7.7)
print(what_is_different([1, 1, 1, 1, 1, 1, 1, 11, 1, 1, 1, 1]) == 11)
print(what_is_different([3, 4, 4, 4]) == 3)
print(what_is_different([4, 4, 4, 3]) == 3)