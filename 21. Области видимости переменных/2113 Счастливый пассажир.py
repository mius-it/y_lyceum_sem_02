def lucky(ticket):
    if is_lucky(lastTicket) and is_lucky(ticket):
        return 'Счастливый'
    return 'Несчастливый'


def is_lucky(num):
    snum = str(num)
    if (int(snum[0]) + int(snum[1]) + int(snum[2]) ==
        int(snum[3]) + int(snum[4]) + int(snum[5])):
        return True
    return False


# lastTicket = 123456
# print(lucky(100001))
# lastTicket = 123321
# print(lucky(100001))
