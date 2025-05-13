def mirror(arr):
    mirrored_part = reversed(arr)  # так получаем список в обратном порядке
    arr.extend(mirrored_part)  # так дописываем в список значения другого списка


arr = [1, 2]
mirror(arr)
print(*arr)

arr = [1]
mirror(arr)
print(*arr)

arr = [1, 2, 6, 8]
mirror(arr)
print(*arr)
