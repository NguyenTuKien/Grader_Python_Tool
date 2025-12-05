from sys import stdin

def dfs(adj, used, cur, target, banned):
    if cur == target:
        return True
    used[cur] = True
    for node in adj[cur]:
        if node != banned and not used[node]:
            if dfs(adj, used, node, target, banned):
                return True
    return False

def main():
    data = stdin.buffer.read().split()
    it = iter(data)
    for _ in range(int(next(it))):
        n, m, u, v = int(next(it)), int(next(it)), int(next(it)), int(next(it))
        adj = [[] for _ in range(n + 1)]
        for _ in range(m):
            x, y = int(next(it)), int(next(it))
            adj[x].append(y)
        used = [False] * (n + 1)
        if not dfs(adj, used, u, v, -1):
            print(0)
            continue
        cnt = 0
        for i in range(1, n + 1):
            if i == u or i == v:
                continue
            used = [False] * (n + 1)
            if not dfs(adj, used, u, v, i):
                cnt += 1
        print(cnt)

if __name__ == "__main__":
    main()
                

    
