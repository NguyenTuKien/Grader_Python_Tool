from sys import stdin


def main():
    data = stdin.buffer.read().split()
    it = iter(data)
    for _ in range(int(next(it))):
        n = int(next(it))
        A = [-1.0 for _ in range(n + 1)]
        B = [1e9 * 1.0 for _ in range(n + 1)]
        dp = [0 for _ in range(n + 1)]
        for i in range(1, n + 1):
            A[i], B[i] = float(next(it)), float(next(it))
        for i in range(1, n + 1):
            for j in range(i):
                if A[i] > A[j] and B[i] < B[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        print(max(dp))            
if __name__ == "__main__":
    main() 