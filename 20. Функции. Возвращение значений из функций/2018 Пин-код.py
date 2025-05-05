import math


def check_pin(pinCode):
    nums = list(map(int, pinCode.split('-')))

    for i in range(2, nums[0]):
        if not nums[0] % i:
            return 'Некорректен'

    numstr = str(nums[1])
    ln = len(numstr)
    for i in range(ln):
        if numstr[i] != numstr[ln - i - 1]:
            return 'Некорректен'

    if not math.log2(nums[2]).is_integer():
        return 'Некорректен'

    return 'Корректен'


# print(check_pin('7-101-4'))
# print(check_pin('12-22-16'))
# print(check_pin('7-23-16'))
# print(check_pin('7-101-66'))
