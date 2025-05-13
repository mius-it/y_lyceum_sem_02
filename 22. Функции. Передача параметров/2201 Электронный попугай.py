known = []


def parrot(phrase):
    if phrase in known:
        print(phrase)
    known.append(phrase)


# parrot("Привет!")
# parrot("Привет!")
# parrot("Как дела?")
#
# parrot("Привет")
# parrot("Как тебя зовут?")
# parrot("Привет")
