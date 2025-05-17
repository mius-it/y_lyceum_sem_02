scoring = {
'Яблочко': 50,
'Зеленое кольцо': 25,
'Внешнее_кольцо': {1:8, 2: 6, 3: 42, 20: 50},
'Внутреннее_кольцо': {1: 2, 2: 9, 3: 56, 20: 3}
}


def score(*args):
    print(args)
    if args[0] == 'Яблочко' or args[0] == 'Зеленое кольцо':
        return scoring[args[0]]
    else:
        return scoring[args[0]][args[1]]


# print(score("Яблочко"))
# print(score("Внешнее_кольцо", 1))
