import math

deg = [0] * 1000009
if __name__ == '__main__':
    n = int(input())
    for i in range(1, n):
        a, b = map(int, input().split())
        deg[a] += 1
        deg[b] += 1
        
    cnt, ver = 0, 0
    for i in range(1, n + 1):
        if deg[i] == 1:
            cnt += 1
        else:
            ver = i
    if cnt == n - 1 and deg[ver] == n - 1:
        print("Yes")
    else:
        print("No")

