def catalan(n):
    cn = 1 if n == 0 else 0
    for i in range(n):
        cn += catalan(i) * catalan(n - i - 1)
    return cn


# print(catalan(0))
# print(catalan(1))
# print(catalan(3))
