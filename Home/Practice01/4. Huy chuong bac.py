import sys
inf = -10**19

n = int(sys.stdin.readline())
m1, m2 = inf, inf

for i in range(n):
    x = int(sys.stdin.readline())
    if x > m1:
        m1, m2 = x, m1
    elif x != m1 and x > m2:
        m2 = x
print("Silver =", m2)