def make_shades(alley, k):
    al_len = len(alley)
    shades = [False] * al_len
    for i in range(al_len - 1):
        sh_len = (alley[i] * k + 1) if alley[i] * k < al_len else al_len
        for j in range(i, i + sh_len):
            shades[j] = True


def calculate_sunny_length(shades):
    pass


def main():
    pass


print(make_shades([0, 0, 0, 4, 0, 1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 3, 0], 1))