letter = input('Enter a character: ')
if len(letter) == 1:
    if letter.isalpha():
        print('Alphabet')
    else:
        print('No')
else:
    print('Enter only one character')
