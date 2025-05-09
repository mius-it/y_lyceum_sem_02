wares = list()
receipt_number = 0


def add_item(item_name, item_cost):
    global wares
    wares.append((item_name, item_cost))


def print_receipt():
    global wares
    global receipt_number
    if wares:
        receipt_number += 1
        print(f'Чек {receipt_number}. Всего предметов: {len(wares)}')
        receipt_sum = 0
        for item in wares:
            print(f'{item[0]} - {item[1]}')
            receipt_sum += item[1]
        print(f'Итого: {receipt_sum}')
        print('-----')
    wares.clear()


# add_item('Блокнот', 100)
# print_receipt()
#
# add_item('Ручка', 70)
# print_receipt()
# print_receipt()
#
# add_item('Булочка', 15)
# add_item('Булочка', 15)
# add_item('Чай', 5)
# print_receipt()
#
# add_item('Булочка', 15)
# add_item('Булочка', 15)
# # (Отменить чек) - этот чек не печатаем
