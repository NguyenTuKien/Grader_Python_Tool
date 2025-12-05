m = int(input())
v = int(input())
t = int(input())
d = input()
res = (v * t) % m
if d == 'A':
    res = m - res

print(res)