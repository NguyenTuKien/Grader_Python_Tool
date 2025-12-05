import sys

def count_divisors(n):
    if n == 1:
        return 1
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            if i * i == n:
                count += 1
            else:
                count += 2
    return count

def solve():
    num_tests = int(sys.stdin.readline())
    results = []
    for _ in range(num_tests):
        n = int(sys.stdin.readline())
        while n > 0 and n % 2 == 0:
            n //= 2
        num_odd_divisors = count_divisors(n)
        results.append(str(num_odd_divisors - 1))
    print("\n".join(results))

if __name__ == "__main__":
    solve()