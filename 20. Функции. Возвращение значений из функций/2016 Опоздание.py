def late(now, classes, bus):
    time_to_classes = ((int(classes[:classes.find(':')]) - int(now[:now.find(':')])) * 60 +
                        (int(classes[classes.find(':') + 1:]) - int(now[now.find(':') + 1:])))
    #print(time_to_classes)
    for b in reversed(bus):
        if time_to_classes - b - 20 >= 0:
            break
        b = -1
    if b == -1:
        return 'Опоздание'
    return b

print(late('12:00', '12:40', [0, 1, 4, 6, 25]))
print(late('9:20', '9:35', [4, 25, 30]))