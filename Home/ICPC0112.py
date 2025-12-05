from sys import stdin

PRIMES = [True] * 1000000

def sieve():
    PRIMES[0] = PRIMES[1] = False
    for i in range(2, int(1e6**0.5) + 1):
        if PRIMES[i]:
            for j in range(i * i, int(1e6), i):
                PRIMES[j] = False
                
def main():
    sieve()
    data = stdin.buffer.read().split()
    it = iter(data)
    for _ in range(int(next(it))):
        n = int(next(it))
        cnt = 0
        for i in range(5, n - 6):
            if PRIMES[i] and PRIMES[i + 2] and PRIMES[i + 6]:
                cnt += 1
            if PRIMES[i] and PRIMES[i + 4] and PRIMES[i + 6]:
                cnt += 1
        print(cnt)
                

if __name__ == "__main__":
    main()