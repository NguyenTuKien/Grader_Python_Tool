from sys import stdin
import re


def main():
    data = stdin.buffer.read().split()
    it = iter(data)
    nums = []
    for _ in range(int(next(it))):
        n = next(it).decode()
        split_nums = re.findall(r'\d+', n)
        for num in split_nums:
            nums.append(int(num))
    nums.sort()
    for num in nums:
        print(num)

if __name__ == "__main__":
    main()