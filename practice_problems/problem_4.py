'''
P: give list of numbers, return the pair which are the closest
    as tuple
E: [12,22,7,17] -> (12,7)
D: none
A: double loop through list, track closest pair
C: below
'''

def closest_numbers(num_list):
    n = len(num_list)
    closest = (num_list[0], num_list[1])
    for i in range(n-1):
        for j in range(i+1, n):
            dist = abs(num_list[i] - num_list[j])
            if dist < abs(closest[0] - closest[1]):
                closest = (num_list[i], num_list[j])
    return closest

print(closest_numbers([5, 25, 15, 11, 20]) == (15, 11))
print(closest_numbers([19, 25, 32, 4, 27, 16]) == (25, 27))
print(closest_numbers([12, 22, 7, 17]) == (12, 7))