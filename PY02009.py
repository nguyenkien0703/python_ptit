t=int(input())
for i in range(t):
    n=int(input())
    #  khai báo map trong python
    m={}
    for i in range(n):
        x=int(input())
        #  nếu x ở trong map rồi 
        #  tăng số lượng xuát hiện của x lên 
        if x in m : m[x]+=1
        else : m[x]=1
    s=0
    #  duyệt map trong python 
    p=100000
    for i in m:
        if m[i]> s:
            s=m[i]
            p=i
        elif m[i]==s:
            p=min(p,i)
    print(p)