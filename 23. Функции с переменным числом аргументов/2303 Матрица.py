def matrix(n=False, m=False, a=False):
    if n:
        if m:
            if a:
                return [[a] * m] * n
            else:
                return [[0] * m] * n
        else:
            return [[0] * n] * n
    else:
        return [[0]]


# rows = matrix()
# for row in rows:
#      print(*row)
# print('----')
# rows = matrix(2)
# for row in rows:
#      print(*row)
# print('----')
# rows = matrix(3, 4)
# for row in rows:
#      print(*row)
# print('----')
# rows = matrix(5, 8, 'ы')
# for row in rows:
#      print(*row)
# print('----')
