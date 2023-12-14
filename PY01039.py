from math import *

t=int(input())

def solve(n):
    for i in range(1,len(n)):
        if(n[i]==n[i-1]) or (i>1 and n[i]!=n[i-2]):
            print("NO")
            return
    print("YES")

while t> 0:
    n=input()
    solve(n)
    t-=1    