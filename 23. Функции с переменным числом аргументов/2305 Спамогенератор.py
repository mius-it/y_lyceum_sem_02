def spam(email_to, name_to, date, place='Мусохранск'):
    msg = 'To: ' + email_to + '\n'
    msg += 'Здравствуйте, ' + name_to + '!\n'
    msg += ('Были бы рады видеть вас на встрече начинающих программистов в '
            + place + ', которая пройдет ' + date  + '.\n')
    return msg


print(spam(email_to='biba@yandex.ru', name_to='Биба', place='Нью Йорк', date='25.05.2025'))
print(spam(email_to='boba@yandex.ru', name_to='Боба', date='25.05.2025'))