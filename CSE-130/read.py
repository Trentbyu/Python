from pickle import NONE
import re
import random


word = "hat"


print(word[0])
while True:
    guess=input('Please guess a word: ')
    i = 0
    
    for letter in guess:
        
        
        if letter not in word:
            print('_', end=' ')
        elif letter in word:

            if i == None:
                print(letter.lower(), end=' ')
            elif word[i] == letter:
                print(letter.upper(), end=' ')
            else:
                print(letter.lower(), end=' ')
           
        i += 1 



        if i > len(word):
            i = None
    
    
 
    if guess==word: break

print(" done ")