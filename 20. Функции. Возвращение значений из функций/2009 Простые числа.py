def prime(number):
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return 'Составное число'
    return 'Простое число'


print(prime(4))
print(prime(3))