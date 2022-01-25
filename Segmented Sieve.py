import math
new_prime = []
def sieveEratosthenes(n):

    prime = [True for i in range(n+1)]
    p = 2
    while p <= n:
        for i in range(len(prime)):
            if prime[i]:
                for j in range(p*p, n+1, p):
                    prime[j] = False
            p += 1

    for k in range(2, len(prime)):
        if prime[k]:
            new_prime.append(k)
    return new_prime


def segmentedSieve(n):
    limit = int(math.floor(math.sqrt(n))+1)
    sieveEratosthenes(limit)

    low = limit
    high = limit*2
    while low < n:
        if high > n:
            high = n

        new = [True for i in range(low+1)]
        for i in range(len(new_prime)):
            lower = int((low//new_prime[i])*new_prime[i])
            if lower < low:
                lower += new_prime[i]
            for j in range(lower, high+1, new_prime[i]):
                new[j - low] = False
        for k in range(low, high):
            if new[k-low]:
                new_prime.append(k)
        low += limit
        high += limit
    print(new_prime)
    
    
n = 100
segmentedSieve(n)

'''

Ans => [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

''
