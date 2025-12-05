for _ in range(int(input())):
    n = int(input())
    a = map(int, input().split())
    a.sort()
    cnt = 0
    for i in range(n - 2):
        l, r = i + 1, n - 1
        while l < r:
            if a[l] + a[r] + a[i] > 0:
                r -= 1
            elif a[l] + a[r] + a[i] < 0:
                l += 1
            else :
                l += 1
                cnt += 1
    print(cnt)