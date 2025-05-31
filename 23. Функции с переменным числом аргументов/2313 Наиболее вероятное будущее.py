def best_future(*chances):
    jumps = []
    universes_count = len(chances)

    for i in range(universes_count):
        for j in range(i + 1, universes_count):
            if chances[j] < chances[i]:
                jumps.append(j)
                break
        else:
            jumps.append(-1)

    return jumps


# data = [1, 2, 8, 3, 2, 1, 4, 4, 5, 1, 6, 2]
# print(*best_future(*data))
