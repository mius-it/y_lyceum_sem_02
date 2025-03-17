def squared(a, b, k):
    for i in range(a, b + 1):
        x = i ** 2
        if x % k:
            print(f"{x:<4}", end=' ')
        if i % 10 == a % 10 - 1:
            print()


squared(11, 99, 10)
# squared(4, 33, 9)
