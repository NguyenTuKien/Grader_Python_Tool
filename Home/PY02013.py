from sys import stdin


def main():
    data = stdin.buffer.read().split()
    it = iter(data)
    while True:
        n = int(next(it))
        if n == 0:
            break
        cnt = 1
        while(n != 1):
            cnt += 1
            if n % 2 == 0:
                n //= 2
            else:
                n = n * 3 + 1
        print(cnt)

if __name__ == "__main__":
    main()