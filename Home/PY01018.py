p = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'
while True:
    try:
        line = input()
        if line == "0":
            break
            
        k, s = line.split()
        k = int(k)
        
        a = ''
        for i in s:
            a += p[(p.index(i) + k) % 28]
        a = a[::-1]
        print(a)
    except ValueError:
        break


