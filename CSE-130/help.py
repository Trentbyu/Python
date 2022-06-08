
word = "dogs"
guess = "dpgs"

for i,l in enumerate(word):
    

 

    if word[i] == guess[i]:

        print(guess[i].upper(), end='')

    else:
        print("_", end='')
