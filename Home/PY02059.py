from sys import stdin

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def main():
    data = stdin.buffer.read().split()
    it = iter(data)
    pos = [[] for _ in range(10000)]
    m, n, mx = int(next(it)), int(next(it)), 0  
    for i in range(m):
        for j in range(n):
            cur = int(next(it))
            if is_prime(cur) :
                mx = max(mx, cur)
                pos[cur].append((i, j))
    if not is_prime(mx):
        print("NOT FOUND")
    else :
        print(mx)
        for i, j in pos[mx]:
            print(f"Vi tri [{i}][{j}]")
    
if __name__ == "__main__":
    main()
