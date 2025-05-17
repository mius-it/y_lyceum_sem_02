def choose_coffee(*order):
    global ingredients
    bill = []
    for coffee in order:
        if coffee == 'Эспрессо':
            ingredients[0] -= 1
        elif coffee == 'Капучино':
            ingredients[0] -= 1
            ingredients[1] -= 3
        elif coffee == 'Маккиато':
            ingredients[0] -= 2
            ingredients[1] -= 1
        elif coffee == 'Кофе по-венски':
            ingredients[0] -= 1
            ingredients[2] -= 2
        elif coffee == 'Латте Маккиато':
            ingredients[0] -= 1
            ingredients[1] -= 2
            ingredients[2] -= 1
        elif coffee == 'Кон Панна':
            ingredients[0] -= 1
            ingredients[1] -= 1
        for i in ingredients:
            if i < 0:
                bill.append('К сожалению, не можем предложить Вам напиток')
                return '\n'.join(bill)
        else:
            bill.append(coffee)
    return '\n'.join(bill)


# ingredients = [1, 2, 3]
# print(choose_coffee("Эспрессо", "Капучино", "Маккиато", "Кофе по-венски", "Латте Маккиато", "Кон Панна"))
# print('\n----------------\n')
# ingredients = [4, 4, 0]
# print(choose_coffee("Капучино", "Маккиато", "Эспрессо"))
