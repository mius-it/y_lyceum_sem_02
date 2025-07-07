def trend(*dat, **func):
    print(list(dat))
    print(func)
    for f in func:
        for d in dat:
            print(f, ':', f(d[0]), '=', d[1])


data = [(0, 0), (-1.0, 1.001), (3.0, 8.999), (-2.0, 4.0)]
functions = {"line": lambda x: 3 * x,
             "square": lambda x: x ** 2,
             "cube": lambda x: 0.5 * x ** 3}
print(trend(*data, **functions))

print('--------------------')


data = [(0, 0), (-1.0, -3.001), (3.0, 9.0), (-2.0, 6.0)]
functions = {"line": lambda x: 3 * x,
             "square": lambda x: x ** 2,
             "cube": lambda x: 0.5 * x ** 3}
print(trend(*data, **functions))

