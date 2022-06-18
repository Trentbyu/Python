



def fib(num):

    if num == 1:

        return 2 

    if num == 2: 

        return 1 
   
    
    x=1
    y=2

    for i in range(0, (num-2)):
        ap = x+y
        
        x = y
        y = ap
        print(x)
       
   
    
    return y






fib(8)