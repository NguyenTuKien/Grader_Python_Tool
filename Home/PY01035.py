from sys import stdin


def main():
    data = stdin.buffer.read().split()
    it = iter(data)
    # for _ in range(int(next(it))):
    bin = next(it).decode()
    n = int(bin, 2)
    print(oct(n)[2:])

if __name__ == "__main__":
    main()