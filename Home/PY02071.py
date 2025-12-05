from sys import stdin

def backtrack(limit, remain, path, results):
    if remain == 0:
        results.append(path[:])
        return
    for i in range(limit, 0, -1):
        if i <= remain:
            path.append(i)
            backtrack(i, remain - i, path, results)
            path.pop() 
def main():
    data = stdin.buffer.read().split()
    it = iter(data)
    for _ in range(int(next(it))):
        n = int(next(it))
        results = []
        backtrack(n, n, [], results)
        print(len(results))
        formatted_strings = []
        for res in results:
            s = "(" + " ".join(map(str, res)) + ")"
            formatted_strings.append(s)
        print(" ".join(formatted_strings))

if __name__ == "__main__":
    main()