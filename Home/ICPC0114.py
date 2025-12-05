from sys import stdin

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def check(num):
    sum = 0
    for x in num:
        if not is_prime(int(x)):
            return False
        sum += int(x)
    if is_prime(sum):
        return True
    return False

def main():
    data = stdin.buffer.read().split()
    it = iter(data)
    for _ in range(int(next(it))):
        num = next(it).decode()
        if is_prime(int(num)) and is_prime(int(num[::-1])) and check(num):
            print("Yes")
        else:
            print("No")

if __name__ == "__main__":
    main()