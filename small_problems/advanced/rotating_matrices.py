'''
P: given m x n matrix, return 90 degree rotation
E: [[1, 2], [3, 4]] -> [[3, 1], [4, 2]]
D: output matrix
A: apply transpose and then reflect wrt vertical axis = reverese rows
C: below
'''

def transpose(matrix):
    m, n = len(matrix), len(matrix[0])
    ans = [[None for _ in range(m)] for __ in range(n)]

    for i in range(n):
        for j in range(m):
            ans[i][j] = matrix[j][i]

    return ans

def vertical_reflection(matrix):
    return [row[::-1] for row in matrix]

def rotate90(matrix):
    return vertical_reflection(transpose(matrix))

matrix1 = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]

matrix2 = [
    [3, 7, 4, 2],
    [5, 1, 0, 8],
]

new_matrix1 = rotate90(matrix1)
new_matrix2 = rotate90(matrix2)
new_matrix3 = rotate90(rotate90(rotate90(rotate90(matrix2))))

# These examples should all print True
print(new_matrix1 == [[3, 4, 1], [9, 7, 5], [6, 2, 8]])
print(new_matrix2 == [[5, 3], [1, 7], [0, 4], [8, 2]])
print(new_matrix3 == matrix2)