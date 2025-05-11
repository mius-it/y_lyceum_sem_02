stat = {}


def get_transactions(t):
    global stat
    if t == 'print_it':
        for row in stat.keys():
            print(stat[row][0], row, stat[row][1])
    else:
        # phone = t[:t.find('-')]
        type = t[t.find('-') + 1:t.find(':')]
        value = int(t[t.find(':') + 1:])
        if type not in stat:
            stat[type] = [0, 0]
        stat[type][0] += 1
        stat[type][1] += value


# get_transactions('880005553535-перевод:100')
# get_transactions('111111111-перевод:1000')
# get_transactions('880005553535-оплата_жкх:10000')
# get_transactions('89065664312-перевод:50000000')
# get_transactions('print_it')
