def quarter(xcoord, ycoord):
    if xcoord > 0 and ycoord > 0:
        print('I', end=' ')
    elif xcoord < 0 and ycoord > 0:
        print('II', end=' ')
    elif xcoord < 0 and ycoord < 0:
        print('III', end=' ')
    elif xcoord > 0 and ycoord < 0:
        print('IV', end=' ')
    print('четверть')

# quarter(float(input()), float(input()))
