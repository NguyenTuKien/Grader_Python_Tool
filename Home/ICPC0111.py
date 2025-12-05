from sys import stdin


def main():
    data = stdin.buffer.read().split()
    it = iter(data)
    for _ in range(int(next(it))):
        n, k = int(next(it)), int(next(it))
        a = [int(next(it)) for _ in range(n)]
        for i in range(k, n):
            print(a[i], end=" ")
        for i in range(k):
            print(a[i], end=" ")
        print()


if __name__ == "__main__":
    main()