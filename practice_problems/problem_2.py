'''
P: return minimum sum of 5 consecutive entries, or None
    if length is less than 5
E: [1,2,3,5,5,6] -> 16
D: none
A: if len < 5 return None, else iterate through list keeping running min
C: below
'''

def minimum_sum(ls):
    if len(ls) < 5:
        return None
    
    result = sum(ls[:5])
    window_sum = result
    for i in range(5, len(ls)):
        window_sum += ls[i] - ls[i-5]
        result = min(result, window_sum)

    return result

print(minimum_sum([1, 2, 3, 4]) is None)
print(minimum_sum([1, 2, 3, 4, 5, -5]) == 9)
print(minimum_sum([1, 2, 3, 4, 5, 6]) == 15)
print(minimum_sum([55, 2, 6, 5, 1, 2, 9, 3, 5, 100]) == 16)
print(minimum_sum([-1, -5, -3, 0, -1, 2, -4]) == -10)