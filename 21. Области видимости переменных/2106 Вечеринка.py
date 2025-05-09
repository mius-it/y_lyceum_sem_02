friendslist = {}


def add_friends(name_of_person, list_of_friends):
    global friendslist
    if name_of_person not in friendslist:
        friendslist[name_of_person] = []
    friendslist[name_of_person].extend(list_of_friends)


def are_friends(name_of_person1, name_of_person2):
    global friendslist
    return name_of_person2 in friendslist[name_of_person1]


def print_friends(name_of_person):
    global friendslist
    print(friendslist[name_of_person])


# add_friends("Алла", ["Марина", "Иван"])
# print_friends("Алла")
# print(are_friends("Алла", "Мария"))
# add_friends("Алла", ["Мария"])
# print_friends("Алла")
# print(are_friends("Алла", "Мария"))
