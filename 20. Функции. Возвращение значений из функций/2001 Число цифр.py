def num_digits(number):
    cntr = 0
    while number:
        number //= 10
        cntr += 1
    return cntr


# print(num_digits(15778))
