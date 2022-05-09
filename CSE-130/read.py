



import random
from string import digits
from string import punctuation
from string import ascii_letters


password = ' '

symbol = digits 
secrue_random = random.SystemRandom()


for i in range(1):
    password += secrue_random.choice(symbol)

print(password)

guess = ''
guesses = []

while password != guess:

    if len(guess) <= 1 :
        guess += secrue_random.choice(symbol)
        if guess in guesses[0::1]:
           stored = guess[1]
           guess = stored
    else: 
        guesses.append(guess)
        guess = " "

            

print(guess[0])
print(len(guesses))
print(guesses[0::1])
print(guess[1])



