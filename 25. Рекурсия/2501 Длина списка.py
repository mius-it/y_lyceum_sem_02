def recursive_len(some_list):
    if not some_list:
        return 0
    return 1 + recursive_len(some_list[1:])

data = [1, 2, 5, 2]
print(recursive_len(data))
print(*data)
