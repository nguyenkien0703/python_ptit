from math import * 

def solve(s):
    tich =1
    for i in s:
        if i!='0':
            tich *= int(i)
    print(tich)

t=int(input())
while t> 0:
    s=input()
    solve(s)
    t-=1