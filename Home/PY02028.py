from sys import stdin

def factor(x):
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True
def main():
    data = stdin.buffer.read().split()
    it = iter(data)
    # for _ in range(int(next(it))):
    n = int(next(it))
    arr = [int(next(it)) for _ in range(n)]
    prime = []
    mark = [0 for _ in range(n)]
    for i, x in enumerate(arr):
        if factor(x):
            prime.append(x)
            mark[i] = 1
    prime.sort()
    for i, x in enumerate(arr):
        if mark[i] == 1:
            print(prime.pop(0), end=' ')
        else : 
            print(x, end=' ')
if __name__ == "__main__":
    main()