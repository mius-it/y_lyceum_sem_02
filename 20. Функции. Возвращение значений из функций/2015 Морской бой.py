def transpose(matrix):
    lm = len(matrix)
    row = []
    res = []
    for i in range(lm):
        for j in range(lm):
            row.append(matrix[j][i])
        res.append(row.copy())
        row.clear()
    return res


def flip_h(matrix):
    res = []
    for m in matrix:
        mr = m[::-1]
        res.append(mr)
    return res


def flip_v(matrix):
    return matrix[::-1]


fields = list()
origin = [['x', 'x', 'x', '.'],
          ['.', '.', '.', '.'],
          ['x', '.', 'x', 'x'],
          ['x', '.', '.', '.']]
fields.append(origin)
fields.append(flip_h(origin))
fields.append(flip_v(origin))
fields.append(transpose(origin))
fields.append(flip_h(flip_v(origin)))
fields.append(flip_v(transpose(origin)))
fields.append(flip_v(flip_h(transpose(origin))))

for f in fields:
    for ff in f:
        print(ff)
    print('--------------------')
