def tribonacci(n):
    trib = []
    if n == 0:
        return 'Число должно быть больше 0'
    if n > 0:
        trib.append(0)
    if n > 1:
        trib.append(0)
    if n > 2:
        trib.append(1)
    if n > 3:
        pass
    return trib


print(tribonacci(3))