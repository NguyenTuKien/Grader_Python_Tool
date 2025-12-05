from sys import stdin, stdout


def main():
    data = stdin.buffer.read().split()
    it = iter(data)
    # for _ in range(int(next(it))):
    n = next(it)
    dec = int(n, 2)
    res =  oct(dec)[2:]
    print(res)

if __name__ == "__main__":
    main()