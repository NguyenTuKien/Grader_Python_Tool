from sys import stdin

def main():
    input_data = stdin.read().split()
    it = iter(input_data)
    for _ in range(int(next(it))):
        n = int(next(it))
        freq = {}
        val, mx_fre = -1, 0
        for i in range(n):
            x = int(next(it))
            if x in freq:
                freq[x] += 1
            else :
                freq[x] = 1
            if freq[x] > mx_fre : 
                val = x
                mx_fre = freq[x]
        if mx_fre > n // 2:
            print(val)
        else :
            print("NO")

if __name__ == "__main__":
    main()