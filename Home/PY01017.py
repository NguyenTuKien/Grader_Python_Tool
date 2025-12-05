for _ in range(int(input())):
    s = input()
    for i, val in enumerate(s):
        if i == 0:
            cnt = 1
        elif val != s[i - 1]:
            print(str(cnt) + s[i - 1], end="")
            cnt = 1
        else :
            cnt += 1
    print(str(cnt) + s[-1])