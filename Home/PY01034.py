from sys import stdin

for _ in range(int(stdin.buffer.readline())):
    n = list(stdin.buffer.readline().decode().strip())
    org = "".join(n)
    pivot = -1
    for i in range(len(n) - 1, 0, -1):
        if int(n[i]) < int(n[i - 1]):
            pivot = i - 1
            break
    if pivot == -1:
        print(-1)
        continue
    mx, idx = -1, pivot
    for i in range(pivot + 1, len(n)):
        if int(n[i]) < int(n[pivot]) and int(n[i]) > mx:
            mx = int(n[i])
            idx = i
    n[pivot], n[idx] = n[idx], n[pivot]
    ans = "".join(n)
    if n[0] == '0' or ans == org:
        print(-1)
    else :
        print(ans)
        