fractal = []
def fill_fractal():
    global fractal
    tmp = [0, fractal, 2]
    fractal = tmp.copy()
    fill_fractal()


fill_fractal()
