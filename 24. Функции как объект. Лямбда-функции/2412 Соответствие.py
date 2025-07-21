def trend(*dat, **func):
    # print('dat:', list(dat))
    # print('func:', func)
    scores = {}
    for f in func:
        scores[f] = 0
    for d in dat:
        for f in func:
            # print(f, ':', func[f](d[0]), '=', d[1])
            if d[1] - 0.01 <= func[f](d[0]) <= d[1] + 0.01:
                scores[f] += 1
    # print(scores)
    for s in scores:
        # print(s, ' - ', scores[s])
        if scores[s] == len(dat):
            return s
    else:
        return 'None'


# data = [(0, 0), (-1.0, 1.001), (3.0, 8.999), (-2.0, 4.0)]
# functions = {"line": lambda x: 3 * x,
#              "square": lambda x: x ** 2,
#              "cube": lambda x: 0.5 * x ** 3}
# print(trend(*data, **functions))
#
# print('--------------------')
#
#
# data = [(0, 0), (-1.0, -3.001), (3.0, 9.0), (-2.0, 6.0)]
# functions = {"line": lambda x: 3 * x,
#              "square": lambda x: x ** 2,
#              "cube": lambda x: 0.5 * x ** 3}
# print(trend(*data, **functions))
