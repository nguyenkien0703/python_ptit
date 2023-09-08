t=int(input())
for k in range(0,t):
    [n,m]=input().split();
    n=int(n)
    m=int(m)

    a=[int(x) for x in input().split()]
    for h in range(m, n):
        print(a[h],end=' ')
    for h in range(0,m):
        print(a[h],end=' ')
    print()
