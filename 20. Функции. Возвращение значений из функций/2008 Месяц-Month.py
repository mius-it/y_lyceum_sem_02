def month_name(num, lang):
    mon_en = ['January', 'February', 'March',
              'April', 'May', 'June',
              'July', 'August', 'September',
              'October', 'November', 'December']
    mon_ru = ['январь', 'февраль', 'март',
              'апрель', 'май', 'июнь',
              'июль', 'август', 'сентябрь',
              'октябрь', 'ноябрь', 'декабрь']
    if lang == 'en':
        return mon_en[num - 1]
    elif lang == 'ru':
        return mon_ru[num - 1]


# print(month_name(3, "en"))
# print(month_name(3, "ru"))
