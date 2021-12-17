"""
SEARCH IN MATRIX
--------

You are give a matrix (a list of lists) of DISTINCT integers and a target number.
Each row in the matrix is SORTED and each column in the matrix is SORTED.
Our matrix does not necessarily have the same height and width.

Write a function that returns a list of the row and column indices of the target integer
IF it is contained in the matrix, otherwise return [-1, -1].

EXAMPLE INPUT

matrix = [
[1,4,7,12,15,1000],
[2,5,19,31,32,1001],
[3,8,24,33,35,1002],
[40,41,42,44,45,1003],
[99,100,103,106,128,1004]
]

target =44

EXAMPLE OUTPUT

result = [3,3]

"""
"""
Note to markers:
I was unable to install the maths package from both settings and pip install as it wasn't compatible - I had no idea what that meant and didn't
have time to work it out so I used other methods to do this question.
"""




# def search_in_matrix(matrix, target):
#     rows = len(matrix)
#     cols = len(matrix[0])
#     row_idx = int(rows/2)
#     cols_idx = int(cols/2)
#     while matrix[row_idx][cols_idx] != target:
#         while row_idx >= 0:
#             if target < matrix[row_idx][cols_idx]:
#                 row_idx -= 1
#                 while matrix[row_idx][cols_idx] != target:
#                     if target < matrix[row_idx][cols_idx]:
#                         cols_idx -= 1
#                         if cols_idx < 0:
#                             break
#                     if target > matrix[row_idx][cols_idx]:
#                         cols_idx += 1
#                         if cols_idx > cols:
#                             break
#         while row_idx <= rows:
#             if target > matrix[row_idx][cols_idx]:
#                 row_idx += 1
#                 while matrix[row_idx][cols_idx] != target:
#                     if target < matrix[row_idx][cols_idx]:
#                         cols_idx -= 1
#                         if cols_idx < 0:
#                             break
#                     if target > matrix[row_idx][cols_idx]:
#                         cols_idx += 1
#                         if cols_idx > cols:
#                             break
#         while cols_idx >= 0:
#             if target < matrix[row_idx][cols_idx]:
#                 cols_idx -= 1
#                 while matrix[row_idx][cols_idx] != target:
#                     if target < matrix[row_idx][cols_idx]:
#                         row_idx -= 1
#                         if row_idx < 0:
#                             break
#                     if target > matrix[row_idx][cols_idx]:
#                         row_idx += 1
#                         if row_idx > rows:
#                             break
#         while cols_idx <= cols:
#             if target > matrix[row_idx][cols_idx]:
#                 cols_idx += 1
#                 while matrix[row_idx][cols_idx] != target:
#                     if target < matrix[row_idx][cols_idx]:
#                         row_idx -= 1
#                         if row_idx < 0:
#                             break
#                     if target > matrix[row_idx][cols_idx]:
#                         row_idx += 1
#                         if row_idx > rows:
#                             break
#     return [row_idx, cols_idx]

# test case
matrix = [
[1,4,7,12,15,1000],
[2,5,19,31,32,1001],
[3,8,24,33,35,1002],
[40,41,42,44,45,1003],
[99,100,103,106,128,1004]
]
# result = [3,3]

target = 24

def search_in_matrix(matrix, target):
    rows = len(matrix)
    cols = len(matrix[0])
    row_idx = int(rows/2)
    cols_idx = int(cols/2)
    while matrix[row_idx][cols_idx] != target:
        if target < matrix[row_idx][cols_idx] and row_idx >= 0:
            row_idx -= 1
            while matrix[row_idx][cols_idx] != target:
                if target < matrix[row_idx][cols_idx] and cols_idx >= 0:
                    cols_idx -= 1
                if target > matrix[row_idx][cols_idx] and cols_idx <= cols:
                    cols_idx += 1
        if target < matrix[row_idx][cols_idx] and cols_idx >= 0:
            cols_idx -= 1
            while matrix[row_idx][cols_idx] != target:
                if target < matrix[row_idx][cols_idx] and row_idx >= 0:
                    row_idx -= 1
                if target > matrix[row_idx][cols_idx] and row_idx <= rows:
                    row_idx += 1
        if target > matrix[row_idx][cols_idx] and row_idx <= rows:
            row_idx += 1
            while matrix[row_idx][cols_idx] != target:
                if target < matrix[row_idx][cols_idx] and cols_idx >= 0:
                    cols_idx -= 1
                if target > matrix[row_idx][cols_idx] and cols_idx <= cols:
                    cols_idx += 1
        if target > matrix[row_idx][cols_idx] and cols_idx <= cols:
            cols_idx += 1
            while matrix[row_idx][cols_idx] != target:
                if target < matrix[row_idx][cols_idx] and row_idx >= 0:
                    row_idx -= 1
                if target > matrix[row_idx][cols_idx] and row_idx <= rows:
                    row_idx += 1
    return [row_idx, cols_idx]

print(search_in_matrix(matrix, target))

# def search_in_matrix(matrix, target):
#     rows = len(matrix)
#     cols = len(matrix[0])
#     row_idx = int(rows/2)
#     cols_idx = int(cols/2)
#     while matrix[row_idx][cols_idx] != target:
#         if matrix[row_idx][cols_idx] != target:
#             while matrix[row_idx][cols_idx] != target:
#                 if target < matrix[row_idx][cols_idx]:
#                     row_idx -= 1
#                     while matrix[row_idx][cols_idx] != target:
#                         if target < matrix[row_idx][cols_idx]:
#                             cols_idx -= 1
#                 if target > matrix[row_idx][cols_idx]:
#                     row_idx += 1
#                     while matrix[row_idx][cols_idx] != target:
#                         if target > matrix[row_idx][cols_idx]:
#                             cols_idx += 1
#     return [row_idx, cols_idx]



