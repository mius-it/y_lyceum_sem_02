def tic_tac_toe(field):
    print(field)
    size = len(field)
    for row in field:
        if row.count('x') == size:
            return 'x win'
        elif row.count('0') == size:
            return '0 win'
    else:
        for i in range(size):
            row = []
            for j in range(size):
                row.append(field[j][i])
            if row.count('x') == size:
                return 'x win'
            elif row.count('0') == size:
                return '0 win'
        else:
            return 'draw'


data = """0 - x
- 0 x
0 0 x"""

field = [line.split() for line in data.split('\n')]
print(tic_tac_toe(field))
