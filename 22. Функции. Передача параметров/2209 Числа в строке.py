def from_string_to_list(string, container):
    container.extend(int(s) for s in string.split())
    return container


# a = [1, 2, 3]
# from_string_to_list("1 3 99 52", a)
# print(*a)
#
# a = [77, 'abc']
# from_string_to_list("", a)
# print(*a)
