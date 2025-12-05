from sys import stdin

def factorial(n):
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res

def permutation(n, cur = "", used = []):
    if len(cur) == n:
        print(cur, end=' ')
        return
    for i in range(n, 0, -1):
        if i not in used:
            used.append(i)
            permutation(n, cur + str(i), used)
            used.pop()

def main():
    data = stdin.buffer.read().split()
    it = iter(data)
    for _ in range(int(next(it))):
        n = int(next(it))
        print(factorial(n))
        permutation(n)
        print()

if __name__ == "__main__":
    main()