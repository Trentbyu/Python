
'''
secret_word = 'mosiah'
guess = ''
guesses = 0
while secret_word != guess:
    print()
    guesses += 1
    guess = input('What is your guess? ')
    guess = guess.lower()
    if guess == secret_word:
        print('Congratulations! You guessed it!')
        print(f'It took you {guesses} guesses.')
    else:
        print('Your guess was not correct.')
'''
# have secret word
# prompmt usere guess
# give hint '_' wrong 
    # lowercase = wrong spot
    # uppercase = right letter right spot
# loop till guess right
# output number of guesses
# print(word1[2])
# outputs 'm' from temple
play = 'yes'
while play == 'yes':
    
    print()
    print('Welcome to the word guessing game!')
    print()
    #word options
    word1 = 'temple'
    word2 = 'moroni'
    word3 = 'hhhhhh'
    word4 = 'mosiah'
    word5 = 'hat'
    word6 = 'alphabet'
    word7 = 'moronihah'
    
    wordnum = 0
    #prompt user to choose which word they will guess
    while wordnum > 7 or wordnum < 1:
        wordnum = int(input('Which word do you want to use? (pick a number between 1 and 7): '))
        if wordnum > 7 or wordnum < 1:
            print('Error')
    print()
    #declare word based on user choice
    if wordnum == 1:
        magic_word = word1
    elif wordnum == 2:
        magic_word = word2
    elif wordnum == 3:
        magic_word = word3
    elif wordnum == 4:
        magic_word = word4
    elif wordnum == 5:
        magic_word = word5
    elif wordnum == 6:
        magic_word = word6
    elif wordnum == 7:
        magic_word = word7
    else:
        magic_word = 'i don\'t know how you managed this'
    
    #don't know yet if i'll need this
    word_len = len(magic_word)
    keep_guessing = 'yes'
    guesses = 0
    print('Your hint is: ',end='')
    for letter in magic_word:
        print('_ ',end='')
    
    print('',end='\n')
    print()
    while keep_guessing == 'yes':
        # guess iterations
        guesses += 1
        guess = input('What is your guess? ')
        guess = guess.lower()
        if guess == magic_word:
            print()
            print('Congratulations! You guessed it!')
            print(f'It took you {guesses} guesses.')
            keep_guessing = 'no'
        else:
            
            # generate hint
            hint = False
            print('Your hint is: ',end='')
            guess_len = len(guess)
            for spot in range(guess_len):
                
                if spot < word_len:
                    if magic_word[spot] == guess[spot]:
                        letter = guess[spot].upper()
                        print(f'{letter} ',end='')
                    else:
                        letter = '_'
                        for x in range(word_len):
                            if guess[spot] == magic_word[x]:
                                letter = guess[spot]
                        print(f'{letter} ', end='')
                else:
                    letter = '_'
                    hint = True
                    for x in range(word_len):
                        if guess[spot] == magic_word[x]:
                            letter = guess[spot]
                    print(f'{letter} ',end='')
            if hint:
                print(f'\nRemember the word is only {word_len} letters long')
        print('',end='\n')
    print()
    play = input('Do you want to play again? ')
    play = play.lower()
    
    print()
print('Thanks for playing! ')
print()
