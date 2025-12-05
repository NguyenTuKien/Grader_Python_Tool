from sys import stdin


def main():
    data = stdin.buffer.read().split()
    it = iter(data)
    # for _ in range(int(next(it))):
    line = next(it).decode()
    nums = [int(line[i:i+2]) for i in range(0, len(line), 2)]
    printed = set()
    for num in nums:
        if num not in printed and 10 <= num <= 99:
            print(f"{num:02d}", end=' ')
            printed.add(num)


if __name__ == "__main__":
    main()