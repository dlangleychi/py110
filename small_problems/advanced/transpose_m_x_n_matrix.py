'''
P: given m x n matrix (at least one row and one column), 
    return n x m transpose
E: [[1,2]] -> [[1],[2]]
D: new output matrix
A: find m and n, create n x m output, populate
C: below
'''

def transpose(matrix):
    m, n = len(matrix), len(matrix[0])
    ans = [[None for _ in range(m)] for __ in range(n)]

    for i in range(n):
        for j in range(m):
            ans[i][j] = matrix[j][i]

    return ans

# All of these examples should print True
print(transpose([[1, 2, 3, 4]]) == [[1], [2], [3], [4]])
print(transpose([[1], [2], [3], [4]]) == [[1, 2, 3, 4]])
print(transpose([[1]]) == [[1]])

matrix_3_by_5 = [
    [1, 2, 3, 4, 5],
    [4, 3, 2, 1, 0],
    [3, 7, 8, 6, 2],
]
expected_result = [
    [1, 4, 3],
    [2, 3, 7],
    [3, 2, 8],
    [4, 1, 6],
    [5, 0, 2],
]

print(transpose(matrix_3_by_5) == expected_result)