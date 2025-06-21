def ask_password(login, password, success, failure):
    vowels = 'aeiouy'
    is_ok = True
    error_message = ''
    login_consonants = ''.join([char for char in login if char not in vowels])
    password_consonants = ''.join([char for char in password if char not in vowels])
    if login_consonants != password_consonants:
        is_ok = False
        error_message = 'Wrong consonants'
    vowels_counter = 0
    for char in password:
        if char in vowels:
            vowels_counter += 1
    if vowels_counter < 3:
        is_ok = False
        if error_message == 'Wrong consonants':
            error_message = 'Everything is wrong'
        else:
            error_message = 'Wrong number of vowels'

    if is_ok:
        success('Привет,' + login)
    else:
        failure('Кто-то пытался притвориться пользователем ' + login + ', но в пароле допустил ошибку:',
                error_message.upper())


def main(login, password):
    ask_password(login.lower(), password.lower(),
                 lambda login: print(login), lambda login, err: print(login, err))


main("anastasia", "nsyatas")
main("eugene", "aanig")
ask_password("anastasia", "nsyatos",
             lambda login: print('super'), lambda login, err: print('bad'))
