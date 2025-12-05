import math

if __name__ == '__main__':
    a0, b0, c0 = map(int, input().split())
    a1, b1, c1 = map(int, input().split())

    if a1 < a0:
        a1 += 24
    time1 = a0 * 3600 + b0 * 60 + c0
    time2 = a1 * 3600 + b1 * 60 + c1
    print(time2 - time1)