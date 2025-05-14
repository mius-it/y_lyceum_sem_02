fractal = [0, 2]


def fill_fractal():
    fractal.insert(len(fractal) // 2, fractal)


print(fractal)
fill_fractal()
fill_fractal()
print(fractal)
