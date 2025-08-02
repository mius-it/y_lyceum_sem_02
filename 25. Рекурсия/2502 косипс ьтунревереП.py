def recursive_reverse(some_list):
    if not some_list:
        return []
    return recursive_reverse(some_list[1:]) + [some_list[0]]




# reversed_list = recursive_reverse([1, 2, 3])
# print(*reversed_list)
#
# print('-----------------')
#
# reversed_list = recursive_reverse([1, 2, 3])
# print(*reversed_list)
# reversed_list = recursive_reverse([4, 5])
# print(*reversed_list)
