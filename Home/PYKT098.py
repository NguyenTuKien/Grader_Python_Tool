from sys import stdin


def main():
    with open("DATA.in", "rb") as input:
        data = input.read().split()
    it = iter(data)
    # for _ in range(int(next(it))):
    output = []
    while True:
        try:
            n = next(it).decode()
            try:
                m = int(n)
                if m > 2 ** 31 - 1 or m < -2 ** 31:
                    output.append(n)
                    continue
            except ValueError:
                output.append(n)
                continue
        except StopIteration:
            break
    output.sort()
    print(' '.join(output))

if __name__ == "__main__":
    main()