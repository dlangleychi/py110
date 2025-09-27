'''
P: input list of numbers (assume nonempty)
    output number sum of sums of each leading sequence
    (leading sequence starts with first elemnent)
E: [3, 5, 2] -> 21
D: list for summing
A: sum list comprehension of leading sums
    iterate of last element
C: below
'''

def sum_of_sums(num_list):
    return sum([sum(num_list[: last + 1]) 
               for last in range(len(num_list))])

def sum_of_sums(num_list):
    result = 0
    prefix_sum = 0
    for num in num_list:
        prefix_sum += num
        result += prefix_sum

    return result

print(sum_of_sums([3, 5, 2]) == 21)               # True
# (3) + (3 + 5) + (3 + 5 + 2) --> 21

print(sum_of_sums([1, 5, 7, 3]) == 36)            # True
# (1) + (1 + 5) + (1 + 5 + 7) + (1 + 5 + 7 + 3) --> 36

print(sum_of_sums([1, 2, 3, 4, 5]) == 35)         # True
# (1) + (1+2) + (1+2+3) + (1+2+3+4) + (1+2+3+4+5) --> 35

print(sum_of_sums([4]) == 4)                      # True
