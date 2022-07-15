# 1. Name:
#      Trent Black
# 2. Assignment Name:
#      Lab 10: Numeric Sequence
# 3. Assignment Description:
#      turns the users numbver into Francois number
# 4. What was the hardest part? Be as specific as possible.
#      it took a lot of searching the internet to find the formula for Francois nummber conversion 
#      i had no idea Francois existed or knew nothing about him so it made it hard to understand his thinking
#       the formula was kind of confusing as well.
# 5. How long did it take for you to complete the assignment?
#      2 hours programing and another 1 and a half searching the internet for the formula
def fany(n):


    assert 1<= n, "Number is less than 1  " #checks that the number is more than 1 
    
    numbers = [1,2] # these numbers aer used later

    if n == 1:
        franynum = 2
    elif n == 2:
        franynum = 1

    if n > 2:
        for i in range(3, n+1):
            numbers[i%2] = numbers[0] + numbers[1]#this is the franis formula just used in a loop not in recursion 

        franynum = numbers[n%2]# at the end of the loop this is the number 


    print(f"Francois number for {n} is {franynum}")# this is the print 


play = True 
while play != False:

    n = input("(type stop to stop) enter a number to convert to Francois number: ")#enter the number you want to convert
    
    
    if n.lower() == "stop":
        play = False
    else:
        assert isinstance(int(n), int), " your number is not a number " #makes sure that the number entered is a number

        fany(int(n))