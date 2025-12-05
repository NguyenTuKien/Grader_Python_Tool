from sys import stdin

def check(val):
    if val < 2:
        return False
    for i in range(2, int(val ** 0.5) + 1):
        if val % i == 0:
            return False
    return True

def main():
    data = stdin.buffer.read().split()
    it = iter(data)
    # for _ in range(int(next(it))):
    m, n = int(next(it)), int(next(it))
    matrix = [[int(next(it)) for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if check(matrix[i][j]):
                print("1", end=" ")
            else:
                print("0", end=" ")
        print()

if __name__ == "__main__":
    main()
