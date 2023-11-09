from math import  * 
Prime=[1] * 10005

def init():
    for i in range(2,int( sqrt(10005))+1):
        if Prime[i]==1:
            for j in range(i*i,10005,i):
                Prime[j]=0


init()
a=[]
b=[]
n,x = map(int, input().split())
a.append(x)
cnt =2
kien =1
while kien <=n:
    if Prime[cnt]==1:
        b.append(cnt)
        
        kien+=1
    cnt+=1

for i in range(1,n+1):
    a.append(a[i-1] + b[i-1])
for i in range(0,n+1):
    print(a[i],end=' ')