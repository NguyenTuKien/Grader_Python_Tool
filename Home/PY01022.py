from sys import stdin


def main():
    s = stdin.readline().strip()
    ans, sum = 0, 100
    while sum >= 10:
        sum = 0
        for c in s:
            sum += ord(c) - 48
        ans += 1
        s = str(sum)
    print(ans)

if __name__ == "__main__":
    main()