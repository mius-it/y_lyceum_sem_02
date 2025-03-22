def number_in_english(n):
    if not (1 <= n <= 999):
        return 'Введите число от 1 до 99 включительно'
    n1 = n // 100
    n2 = (n // 10) % 10
    n3 = n % 10
    nstr = ''

    if n1 == 1:
        nstr = 'one hundred'
    elif n1 == 2:
        nstr = 'two hundred'
    elif n1 == 3:
        nstr = 'three hundred'
    elif n1 == 4:
        nstr = 'four hundred'
    elif n1 == 5:
        nstr = 'five hundred'
    elif n1 == 6:
        nstr = 'six hundred'
    elif n1 == 7:
        nstr = 'seven hundred'
    elif n1 == 8:
        nstr = 'eight hundred'
    elif n1 == 9:
        nstr = 'nine hundred'

    if n1 and (n2 or n3):
        nstr += ' and'

    if n2 == 1:
        if n3 == 0:
            nstr += ' ten'
        elif n3 == 1:
            nstr += ' eleven'
        elif n3 == 2:
            nstr += ' twelve'
        elif n3 == 3:
            nstr += ' thirteen'
        elif n3 == 4:
            nstr += ' fourteen'
        elif n3 == 5:
            nstr += ' fifteen'
        elif n3 == 6:
            nstr += ' sixteen'
        elif n3 == 7:
            nstr += ' seventeen'
        elif n3 == 8:
            nstr += ' eighteen'
        elif n3 == 9:
            nstr += ' nineteen'
        return nstr
    elif n2 == 2:
        nstr += ' twenty'
    elif n2 == 3:
        nstr += ' thirty'
    elif n2 == 4:
        nstr += ' fourty'
    elif n2 == 5:
        nstr += ' fifty'
    elif n2 == 6:
        nstr += ' sixty'
    elif n2 == 7:
        nstr += ' seventy'
    elif n2 == 8:
        nstr += ' eighty'
    elif n2 == 9:
        nstr += ' ninety'

    if n3 == 1:
        nstr += ' one'
    elif n3 == 2:
        nstr += ' two'
    elif n3 == 3:
        nstr += ' three'
    elif n3 == 4:
        nstr += ' four'
    elif n3 == 5:
        nstr += ' five'
    elif n3 == 6:
        nstr += ' six'
    elif n3 == 7:
        nstr += ' seven'
    elif n3 == 8:
        nstr += ' eight'
    elif n3 == 9:
        nstr += ' nine'

    return nstr.strip()


# print(number_in_english(999))
