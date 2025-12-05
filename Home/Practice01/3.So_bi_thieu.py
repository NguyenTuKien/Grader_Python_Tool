import sys

inp = sys.stdin.buffer.read().strip().split()
total = int(inp[0])                           
total = total * (total + 1) // 2              
total -= sum(map(int, inp[1:]))              
print(total)
