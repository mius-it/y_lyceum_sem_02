def make_shades(alley, k):
    al_len = len(alley)
    shades = [False] * al_len
    for i in range(al_len - 1):
        if alley[i]:
            sh_len = (alley[i] * k + 1) if (i + alley[i] * k + 1) < al_len else (al_len - i)
            for j in range(i, i + sh_len):
                shades[j] = True
    return shades


def calculate_sunny_length(shades):
    return len(shades) - sum(shades)


def main():
    k = int(input())
    alley = list(map(int, input().split()))
    if calculate_sunny_length(make_shades(alley, k)) < 10:
        print('Тени достаточно')
    else:
        print('Обгорел')

# main()
# print(make_shades([0, 0, 0, 4, 0, 1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 3, 0], 1))
# print(calculate_sunny_length([True, True, True, True, True, True, False, False, False, True, True, True, True, True, True, True, False]))
