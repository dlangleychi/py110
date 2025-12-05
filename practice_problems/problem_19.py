'''
P: given list of ints, return element that occurs odd number of times, 
    guaranteed to be unique
E: [1,2,1] -> 2
D: none, or count dictionary
A: apply xor to every element, or create count dictionary and find odd
    occuring element
C: below
'''

def odd_fellow(num_list):
    result = 0
    for num in num_list:
        result ^= num
    return result

def odd_fellow(num_list):
    counts = {}
    for num in num_list:
        counts[num] = counts.get(num,0) + 1
    
    for num, count in counts.items():
        if count % 2 == 1:
            return num

print(odd_fellow([4]) == 4)
print(odd_fellow([7, 99, 7, 51, 99]) == 51)
print(odd_fellow([7, 99, 7, 51, 99, 7, 51]) == 7)
print(odd_fellow([25, 10, -6, 10, 25, 10, -6, 10, -6]) == -6)
print(odd_fellow([0, 0, 0]) == 0)