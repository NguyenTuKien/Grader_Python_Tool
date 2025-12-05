from sys import stdin

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def check(s):
    for i, x in enumerate(s):
        if is_prime(i) ^ is_prime(int(x)):
            return False    
    return True

def main():
    data = stdin.buffer.read().split()
    it = iter(data)
    for _ in range(int(next(it))):
        s = next(it).decode()
        if check(s):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()