from sys import stdin
from collections import deque

def check_kahn(node_cnt, adj, in_degree):
    queue = deque()
    
    for i in range(node_cnt):
        if in_degree[i] == 0:
            queue.append(i)
            
    processed_count = 0
    while queue:
        u = queue.popleft()
        processed_count += 1
        
        for v in adj[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
                
    return processed_count == node_cnt

def main():
    data = stdin.buffer.read().split()
    it = iter(data)

    adj = []        
    in_degree = []  
    name_map = {}   
    node_cnt = 0    

    for _ in range(int(next(it))):
        u_name = next(it)
        op = next(it)
        v_name = next(it)

        if u_name not in name_map:
            name_map[u_name] = node_cnt
            node_cnt += 1
            adj.append([])
            in_degree.append(0)
            
        if v_name not in name_map:
            name_map[v_name] = node_cnt
            node_cnt += 1
            adj.append([])
            in_degree.append(0)
            
        u = name_map[u_name]
        v = name_map[v_name]

        if op == b'>':
            adj[u].append(v)
            in_degree[v] += 1
        elif op == b'<':
            adj[v].append(u)
            in_degree[u] += 1
            
    if check_kahn(node_cnt, adj, in_degree):
        print("possible")
    else:
        print("impossible")

if __name__ == "__main__":
    main()