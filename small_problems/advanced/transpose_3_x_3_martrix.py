'''
P: given 3x3 matrix, return new matrix that is transpose of input
E: 1,2,3,4,5,6,7,8,9 -> 1,4,7,2,5,8,3,6,9
D: new output matrix
A: nested list comprehension
C: below
'''

def transpose(matrix):
    return [[matrix[i][j] for i in range(3)] for j in range(3)]

matrix = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]

new_matrix = transpose(matrix)

print(new_matrix == [[1, 4, 3], [5, 7, 9], [8, 2, 6]]) # True
print(matrix == [[1, 5, 8], [4, 7, 2], [3, 9, 6]])     # True