def equation(a, b):
    x1, y1 = str(a).split(';')
    x2, y2 = str(b).split(';')

    if x2 == x1:
        k = 0
    else:
        k = (float(y2) - float(y1)) / (float(x2) - float(x1))
    b = float(y1) - k * float(x1)

    if k == 0:
        print(b)
    else:
        print(k, b)

# equation("0;0", "1;1")
# equation("0;0", "0;4")
# equation("4;6.9", "-5.2;6.9")
