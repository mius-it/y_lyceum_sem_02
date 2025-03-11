def who_are_you_and_hello():
    name = input()
    while not name.isalpha() or not name.istitle():
        name = input()
    print(f'Привет, {name}!')

# who_are_you_and_hello()
