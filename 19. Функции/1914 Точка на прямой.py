def line(s, t):
    k = float(s[:s.find('x')])
    b = float(s[s.find('+') + s.find('-') + 1:])
    x = float(t[:t.find(';')])
    y = float(t[t.find(';') + 1:])
    return y == k * x + b


# print(line("1x+6", "1;7"))
# print(line("5x-10", "5;-9"))
# print(line("0x+7", "3;7"))
# print(line("3.5x+0", "2;7"))
