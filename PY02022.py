from math import * 

a=[1]* 1000007

def init() :
    a[0]= a[1]=0
    for i in range(2,int(sqrt(1000007)) + 1):
        if a[i]==1:
            for j in range(i*i , 1000007 ,i) : a[j] = 0

init()
m={}
n=int(input())
b=[int(x) for x in input().split()]
for i in b:
    if a[i]==1:
        if i in m :
            m[i]+=1
        else: m[i]=1

for i in m :
    print("{} {}".format(i,m[i]))