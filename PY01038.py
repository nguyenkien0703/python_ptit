from math import *

t=int(input())

def solve(n):
    sum =n
    cnt =0
    ok=0
    while cnt <1000:
        if sum %7==0:
            ok=1
            print(sum)
            break;
        s=int(str(sum)[::-1])
        # print(s)
        sum +=s

    if ok ==0:
        print(-1)


while t>0:
    n=int(input())
    solve(n)
    t-=1
