def tribonacci(n):
    if n > 2:
        return tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)
    elif n == 2:
        return 1
    elif n == 1:
        return 0
    elif n == 0:
        return 0


print(tribonacci(7))