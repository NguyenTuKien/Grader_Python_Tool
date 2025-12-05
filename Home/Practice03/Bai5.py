from sys import stdin
from math import gcd

def lcm(a, b):
    return a * b // gcd(a, b)

def V(a, b, x):
    return x * (a - 2 * x) * (b - 2 * x)

def big(a, b):
    arr = []
    for i in range(1, min(a, b) // 2):
        arr.append(V(a, b, i))
    arr.sort(reverse=True)
    return arr[:3]

def main():
    data = stdin.buffer.read().split()
    it = iter(data)
    for _ in range(int(next(it))):
        a, b, x, y, z ,l, r = int(next(it)), int(next(it)), int(next(it)), int(next(it)), int(next(it)), int(next(it)), int(next(it))
        v = big(a, b)
        for i in range (x, r + 1, v[0]):
            if i % v[1] == y and i % v[2] == z:
                k = i
                break
        if k < l :
            com = lcm(v[0], lcm(v[1], v[2]))
            d = (l - k) // com
            if d * com + k < l :
                d += 1
            print(k + d * com)
        else:
            print(k)

if __name__ == "__main__":
    main()