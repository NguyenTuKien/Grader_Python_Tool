t = int(input())
while t > 0:
    a = input()
    tmp = 0
    ans = 0
    found = False  
    for it in a:
        if '0' <= it <= '9':
            tmp = tmp * 10 + int(it)
            found = True
        else:
            if found:
                ans = max(ans, tmp)
                tmp = 0
                found = False

    if found:
        ans = max(ans, tmp)

    print(ans)
    t -= 1
