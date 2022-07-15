


while True:
    max_number = int(input("enter the number "))
    if max_number >=2:
        break

primes = list(range(2,max_number +1))


for prime in primes:
    if prime > max_number **2:
        break
    print(primes[len(primes)-1])
    for mult in range(2,len(primes)):
        cross = mult * prime

        if cross > len(primes):
            break
        elif cross in primes:
            primes.remove(cross)

print(primes)