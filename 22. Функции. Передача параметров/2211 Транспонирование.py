def transpose(matrix1):
    global matrix
    tr_matrix, row = [], []
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            row.append(matrix[j][i])
        tr_matrix.append(row.copy())
        row.clear()
    matrix = tr_matrix


# matrix = [[1]]
# transpose(matrix)
# for line in matrix:
#     print(*line)
#
# print('-------------')
#
# matrix = [[1, 2], [3, 4]]
# transpose(matrix)
# for line in matrix:
#     print(*line)
