


num = 10

guess = 0

while num != guess:
    guess = int(input("guess: "))
    if num > guess:
        print("higher")
    if num < guess:
        print("lower")