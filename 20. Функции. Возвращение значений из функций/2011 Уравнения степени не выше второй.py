def roots_of_quadratic_equation(a,b,c):
    if a == 0:
        return [] if (b == 0 and c != 0) else (['all'] if b == 0 else [-c / b])

    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return []

    sqrt_d = discriminant ** 0.5
    denominator = 2 * a
    if discriminant == 0:
        return [-b / denominator]

    x1 = (-b + sqrt_d) / denominator
    x2 = (-b - sqrt_d) / denominator
    return [int(x1), int(x2)]


# result = roots_of_quadratic_equation(1, 2, 1)
# print(*sorted(result))
# result = roots_of_quadratic_equation(1, -3, 2)
# print(*sorted(result))