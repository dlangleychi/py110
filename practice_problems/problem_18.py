'''
P: given a list of number, return index such that sum before equals
sum after, if multiple indexes return first
E: [1, 2, 4, 4, 2, 3, 2] -> 3
D: none
A: calculate the sum of the whole, iterate through keeping a running sum,
    if the runing sum = whole sum - running sum - current element return
    index, if we make it to the end return -1
C: below
'''

def equal_sum_index(ls):
    total_sum = sum(ls)
    running_sum = 0
    for idx, num in enumerate(ls):
        if running_sum == total_sum - running_sum - num:
            return idx
        running_sum += num
    return -1

print(equal_sum_index([1, 2, 4, 4, 2, 3, 2]) == 3)
print(equal_sum_index([7, 99, 51, -48, 0, 4]) == 1)
print(equal_sum_index([17, 20, 5, -60, 10, 25]) == 0)
print(equal_sum_index([0, 2, 4, 4, 2, 3, 2]) == -1)

# The following test case could return 0 or 3. Since we're
# supposed to return the smallest correct index, the correct
# return value is 0.
print(equal_sum_index([0, 20, 10, -60, 5, 25]) == 0)