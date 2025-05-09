jokes = []


def print_only_new(message):
    if message not in jokes:
        print(message)
        jokes.append(message)


# print_only_new('Шутка номер 15')
# print_only_new('Шутка номер 23')
# print_only_new('Шутка номер 24')
# print_only_new('Шутка номер 24')
# print_only_new('Шутка номер 100')
# print_only_new('Шутка номер 24')
# print_only_new('Шутка номер 99')
# print_only_new('Шутка номер 15')
# print_only_new('Шутка номер 100')
