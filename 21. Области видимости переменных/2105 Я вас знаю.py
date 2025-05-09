name = ''


def polite_input(question):
    global name
    while not name:
        name = input('Как вас зовут? ')
    input(f'{name}, {question} ')
#    print(input(f'{name}, {question} '))


# age = polite_input('укажите возраст')
# school_number = polite_input('укажите номер школы')
# class_num = polite_input('укажите полный номер класса')
