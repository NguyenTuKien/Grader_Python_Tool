from sys import stdin


def main():
    data = stdin.buffer.read().split()
    it = iter(data)
    # for _ in range(int(next(it))):
    m, n = int(next(it)), int(next(it))
    a = [[int(next(it)) for _ in range(n)] for _ in range(m)]
    mx = max(max(row) for row in a)
    mn = min(min(row) for row in a)
    lucky_numbers = mx - mn
    positions = []
    found = False
    for i, row in enumerate(a):
        for j, val in enumerate(row):
            if val == lucky_numbers:
                positions.append(f"Vi tri [{i}][{j}]")
                found = True
    if not found:
        print("NOT FOUND")
    else:
        print(lucky_numbers)
        for pos in positions:
            print(pos)


if __name__ == "__main__":
    main()