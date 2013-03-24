#Python 2.7.3
#Sphere Online Judge Problem PRIME1
#http://www.spoj.com/problems/PRIME1/

from math import sqrt

primes = [2]

for i in range(3,3500,2):
    isprime = True

    cap = sqrt(i) + 1

    for j in primes:
        if (j >= cap):
            break
        if (i % j == 0):
            isprime = False
            break

    if (isprime):
        primes.append(i)

print primes[:-1]