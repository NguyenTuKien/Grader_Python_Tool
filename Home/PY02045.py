from sys import stdin


def main():
    data = stdin.buffer.read().split()
    it = iter(data)
    # for _ in range(int(next(it))):
    num = int(next(it))
    while num > 9:
        tmp = str(num).strip()
        num1 = tmp[:len(tmp)//2]
        num2 = tmp[len(tmp)//2:]
        num = int(num1) + int(num2)
        print(num)

if __name__ == "__main__":
    main()