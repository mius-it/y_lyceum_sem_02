food = {
    'жирное': ['плов'],
    'сладкое': ['сахар', 'мед'],
    'мучное': ['печенье'],
    'диетическое': ['творог', 'чай', 'фрукты']
}


def diet(string):
    dishes = string.split(', ')
    diet_dishes_cntr = 0
    for dish in dishes:
        if dish in food['диетическое']:
            diet_dishes_cntr += 1
    if diet_dishes_cntr > len(dishes) / 2:
        return 'Так держать, Воин Дракона!'
    return 'Не ешь столько, По!'


print(diet("творог"))
print(diet("печенье, чай, сахар, фрукты, мед"))