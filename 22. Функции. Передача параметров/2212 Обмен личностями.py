def swap(first1, second1):
    global first
    global second
    tmp = first.copy()
    first = second.copy()
    second = tmp.copy()


# first = [1, 2, 3]
# second = [4, 5, 6]
# first_content = first[:]
# second_content = second[:]
# swap(first, second)
# print(first, second_content, first == second_content)
# print(second, first_content, second == first_content)
#
# print('\n----------------------\n')
#
# first = [1, 2, 3]
# second = [4, 5, 6, 7]
# first_content = first[:]
# second_content = second[:]
# swap(first, second)
# print(first, second_content, first == second_content)
# print(second, first_content, second == first_content)
