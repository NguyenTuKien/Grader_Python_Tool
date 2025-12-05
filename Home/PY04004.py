from sys import stdin


def main():
    data = stdin.buffer.read().split()
    it = iter(data)
    # for _ in range(int(next(it))):
    a, b, c, d = int(next(it)), int(next(it)), int(next(it)), int(next(it))
    e = a * d + c * b
    f = b * d
    import math
    g = math.gcd(e, f)
    print(f"{e//g}/{f//g}")

if __name__ == "__main__":
    main()