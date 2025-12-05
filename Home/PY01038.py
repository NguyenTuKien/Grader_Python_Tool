import sys

def solve(n):
    while n % 7 != 0:
        tmp = str(n)
        tmp = tmp[::-1]
        n = int(tmp) + n
    return n

if __name__ == "__main__":
    for i in range(int(sys.stdin.readline())):
        n = int(sys.stdin.readline())
        print(solve(n))