import math

prime = [1] * 1000006

def init():
    prime[0] = prime[1] = 0
    for i in range(2, 1001):
        if prime[i] == 1:
            for j in range(i * i, 1000001, i):
                prime[j] = 0
            
init()
for i in range(int(input())):
    a, b = map(int, input().split())
    u = str(math.gcd(a, b))
    t = 0
    for i in u:
        t += int(i)
    if prime[t] == 1:
        print("YES")
    else :
        print("NO")
