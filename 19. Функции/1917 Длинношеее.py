def print_long_words(text):
    text = (text.lower().replace(',', '').replace('.','').replace(';','').
             replace(' - ', ' ').replace(' – ', ' '))
    words = text.split()
    voc_ru = ['а', 'о', 'э', 'и', 'у', 'ы', 'е', 'ё', 'ю', 'я']
    voc_en = ['a', 'e', 'i', 'o', 'u', 'y']
    for w in words:
        cntr = 0
        for v in voc_ru:
            cntr += w.count(v)
        for v in voc_en:
            cntr += w.count(v)
        if cntr > 3:
            print(w)


# print_long_words('Как и в прочих заданиях этого урока, в вашем решении функция должна быть определена, но не должна вызываться.')
