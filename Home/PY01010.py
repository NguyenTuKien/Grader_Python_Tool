for _ in range(int(input())):
    s = input()
    head = s[:2]
    tail = s[-2:]
    if head == tail:
        print("YES")
    else :
        print("NO")
