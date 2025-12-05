from sys import stdin
from math import isqrt
from bisect import bisect_right

def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, isqrt(n) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return [x for x in range(n + 1) if is_prime[x]]

def main():
    n = int(stdin.read())
    limit = isqrt(n)
    primes = sieve(limit)
    ans = 0
    for p in primes:
        if p**8 <= n:
            ans += 1
        else:
            break 
    
    prime_count = len(primes)
    for i in range(prime_count):
        p1 = primes[i]
        if p1 * p1 >= limit:
            break
        target = limit // p1
        k = bisect_right(primes, target)
        if k > i + 1:
            ans += (k - (i + 1))

    print(ans)

if __name__ == "__main__":
    main()