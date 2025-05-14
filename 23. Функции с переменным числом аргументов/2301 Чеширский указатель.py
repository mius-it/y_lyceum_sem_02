def cheshire(lst):
    first, *middle, last = lst
    for word in middle:
        if first.lower() <= word.lower() <= last.lower():
            print(word, end=' ')


# cheshire('Fury said to a mouse That he met in the house'.split())
# print('\n---')
# cheshire('How I wonder what you\'re at Twinkle twinkle little bat Up above '
#          'the world you fly Like a tea-tray in the sky'.split())
cheshire(input().split())