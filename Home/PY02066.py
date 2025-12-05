from sys import stdin

def main():
    data = stdin.buffer.read().split()
    it = iter(data)
    n = int(next(it))
    a = [int(next(it)) for _ in range(n)]
    lost = []
    idx = 1
    for x in a:
        while idx < x:
            lost.append(idx)
            idx += 1
        idx = x + 1

    if not lost:
        print("Excellent!")
    else:
        print("\n".join(map(str, lost)))

if __name__ == "__main__":
    main()
