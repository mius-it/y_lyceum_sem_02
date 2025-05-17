def partial_sums(*args):
    result = [0]
    for i in range(len(args)):
        psum = 0
        for j in range(i + 1):
            psum += args[j]
        result.append(psum)
    return result


# print(partial_sums(13))
#
# print(partial_sums(1, 0.5, 0.25, 0.125))
