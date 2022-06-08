
word = "hat"


print(word[0])
while True:
    guess=input('Please guess a word: ')
    i = 0
    
    for i,letter in enumerate(guess):
        
        
        if letter not in word:
            print('_', end=' ')
        elif letter in word:

            
            try:
                if word[i] == letter:
                    print(letter.upper(), end=' ')
                else:
                    print(letter.lower(), end=' ')
            except:
                print(letter.lower(), end=' ')
                
        
 
    if guess==word: break

print(" done ")