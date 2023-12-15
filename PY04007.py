# tich cua ma tran a voi chuyen vi cua no 
t = int(input())
for kk in range(t):
    n, m =[int(x) for x in input().split()]
    a=[]
    for i in range(n):
        a.append([int(x) for x in input().split()])
    b= []
    for i in range(m):
        b.append([])
        for j in range(n):
            b[i].append(a[j][i])

    ans=[]
    for i in range(n):
        r=[]
        for j in range(n):
            x= 0
            for k in range(m):
                x += a[i][k] * b[k][j]
            r.append(str(x))
        ans.append(r)

    for i in ans:
        print(' '.join(i))
