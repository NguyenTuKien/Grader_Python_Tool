from sys import stdin
import math

def main():
    data = stdin.buffer.read().split()
    it = iter(data)
    for _ in range(int(next(it))):
        a, b = int(next(it)), int(next(it))
        print(math.gcd(a, b))

if __name__ == "__main__":
    main()