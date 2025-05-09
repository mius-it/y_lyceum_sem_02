MorseCode = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
    ' ': '-...-',
    ',': '.-.-.-',
    '.': '......',
    ':': '---...',
    ';': '-.-.-.',
    '-': '-....-',
    '?': '..--..',
    '!': '--..--'
}


def encode_to_morse(text):
    mrz = ''
    for letter in text:
        mrz += MorseCode[letter] + ' '
    print('Encoded phrase is:', mrz)


def decode_from_morse(code):
    reverse_MorseCode = {v: k for k, v in MorseCode.items()}
    mrz = code.split()
    phrase = ''
    for letter in mrz:
        phrase += reverse_MorseCode[letter]
    print('Decoded phrase is:', phrase)

def main():
    while 1:
        choice = input('Encode, Decode or Finish? (e/d/f): ')
        if choice == 'f':
            break
        elif choice == 'e':
            encode_to_morse(input('Input phrase in english to encode: ').upper())
        elif choice == 'd':
            decode_from_morse(input('Input Morze to decode (space separated): '))
        else:
            print('Wrong answer, try again')

main()