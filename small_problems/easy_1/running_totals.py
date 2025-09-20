'''
P: input list of numbers, output new list with running totals
E: [2, 5, 13] -> [2, 7, 20], [] -> []
D: none
A:
1. initialize running_total variable as zero
2. loop through list, incrementing running_total and appending it
to result
C: below
'''

def running_total(num_list):
    result = []
    running_sum = 0
    for x in num_list:
        running_sum += x
        result.append(running_sum)
    return result

print(running_total([2, 5, 13]) == [2, 7, 20])    # True
print(running_total([14, 11, 7, 15, 20])
      == [14, 25, 32, 47, 67])                    # True
print(running_total([3]) == [3])                  # True
print(running_total([]) == [])                    # True