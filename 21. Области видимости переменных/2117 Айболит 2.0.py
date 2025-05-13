base = ["Иван", "Юлия Иванкова"]
query = [None, None, None]


def hello(name):
    global query
    for i in range(len(query)):
        if query[i] == None:
            print(f'Здравствуйте, {name}! Подойдите к окошку номер {i + 1}')
            query[i] = name
            break
    else:
        print(f'Простите, {name}. Все окна заняты')


def search_card(name):
    if name in query:
        for i in range(len(base)):
            if name == base[i]:
                print(f'Ваша карта с номером {i + 1} найдена')
                break
        else:
            print('Ваша карта не найдена')
    else:
        print(f'Простите, {name}, дождитесь своей очереди')


def good_bye(name):
    global query
    for i in range(len(query)):
        if query[i] == name:
            query[i] = None
            print(f'До свидания, не болейте, {name}')
            break
    else:
        print(f'Простите, {name}, дождитесь своей очереди')


# hello("Иван")
# search_card("Иван")
# hello("Юлия Иванова")
# hello("Иван2")
# search_card("Юлия Иванова")
# hello("Иван3")
# search_card("Иван3")
# hello("Иван4")
# good_bye("Юлия Иванова")
# hello("Иван3")
# search_card("Иван3")
