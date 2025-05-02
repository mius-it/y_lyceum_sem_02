def password_level(password):
    if len(password) <= 6:
        return 'Недопустимый пароль'
    if (password.isnumeric() or
            (password.isalpha() and password == password.lower())):
        return 'Ненадежный пароль'
    if (password.isalpha() or
            password.isalnum() and password == password.lower()):
        return 'Слабый пароль'
    return 'Надежный пароль'


print(password_level("kgsu"))
print(password_level("12345678"))
print(password_level("qwertyuiop"))
print(password_level("qWerTyuiOp"))
print(password_level("qwerty123"))
print(password_level("QwerTy123"))
