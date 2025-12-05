n = int(input())
a = list(map(int, input().split()))
st = []
for it in a:
    if st and (st[-1] + it) % 2 == 0:
        st.pop()
    else :
        st.append(it)  
    
print(len(st))
    