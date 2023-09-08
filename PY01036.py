from math import * 
t=int(input())

def solve(n):
    sum=0.0
    if n %2==1:
        for i in range(1,n+1,2):
            sum += (1.0/i)
    else:
        for i in range(2,n+1,2):
            sum += (1.0/i)
    # lamf tròn đến 6 chữ số phần thập phân
    print('{:.6f}'.format(sum))

while t >0:
    n=int(input())
    solve(n)
    t-=1