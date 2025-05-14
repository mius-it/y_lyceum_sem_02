# Создаем глобальную переменную для хранения дерева
wb_tree = None

# Определяем черное и белое поддеревья
black = []
white = []

# Рекурсивно создаем фрактальную структуру
black.append(white)
black.append(white)
black.append(white)  # Черная вершина содержит 3 белых поддерева

white.append(black)
white.append(black)  # Белая вершина содержит 2 черных поддерева

# Корень дерева - черная вершина (содержит 3 белых поддерева)
wb_tree = black

# Для предотвращения бесконечной рекурсии при печати
# добавим ограничение глубины вывода
# def print_tree(tree, depth=0, max_depth=1):
#     if depth > max_depth:
#         print("  " * depth + "...")
#         return
#     if tree is black:
#         print("  " * depth + "Black")
#     else:
#         print("  " * depth + "White")
#     for child in tree:
#         print_tree(child, depth + 1, max_depth)
#
# # Демонстрация структуры дерева
# print("Фрактальное дерево (первые 3 уровня):")
# print_tree(wb_tree)
