def golden_ratio(i):
    fibo = [1, 1]
    for j in range(2, i + 1):
        fibo.append(fibo[j - 2] + fibo[j - 1])
    print(fibo[-1] / fibo[-2])

# golden_ratio(4)
