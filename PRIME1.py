#Python 2.7.3
#Sphere Online Judge Problem PRIME1
#http://www.spoj.com/problems/PRIME1/

from math import sqrt

primes = [2]

#steps through each number from 3 to 32000 (the sqrt of the given upper bound) by 2s
#if an individual number is prime, adds it to the list "primes"
for i in range(3,32000,2):
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

#outputs the list of primes; used for bug-testing purposes only
#print primes[:-1]

#T is the number of integer pairs (test cases) and thus times the generator will activate
T = input()
#clears the var "output" (just in case :])
output = ""

#steps through each value in
for t in range(T):
    #after the first integer pair, adds a newline to separate the values)
    if (t >0):
        output += "\n"

    #grabs the integer pairs from the user and splits them into two vars, m and n, where there is a space
    m,n = raw_input().split(' ')
    m = int(m)
    n = int(n)
    cap = sqrt(n)+1

    #if the lower bound is not at least 2, make it 2 (no primes exist smaller than 2)
    if (m < 2):
        m = 2

    #changes "isprime" into a list of 100001 "True"s
    isprime = [True] * 100001

    #for all the irrelevant values in "primes, sets the corresponding True/False value in "isprime" to False
    #faster than looping through all the values of isprime and setting them to False individually
    for i in primes:
        if (1 >= cap):
            break

        if (i >= m):
            start = i * 2
        else:
            start = M + ((i - M % i)%i)

        falseblock = [False] * len(isprime[start-M:N+1-M:i]);
        isprime[start-M:N+1-M:i] = falseblock

    #finally, the sweet part
    #adds all the relevant primes (i.e. between n and m) to the output list
    for i in range(m:n+1):
        if (isprime[i-m] == True):
            output += str(i) + "\n"

print output[:-1]