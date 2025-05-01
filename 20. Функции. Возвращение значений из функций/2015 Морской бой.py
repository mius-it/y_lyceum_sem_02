def transpose(matrix):
    res = []
    lm = len(matrix)
    for i in range(lm - 1, -1, -1):
        res.append(matrix[i].reverse())
    return res


def flip_h(matrix):
    res = []
    for m in matrix:
        print('m = ', m)
        mr = m[::-1]
        print('mr = ', mr)
        res.append(mr)
    return res


def flip_v(matrix):
    return matrix[::-1]


fields = list()
origin = [['x', 'x', 'x', '.'],
['.', '.', '.', '.'],
['x','.','x','x'],
['x','.','.','.']]
fields.append(origin)
fields.append(flip_h(origin))
fields.append(flip_v(origin))
fields.append(transpose(origin))

for f in fields:
    print(f)
