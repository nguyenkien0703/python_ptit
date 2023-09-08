def Prime(n):
    for i in range(2,int(n**0.5)+ 1 ):
        if n%i==0:
            return 0
    return  n> 1
def check(n):
    if (Prime(n) and Prime(n+2) and Prime(n+6)) or (Prime(n) and Prime(n+4) and Prime(n+6)):
        return 1
    else:
        return 0

t =int(input())
for k in range(0,t):
    n=int(input())
    cnt =0
    for i in range(2,n):
        if check(i)==1 and (i+6)<= n:
            cnt+=1
    print(cnt)