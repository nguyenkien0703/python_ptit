t=int(input())
while t>0:
    ok =0
    n=int(input())
    #  nhập vào mảng a rồi sort tăng dần luôn trong python 
    a=sorted([int(x) for x in input().split()])

    b=sorted([int(x) for x in input().split()])
    for i in range(0,n):
        if a[i] >b[i]:
            ok =1
            break
    if ok ==0:
        print("YES")
    else: print("NO")
    t-=1