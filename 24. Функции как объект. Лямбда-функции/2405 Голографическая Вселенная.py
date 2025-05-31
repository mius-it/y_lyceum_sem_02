def hologram(*strings, transformation=1):
    pass


data = ["Everything that happens",
        "in three-dimensional space",
        "is displayed on",
        "a two-dimensional border"]
print(*hologram(*data), sep='\n')


data = ["You can restore",
        "any object",
        "using a hologram"]
print(*hologram(*data, transformation=4), sep='\n')

