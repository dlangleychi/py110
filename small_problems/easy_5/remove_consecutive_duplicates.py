'''
P: input sequence of integers
    output list where same value successively is only one occurence
E: [1, 1, 2, 2, 2, 3] -> [1, 2, 3]
D: output list
A: iterate index value
    if index is zero of input[index - 1] is not value
        append to result
C: below
'''

def unique_sequence(sequence):
    result = []
    for idx, integer in enumerate(sequence):
        if (idx == 0) or (sequence[idx - 1] != integer):
            result.append(integer)

    return result

def unique_sequence(sequence):
    return [integer for idx, integer in enumerate(sequence) 
            if idx == 0 or integer != sequence[idx - 1]]

original = [1, 1, 2, 6, 6, 6, 5, 5, 3, 3, 3, 4]
expected = [1, 2, 6, 5, 3, 4]
print(unique_sequence(original) == expected)      # True