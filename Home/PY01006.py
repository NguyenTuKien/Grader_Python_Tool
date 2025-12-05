for _ in range(int(input())):
    ok = True
    s = input()
    for i in s:
        if i not in '47':
            ok = False
            break
    if ok :
        print("YES")
    else :
        print("NO")