for _ in range(int(input())):
    n, x, m = map(float, input().split())
    i = 0
    while n < m:
        n =  n * (100 + x) / 100
        i += 1
    print(i)  