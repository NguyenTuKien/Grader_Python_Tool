import sys

def solve(n):
    if len(n) < 3: 
        return "NO"
    for i in range(len(n) - 1):
        if n[i] < n[i+1]:
            for j in range(i, len(n)):
                if j == len(n) - 1:
                    return "YES"
                if n[j] <= n[j+1]:
                    break
        else :
            for j in range(i, len(n)):
                if j == len(n) - 1:
                    return "YES"
                if n[j] <= n[j+1]:
                    break
            return "NO"


if __name__ == "__main__":
    for t in range(int(sys.stdin.readline())):
        n = sys.stdin.readline()
        print(solve(n))
        
        
                        
                    
                    