def allocation(sold):
    unsold = []
    for s in sold:
        if places[s[0] - 1][s[1] - 1]:
            unsold.append(s)
        else:
            places[s[0] - 1][s[1] - 1] = 1
    return unsold


places = [[1, 1, 0, 0], [0, 0, 0, 1], [0, 1, 1, 0, 0, 0]]
print('было: ', places)
data = [(2, 3), (1, 4), (3, 1), (2, 3), (3, 3)]
print(allocation(data))
print('стало:', places)