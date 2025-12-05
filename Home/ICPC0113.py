from sys import stdin

PRIMES = [True] * 1000000
EMIRP_NUM = []

def sieve():
    PRIMES[0] = PRIMES[1] = False
    for i in range(2, int(1e6**0.5) + 1):
        if PRIMES[i]:
            for j in range(i * i, int(1e6), i):
                PRIMES[j] = False
    for i in range(13, int(1e6)):
        if PRIMES[i]:
            rev = int(str(i)[::-1])
            if i < rev and PRIMES[rev]:
                EMIRP_NUM.append((i, rev))
                
def main():
    sieve()
    data = stdin.buffer.read().split()
    it = iter(data)
    for _ in range(int(next(it))):
        n = int(next(it))
        idx = 0
        ans = []
        for i, rev in EMIRP_NUM:
            if i >= n:
                break
            if rev < n:
                ans.append(i)
                ans.append(rev)
        print(' '.join(map(str, ans)))

if __name__ == "__main__":
    main()