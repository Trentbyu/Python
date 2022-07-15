
max_number = 100



primes = list(range(2,max_number +1))
constPrime = list(range(2,max_number +1))

for i in constPrime:
    
    if i*2 in primes:
        x = i*2
        primes.remove(x)

    if i*3 in primes:
        x = i*3
        primes.remove(x)
    if i*4 in primes:
        x = i*4

        primes.remove(x)
    if i*5 in primes:
        x = i*5
        
        primes.remove(x)
    if i*7 in primes:
        x = i*7
        
        primes.remove(x)
    

print(primes)