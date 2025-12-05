from sys import stdin

def main():
    data = stdin.buffer.read().split()
    it = iter(data)
    for _ in range(int(next(it))):
        m, n = int(next(it)), int(next(it))
        a = [[int(next(it)) for _ in range(n)] for _ in range(m)]
        a_t = list(zip(*a))
        res = [[0 for _ in range(m)] for _ in range(m)]
        for i in range(m):
            for j in range(m):
                for k in range(n):
                    res[i][j] += a[i][k] * a_t[k][j]
        for row in res:
            print(" ".join(map(str, row)))

if __name__ == "__main__":
    main()