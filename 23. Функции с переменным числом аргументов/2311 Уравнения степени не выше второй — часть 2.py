def solve(*coefficients):
    coeff_count = len(coefficients)
    if coeff_count == 1:
        return 'all',
    elif coeff_count == 2:
        b, c = coefficients
        x = (0 - c) / b
        return x,
    elif coeff_count == 3:
        a, b, c = coefficients
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
        return [x1, x2]
    else:
        return None,


# print(sorted(solve(1, 2, 1)))
# print(sorted(solve(1, -3, 2)))
# print(sorted(solve(1, -3)))
# print(sorted(solve(1)))
# print(sorted(solve()))
