from math import *
def check(n, m ):
    if gcd(n,m)==1:
        return True
    return False

n=int(input())
a=[int(x) for x in input().split()]

a=sorted(a)
for i in range(n-1):
    for j in range(i+1, n):
        if(check(a[i],a[j])== True):
            print('{} {}'.format(a[i],a[j]))

