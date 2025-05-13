def difference(mylist):
    print('mylist:', mylist)
    print('sorted(mylist):', sorted(mylist))
    print('mylist:', mylist, '- изначальный список остался неизменным')
    print('-------------------------')
    print('mylist:', mylist)
    mylist.sort()
    print('Выполняем mylist.sort()')
    print('mylist:', mylist, '- изначальный список изменён (отсортирован)')


difference([5, 6, 9, 8, 2])