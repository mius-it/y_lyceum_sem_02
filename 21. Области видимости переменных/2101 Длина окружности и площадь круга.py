PI = 3.14159


def circle_length(radius):
    global PI
    return 2 * PI * radius


def circle_area(radius):
    global PI
    return PI * radius ** 2


def main():
    rad = float(input('Введите радиус окружности: '))
    print(circle_length(rad), circle_area(rad))
    pass


print(circle_length(5))
print(circle_area(10))
main()
