'''
Author: Matthew Harris
File: W08_Wordle.py
'''
again = 'y'
while again.lower() == 'y':
    word = 'mosiah'
    word_length = len(word)
    print(f'The word has {word_length} characters')
    for i in range(word_length):
        print('_ ', end='')
    print() 
    answered_guessed = False
    guess = input('What is your guess? ')
    guess_len = len(guess)
    while guess.lower() != word:
        for index, letter in enumerate(guess):
            if index < word_length and letter == word[index]:
                print(letter.upper() + ' ', end='')
            elif letter.lower() in word:
                print(letter + ' ', end='')
            else:
                print('_ ', end='')
        print()
        guess = input('What is your guess? ')
        guess_len = len(guess)
    print()
    print(f'Congrats, you guessed the word: {word}')
    again = input('Would you like to play again (y/n)? ')