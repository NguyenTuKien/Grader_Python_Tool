from sys import stdin

FACTORIAL = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

def main():
    data = stdin.buffer.read().split()
    it = iter(data)
    for _ in range(int(next(it))):
        num = next(it).decode()
        sum = 0
        for digit in num:
            sum += FACTORIAL[int(digit)]
        if sum == int(num):
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()