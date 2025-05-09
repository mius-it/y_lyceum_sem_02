translated_text = ''


def translate(text):
    vocals = 'аеёиоуыэюяАЕЁИОУЫЭЮЯ'
    global translated_text
    translated_text = ''
    for letter in text:
        if letter not in vocals:
            translated_text += letter
    translated_text = ' '.join(translated_text.split())


# translate("Удивительный факт, но текст на языке НЕРАЗБОРЧИВО оказывается довольно просто читать. Достаточно небольшой тренировки - и вы сможете это делать.")
# print(translated_text)
