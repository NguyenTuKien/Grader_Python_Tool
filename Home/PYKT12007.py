from sys import stdin

def main():
    # Đọc toàn bộ dữ liệu một lần
    data = stdin.buffer.read().split()
    it = iter(data)
    for _ in range(int(next(it))):
        n, u = int(next(it)), float(next(it))
        arr = [float(next(it)) for _ in range(n)]
        arr.sort()
        for i in range(n - 1):
            diff = (arr[i + 1] - arr[i]) * (i + 1)
            if u >= diff:
                u -= diff
                for j in range(i + 1):
                    arr[j] = arr[i+1]
            else:
                inc = u / (i + 1)
                for j in range(i + 1):
                    arr[j] += inc
                u = 0
                break
        if u > 0:
            avg = min((sum(arr) + u) / n, 1.0)
            ans = avg ** n
        else:
            ans = 1.0
            for x in arr:
                ans *= x
                
        print(f"{ans:.6f}")

if __name__ == "__main__":
    main()