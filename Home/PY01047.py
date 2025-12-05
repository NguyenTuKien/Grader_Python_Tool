import math

def check_prime(n):
    if n < 2 : return False
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    for _ in range(int(input())):
        s = input()
        num = int(s[-4:])
        # print(num)
        if check_prime(num) : print("YES")
        else : print("NO")
