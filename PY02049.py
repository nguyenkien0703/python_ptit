

def pt(n,p):
    cnt =0;
    for i in range(1,n+1):
        if i%p==0:
            while i%p==0:
                cnt+=1
                i/=p;

    return cnt ;

t=int(input())
for k in range(t):
    a=[int(x) for x in input().split()]

  
    print(pt(a[0],a[1]))
    print()