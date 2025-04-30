def palindrome(s):
    s = s.replace(' ', '').lower()
    l = len(s)
    for i in range(l//2):
        if s[i].lower() != s[l - i - 1].lower():
            return 'Не палиндром'
    return 'Палиндром'


# print(palindrome('А роза упала на лапу Азора'))
# print(palindrome('Палиндром'))
