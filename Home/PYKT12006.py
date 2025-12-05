from sys import stdin

def main():
    data = stdin.buffer.read().split()
    it = iter(data)
    n, k = int(next(it)), int(next(it))
    a = [int(next(it)) for _ in range(n)]
    b = [int(next(it)) for _ in range(n)]
    items = []
    for i in range(n):
        diff = a[i] - b[i]
        items.append((diff, a[i], b[i])) 
    items.sort()
    total_cost = 0
    for i in range(n):
        diff, price_a, price_b = items[i]
        if i < k:
            total_cost += price_a
        else:
            total_cost += min(price_a, price_b)
            
    print(total_cost)

if __name__ == "__main__":
    main()