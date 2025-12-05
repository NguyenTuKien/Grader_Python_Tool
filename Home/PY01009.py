s = input()
upper_case = 0
lower_case = 0
for i in s:
    if 'a' <= i <= 'z':
        lower_case += 1
    elif 'A' <= i <= 'Z':
        upper_case += 1
if lower_case >= upper_case:
    print(s.lower())
else :
    print(s.upper())