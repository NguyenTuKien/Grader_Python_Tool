import math

def check(value):
    int_value = int(value)
    rev_value = int(value[::-1])
    GCD = math.gcd(int_value, rev_value)
    if GCD > 1:
        return False
    return True

if  __name__ ==  "__main__":
    for _ in range(int(input())):
        value = input()
        if check(value):
            print("YES")
        else:
            print("NO")