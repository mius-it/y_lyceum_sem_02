def defractalize(fractal):
    for i in range(len(fractal) - 1, -1, -1):
        if fractal[i] is fractal:
            fractal.pop(i)

fractal = [2, 5]
fractal.append(fractal)
fractal.append(3)
defractalize(fractal)
print(fractal)

print('-----------------')

fractal = [2, 5]
fractal.append(fractal)
fractal.append(3)
fractal.append(fractal)
fractal.append(9)
defractalize(fractal)
print(fractal)