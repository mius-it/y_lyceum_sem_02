horses_available = [True] * 10

def do_bet(horse, bet):
    global horses_available
    if horses_available[horse - 1] and bet:
        print(f'Ваша ставка в размере {bet} на лошадь {horse} принята')
        horses_available[horse - 1] = False
    else:
        print('Что-то пошло не так, попробуйте еще раз')



do_bet(1, 10)
do_bet(1, 100)
do_bet(2, 0)
do_bet(2, 200)