import math

if __name__ == "__main__":
    t = input()
    a = t.split()
    st, length = 0, 0
    for i in a:
        if len(i) > length:
            length = len(i)
            st = i
    print(st, length)