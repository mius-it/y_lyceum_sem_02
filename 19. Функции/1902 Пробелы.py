def space_game(text):
    spaces = str(text).count(' ')
    if spaces % 2 == 1 or spaces == 0:
        print('Вы проиграли')
    else:
        print('Вы выиграли')

# space_game(input())
