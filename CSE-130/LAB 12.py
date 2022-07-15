
# 1. Name:
#      Trent Black
# 2. Assignment Name:
#      Lab 13: Prime Numbers
# 3. Assignment Description:
#      find all the prime numbers up to the number given by the user
# 4. What was the hardest part? Be as specific as possible.
#      This assignment was hard at first i thought i had it with pusedo code but i did not
#       i was able to use my pusedo code to find primes but i did not stop at the squre root of the number 
#       so i found out after a while how to do it by using two for loops 
# 5. How long did it take for you to complete the assignment?
#     3.25 hr


import math
n=9


while n!= 0:
    n = int(input("this program will find all the prime numbers at or below N. Select that N: "))

    assert n != 2 , "There are no prime numbers below 2 "



    assert n != 0 , "0 canot be used no prime numbers  "


    assert n != 1 , "1 cannot be used it is not a prime number nor does it have any lower than itself  "


    assert n != -1 , "-1 cannot be used it is not a prime number nor does it have any lower than itself  "



    primes = []
    for number in range(2, n +1):
        primes.append(number)
  
    for number in range(2, math.ceil((math.sqrt(n)))):
        for multiple in range(2, (math.ceil(n/number)+1)):
            value = number * multiple 


            if value in primes:
                primes.remove(value)
    assert len(primes) >0, "no items in primes "
    print(f"The prime numbers at or below {n} are: {primes}")
