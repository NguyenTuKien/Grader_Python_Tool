from sys import stdin

def main():
    input_data = stdin.read().split()
    it = iter(input_data)
    for _ in range(int(next(it))):
        m, n, ans = int(next(it)), int(next(it)), 0
        matrix = [[int(next(it)) for _ in range(n)] for _ in range(m)]
        kernel = [[int(next(it)) for _ in range(3)] for _ in range(3)]
        for i in range(m - 2):
            for j in range(n - 2):
                val = 0
                for di in range(0, 3):
                    for dj in range(0, 3):
                        val += matrix[i + di][j + dj] * kernel[di][dj]
                ans += val
        print(ans)

if __name__ == "__main__":
    main()