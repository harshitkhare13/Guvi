letter = input('Enter an alphabet: ')
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
if (letter >= 'a' and letter <= 'z') or  (letter >= 'A' and letter <= 'Z'): 
    if letter in vowels:
        print('vowel')
    else:
        print('consonant')
else:
    print('Invalid')
