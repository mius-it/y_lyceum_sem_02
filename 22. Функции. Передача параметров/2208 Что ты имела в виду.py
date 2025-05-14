numbers = [2, 5, 7, 7, 8, 4, 1, 6]
# odd = even = []  # два разных имени списка указывают на один объект
# в результате действия над разными именами по сути производятся над одним списком
odd, even = [], []  # исправляется так
for number in numbers:
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)

print('odd:', odd)
print('even:', even)