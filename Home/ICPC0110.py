from sys import stdin


def main():
    data = stdin.buffer.read().split()
    it = iter(data)
    for _ in range(int(next(it))):
        n = int(next(it))
        max1 = max2 = max3 = -10**20   # nhỏ hơn cả min A[i]
        for _ in range(n):
            x = int(next(it))
            if x > max1:
                max3 = max2
                max2 = max1
                max1 = x
            elif x > max2:
                max3 = max2
                max2 = x
            elif x > max3:
                max3 = x
        print(max1 + max2 + max3)
  
if __name__ == "__main__":
    main()