def print_operation_table(operation, num_rows=9, num_columns=9):
    for y in range(1, num_rows + 1):
        for x in range(1, num_columns + 1):
            print(operation(x, y), end='\t')
        print('')



# print_operation_table(lambda x, y: x * y)
# print_operation_table(lambda x, y: x * y, 5)
