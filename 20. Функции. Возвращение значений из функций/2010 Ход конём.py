def make_coords_tuple(coords_string):
    return ord(coords_string[0]) - 64, int(coords_string[1])


def make_coords_string(coords_tup):
    return chr(coords_tup[0] + 64) + str(coords_tup[1])


def is_on_field(coords_tup):
    return (0 < coords_tup[0] <= 8) and (0 < coords_tup[1] <= 8)


def possible_turns(cell):
    cell_tup = make_coords_tuple(cell)
    if not is_on_field(cell_tup):
        return 'Клетка вне поля'
    knight_landing_tup = list()
    knight_landing_str = list()
    knight_moves = [
        (2, 1), (2, -1),
        (-2, 1), (-2, -1),
        (1, 2), (1, -2),
        (-1, 2), (-1, -2)
    ]
    for dx, dy in knight_moves:
        knight_landing_tup.append((cell_tup[0] + dx, cell_tup[1] + dy))
    for tup in knight_landing_tup:
        if is_on_field(tup):
            knight_landing_str.append(make_coords_string(tup))
    return knight_landing_str


# print(possible_turns("B1"))
# print(possible_turns("H8"))
# print(possible_turns("B9"))
# print(possible_turns("Z1"))
# print(possible_turns("A2"))
