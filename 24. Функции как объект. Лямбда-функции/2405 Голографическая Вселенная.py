def hologram(*strings, transformation=1):
    result = []
    if transformation == 1:
        for s in strings:
            temp = ' '.join(map(str.capitalize, map(str.lower, s.split())))
            result.append(temp)
    elif transformation == 2:
        for s in strings:
            temp = ''.join([ch for ch in s if ord(ch) % 2 == 0])
            result.append(temp)
    elif transformation == 3:
        for s in strings:
            temp = len(s)
            result.append(temp)
    elif transformation == 4:
        for s in strings:
            if len(s) % 2 == 1:
                s_set = set(s)
                s_list = sorted(list(s_set))
                result.append(''.join(s_list))
            else:
                result.append(s)
    return result


data = ["Everything THAT happens",
        "in three-dimensional space",
        "is displayed on",
        "a two-dimensional border"]
print(*hologram(*data), sep='\n')

print('----------------')
data = ["Everything THAT happens",
        "in three-dimensional space",
        "is displayed on",
        "a two-dimensional border"]
print(*hologram(*data, transformation=1), sep='\n')

print('----------------')
data = ["Everything THAT happens",
        "in three-dimensional space",
        "is displayed on",
        "a two-dimensional border"]
print(*hologram(*data, transformation=2), sep='\n')

print('----------------')
data = ["Everything THAT happens",
        "in three-dimensional space",
        "is displayed on",
        "a two-dimensional border"]
print(*hologram(*data, transformation=3), sep='\n')

print('----------------')
data = ["You can restore",
        "any object",
        "using a hologram"]
print(*hologram(*data, transformation=4), sep='\n')
