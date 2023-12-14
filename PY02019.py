from math import * 

def check(a, b):
    return gcd(a,b)==1

n=int(input())
a=sorted([int(x) for x in input().split()])
for i in range(0,n-1):
    for j in range(i+1, n):
        if check(a[i],a[j])==True:
            print('{} {}'.format(a[i],a[j]))
