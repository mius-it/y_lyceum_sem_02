def accumulation(*heap):
    sum = 0
    result = []
    result.append(sum)
    for item in heap:
        sum += item
        result.append(sum)
    return result


# data = [1, 2, 3, 4, 5]
# print(*accumulation(*data))
#
# print('---')
#
# data = []
# print(*accumulation(*data))
