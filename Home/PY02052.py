from sys import stdin


def main():
    data = stdin.buffer.read().split()
    it = iter(data)
    # for _ in range(int(next(it))):
    n = int(next(it))
    arr = [[int(next(it)) for _ in range(n)] for _ in range(n)]
    diff = int(next(it))
    sum_top = 0
    sum_bot = 0
    for i in range(n):
        for j in range(n):
            if i < j:
                sum_top += arr[i][j]
            elif i > j:
                sum_bot += arr[i][j]
    if(abs(sum_top - sum_bot) <= diff):
        print("YES")
    else:
        print("NO")
    print(abs(sum_top - sum_bot))

if __name__ == "__main__":
    main()