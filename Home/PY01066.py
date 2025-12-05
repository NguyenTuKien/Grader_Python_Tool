if __name__ == '__main__':
    for _ in range(int(input())) : 
        s = input()
        s_rev = s[::-1]
        ok = True
        for i in range(1, len(s)):
            if abs(ord(s[i]) - ord(s[i - 1])) != abs(ord(s_rev[i]) - ord(s_rev[i - 1])):
                ok = False
                break
        if ok : 
            print("YES")
        else : 
            print("NO")
