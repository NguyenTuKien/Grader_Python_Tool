def count(n, dg):
    cnt, f = 0, 1
    while n // f:
        l = n - (n // f) * f
        cur = (n // f) % 10
        r = n // (f * 10)

        if dg != 0:
            if cur > dg:
                cnt += (r + 1) * f
            elif cur == dg:
                cnt += r * f + l + 1
            else:
                cnt += r * f
        else:
            if cur > 0:
                cnt += r * f
            elif cur == 0:
                cnt += (r - 1) * f + (l + 1)
            else:
                cnt += (r - 1) * f
        f *= 10
    return cnt
    
def countTo(n):
    return [count(n, dg) for dg in range(10)]

t = int(input())
while t > 0:
    t -= 1
    a, b = map(int, input().split())
    ca = countTo(a - 1)
    cb = countTo(b)
    ans = [cb[i] - ca[i] for i in range(10)]
    for i in range(10):
        print(ans[i], end = " ")
    print()