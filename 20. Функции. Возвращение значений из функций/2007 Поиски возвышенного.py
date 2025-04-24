def find_mountain(heightsMap):
    row = 0
    col = 0
    maxh = 0
    for i in range(len(heightsMap)):
        for j in range(len(heightsMap[i])):
            if heightsMap[i][j] > maxh:
                maxh = heightsMap[i][j]
                row = i
                col = j
    return row, col


'''
a = [[1, 3, 1], [3, 2, 5], [2, 2, 2]]
print(find_mountain(a))

a = [[2, 4, 2, 3, 2], [3, 2, 3, 4, 3]]
row, col = find_mountain(a)
print(a[row][col])
'''