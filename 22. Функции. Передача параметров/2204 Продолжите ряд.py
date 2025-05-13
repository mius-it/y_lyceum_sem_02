def continue_fibonacci_sequence(sequence, n):
    for i in range(n):
        next_element = sequence[-1] + sequence[-2]
        sequence.append(next_element)  # новые элементы добавляются в список именно таким образом


# sequence = [1, 1]
# continue_fibonacci_sequence(sequence, 1)
# print(*sequence)
#
# sequence = [1, 1, 2, 3, 5]
# continue_fibonacci_sequence(sequence, 0)
# print(*sequence)
#
# sequence = [1, 1, 2, 3, 5]
# continue_fibonacci_sequence(sequence, 10)
# print(*sequence)
