for t in range(int(input())):
    n=int(input())
    a=[int(x) for x in input().split()]
    ans =[]
    st = []
    for i in range(n):
        while len(st) > 0 and a[i] >= a[st[-1]]:
            st.pop()
        if len(st)==0:
            ans.append(i+1)
        else:
            ans.append(i-st[-1])
        st.append(i)
    for i in ans:
        print(i,end =' ')
    print()