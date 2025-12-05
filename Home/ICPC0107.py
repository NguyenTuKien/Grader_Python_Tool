for _ in range(int(input())):
    a, b = input().split()
    s1 = input()
    s2 = input()
    s1 = s1.replace(a, b)
    s2 = s2.replace(a, b)
    num1 = int(s1) + int(s2)
    s1 = s1.replace(b, a)
    s2 = s2.replace(b, a)
    num2 = int(s1) + int(s2)
    if num1 > num2 : num1, num2 = num2, num1
    print(num1, num2)

