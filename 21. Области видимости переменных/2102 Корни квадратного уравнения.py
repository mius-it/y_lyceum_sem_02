def larger_root(p, q):
    d = discriminant(1, p, q)
    if d == 0:
        return (-1) * p / 2
    x1 = ((-1) * p + d ** 0.5) / 2
    x2 = ((-1) * p - d ** 0.5) / 2
    return max(x1, x2)


def smaller_root(p, q):
    d = discriminant(1, p, q)
    if d == 0:
        return (-1) * p / 2
    x1 = ((-1) * p + d ** 0.5) / 2
    x2 = ((-1) * p - d ** 0.5) / 2
    return min(x1, x2)


def discriminant(a, b, c):
    return b ** 2 - 4 * a * c


def main():
    p = float(input('Input p: '))
    q = float(input('Input q: '))
    print(discriminant(1, p, q))
    print(smaller_root(p, q), larger_root(p, q))

# print(smaller_root(2, 1))
# print(larger_root(2, 1))
# print(discriminant(1, 2, 1))
# main()
