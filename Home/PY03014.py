from sys import stdin

def main():
    for _ in range(int(stdin.readline())):
        line = stdin.readline().strip()
        stack = []
        idx = 1
        ans = ""
        for c in line:
            if c == '(':
                ans += str(idx) + " "
                stack.append(idx)
                idx += 1
            elif c == ')':
                if stack:
                    ans += str(stack.pop()) + " "
        print(ans.strip())

if __name__ == "__main__":
    main()