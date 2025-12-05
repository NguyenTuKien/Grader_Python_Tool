if __name__ == "__main__":
    queue = ["2", "4", "6", "8"]
    i = 0
    while i < len(queue):
        tmp = queue[i]
        if len(tmp) < 3: 
            if int(tmp + "0") < 1000: queue.append(tmp + "0")
            if int(tmp + "2") < 1000: queue.append(tmp + "2")
            if int(tmp + "4") < 1000: queue.append(tmp + "4")
            if int(tmp + "6") < 1000: queue.append(tmp + "6")
            if int(tmp + "8") < 1000: queue.append(tmp + "8")
        i += 1
    ls = []
    for half in queue:
        tmp = half + half[::-1]
        num = int(tmp)
        if num < 1000000:
            ls.append(num)
    ls.sort()
    for _ in range(int(input())):
        n = int(input())
        out = []
        for num in ls:
            if num < n:
                out.append(str(num))
            else:
                break
        print(" ".join(out))