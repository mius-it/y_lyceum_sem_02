def search_rhymes(rhyme):
    vowels = 'аеёиоуыэюя'
    words = rhyme.split()
    syllables = 0
    for word in words:
        syllable_counter = 0
        for letter in word:
            if letter in vowels:
                syllable_counter += 1
        if syllables == 0:
            syllables = syllable_counter
        elif syllable_counter != syllables:
            return 'Пам парам'
    return 'Парам пам-пам'


print(search_rhymes(input()))
# print(search_rhymes("пара-ра-рам рам-пам-папам па-ра-па-дам"))
# print(search_rhymes("пара-ра-рам-ам рам-пам-папам па-ра-па-дам"))
