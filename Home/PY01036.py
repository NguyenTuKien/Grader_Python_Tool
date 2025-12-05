if __name__ == "__main__":
    for _ in range (int(input())):
        n = float(input())
        sum = 0.0
        if n % 2 == 0:
            for i in range(2, int(n)+1, 2):
               sum += 1 / i
        else:
            for i in range(1, int(n)+1, 2):
                sum += 1 / i
        print(f"{sum:.6f}")
