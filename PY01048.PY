t=int(input())
for k in range(t):
    n=int(input())
    cnt=0
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            if i%2==1: cnt+=1
            if (n/i)!=i and  (n/i)%2==1: cnt+=1
    print(cnt-1)