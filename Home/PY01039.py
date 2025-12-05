if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        s = input()
        ok = True
        for i in range(len(s) - 2):
            if s[i] != s[i + 2]:
                ok = False
                break
        if ok:
            print("YES")
        else:
            print("NO")