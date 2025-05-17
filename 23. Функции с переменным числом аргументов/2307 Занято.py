def sequence_occupied(**args):
    for i in args:
        for j in args[i]:
            places[int(i) - 1][j - 1] = 1
    max_seq = 0
    max_seq_row = 0
    for row in range(len(places)):
        seq = 0
        for seat in places[row]:
            if seat == 1:
                seq += 1
            else:
                seq = 0
        if seq > max_seq:
            max_seq = seq
            max_seq_row = row + 1
    return max_seq, max_seq_row


places = [[1, 1, 0, 0], [0, 0, 0, 1], [0, 1, 1, 0, 0, 0]]
data = {'2': [3, 2], '1': [4], '3': [4]}
print(sequence_occupied(**data))
print(places)
