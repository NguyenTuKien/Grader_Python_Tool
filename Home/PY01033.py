from math import gcd

def check(a, b, c):
    if gcd(a, b) == 1 and gcd(b, c) == 1 and gcd(a, c) == 1:
        return True
    return False

if __name__ == "__main__":
    l, r = map(int, input().split())
    for i in range(l, r + 1):
        for j in range(i + 1, r + 1):
            for k in range(j + 1, r + 1):
                if(check(i, j, k)):
                    print(f"({i}, {j}, {k})")