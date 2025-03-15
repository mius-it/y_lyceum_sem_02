def ask_password():
    cntr = 3
    while cntr > 0:
        cntr -= 1
        psw = input()
        if psw == 'password':
            print('Пароль принят')
            return
    print('В доступе отказано')

# ask_password()
