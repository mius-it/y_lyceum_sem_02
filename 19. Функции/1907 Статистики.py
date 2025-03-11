def print_average(arr):
    print(sum(arr) / len(arr))


def print_statistics(arr):
    if arr:
        print(len(arr))
        print_average(arr)
        print(min(arr))
        print(max(arr))
        arr.sort()
        la = len(arr)
        if la % 2 == 1:
            print(arr[la // 2])
        else:
            print((arr[la // 2] + arr[la // 2 - 1]) / 2)
    else:
        print(0, 0, 0, 0, 0, sep='\n')

# print_statistics([])
