if __name__ == "__main__":
    for _ in range(int(input())):
        s = input()
        ok = True
        for i in s:
            if i != '0' and i != '1' and i != '2':
                ok = False
                break
        if ok:
            print("YES")
        else:
            print("NO")