'''
P: given a list of numbers, return number of identical pairs
E: [1, 1, 1] -> 1
D: using a dictionary of counts
A: loop through list recording occurences of each number, loop
    through dictionary adding up values quotient via 2
C: below
'''

def pairs(num_list):
    counts = {}
    for num in num_list:
        counts[num] = counts.get(num, 0) + 1

    result = 0
    for count in counts.values():
        result += count // 2

    return result

print(pairs([3, 1, 4, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7]) == 3)
print(pairs([2, 7, 1, 8, 2, 8, 1, 8, 2, 8, 4]) == 4)
print(pairs([]) == 0)
print(pairs([23]) == 0)
print(pairs([997, 997]) == 1)
print(pairs([32, 32, 32]) == 1)
print(pairs([7, 7, 7, 7, 7, 7, 7]) == 3)