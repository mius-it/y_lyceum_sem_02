def number_to_words(n):
    if not (1 <= n <= 99):
        return 'Введите число от 1 до 99 включительно'
    n1 = n // 10
    n2 = n % 10
    nstr = ''

    if n1 == 1:
        if n2 == 0:
            nstr = 'десять'
        elif n2 == 1:
            nstr = 'одиннадцать'
        elif n2 == 2:
            nstr = 'двенадцать'
        elif n2 == 3:
            nstr = 'тринадцать'
        elif n2 == 4:
            nstr = 'четырнадцать'
        elif n2 == 5:
            nstr = 'пятнадцать'
        elif n2 == 6:
            nstr = 'шестнадцать'
        elif n2 == 7:
            nstr = 'семнадцать'
        elif n2 == 8:
            nstr = 'восемнадцать'
        elif n2 == 9:
            nstr = 'девятнадцать'
        return nstr
    else:
        if n2 == 0:
            nstr = ''
        elif n2 == 1:
            nstr = 'один'
        elif n2 == 2:
            nstr = 'два'
        elif n2 == 3:
            nstr = 'три'
        elif n2 == 4:
            nstr = 'четыре'
        elif n2 == 5:
            nstr = 'пять'
        elif n2 == 6:
            nstr = 'шесть'
        elif n2 == 7:
            nstr = 'семь'
        elif n2 == 8:
            nstr = 'восемь'
        elif n2 == 9:
            nstr = 'девять'
    if n1 == 2:
        nstr = 'двадцать ' + nstr
    elif n1 == 3:
        nstr = 'тридцать ' + nstr
    elif n1 == 4:
        nstr = 'сорок ' + nstr
    elif n1 == 5:
        nstr = 'пятьдесят ' + nstr
    elif n1 == 6:
        nstr = 'шестьдесят ' + nstr
    elif n1 == 7:
        nstr = 'семьдесят ' + nstr
    elif n1 == 8:
        nstr = 'восемьдесят ' + nstr
    elif n1 == 9:
        nstr = 'девяносто ' + nstr

    return nstr


# print(number_to_words(450))
