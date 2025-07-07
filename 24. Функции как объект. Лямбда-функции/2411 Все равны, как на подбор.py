def same_by(characteristic, objects):
    if not objects:
        return True
    reference = characteristic(objects[0])
    for obj in objects:
        if characteristic(obj) != reference:
            return False
    return True


# values = [0, 2, 10, 6]
# if same_by(lambda x: x % 2, values):
#     print('same')
# else:
#     print('different')
#
# print('------------------')
#
# values = [1, 2, 3, 4]
# if same_by(lambda x: x % 2, values):
#     print('same')
# else:
#     print('different')
# print('------------------')
# if same_by(lambda x: x % 2, []):
#     print('same')
# else:
#     print('different')
