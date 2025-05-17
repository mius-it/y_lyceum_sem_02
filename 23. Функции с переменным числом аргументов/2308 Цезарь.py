def encrypt_caesar(msg, shift=3):
    result = ''
    for letter in msg:
        old_code = ord(letter)
        if 1040 <= old_code <= 1071:
            new_code = 1040 + (old_code - 1040 + shift) % 32
            result += chr(new_code)
        elif 1072 <= old_code <= 1103:
            new_code = 1072 + (old_code - 1072 + shift) % 32
            result += chr(new_code)
        else:
            result += letter
    return result


def decrypt_caesar(msg, shift=3):
    result = ''
    for letter in msg:
        old_code = ord(letter)
        if 1040 <= old_code <= 1071:
            new_code = 1040 + (old_code - 1040 - shift) % 32
            result += chr(new_code)
        elif 1072 <= old_code <= 1103:
            new_code = 1072 + (old_code - 1072 - shift) % 32
            result += chr(new_code)
        else:
            result += letter
    return result

# msg = "Да здравствует салат Цезарь! ЬЪЭЮЯ"
# shift = 3
# encrypted = encrypt_caesar(msg, shift)
# decrypted = decrypt_caesar(encrypted, shift)
# print(encrypted)
# print(decrypted)
#
# print('\n-------------\n')
#
# msg = "Да здравствует салат Цезарь! ЬЪЭЮЯ"
# shift = 5
# encrypted = encrypt_caesar(msg, shift)
# decrypted = decrypt_caesar(encrypted, shift)
# print(encrypted)
# print(decrypted)
