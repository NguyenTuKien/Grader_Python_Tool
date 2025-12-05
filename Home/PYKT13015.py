from sys import stdin

def main():
    data = stdin.buffer.read().split()
    it = iter(data)
    for _ in range(int(next(it))):
        a, b, c, d, M = int(next(it)), int(next(it)), int(next(it)), int(next(it)), int(next(it))
        res = pow(pow(a, b, M), pow(c, d), M)
        print(res)


if __name__ == '__main__':
    main()