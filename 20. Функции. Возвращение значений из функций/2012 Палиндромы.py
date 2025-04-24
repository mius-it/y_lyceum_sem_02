def palindrome(s):
    l = len(s)
    for i in range(l//2):
        if s[i] != s[l - i - 1]:
            return 'Не палиндром'
    return 'Палиндром'


print(palindrome('А роза упала на лапу Азора'))
print(palindrome('Палиндром'))