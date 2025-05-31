def function(*args, func):
    return func(args)


data = [1, 2, 15, 3]
f = max
print(function(*data, func=f))

data = ["one", "two", "three"]
f = sorted
print(function(*data, func=f))

