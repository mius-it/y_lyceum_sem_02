def eratosthenes(N):
    row = [i for i in range(2, N + 1)]
    print(row)
    i, j = 0, 1
    while 1:
        while 1:
            if not row[j] % row[i]:
                print(row.pop(j), end=' ')
            j += 1
            if j >= len(row):
                break
        i += 1
        j = i + 1
        if i >= len(row) - 1:
            break


# eratosthenes(15)
