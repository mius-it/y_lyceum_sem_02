def roman():
    global three
    three= one + two
    print(make_roman(one), '+', make_roman(two), '=', make_roman(three))


def make_roman(num):
    if not 1 <= num <= 1000:
        return "Число должно быть от 1 до 1000"

    val = [1000, 900, 500, 400, 100,
           90, 50, 40, 10, 9, 5, 4, 1]
    syms = ["M", "CM", "D", "CD", "C",
            "XC", "L", "XL", "X", "IX", "V", "IV", "I"
    ]

    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syms[i]
            num -= val[i]
        i += 1
    return roman_num

one, two, three = 400, 500, 0
roman()