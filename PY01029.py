import math
t=int(input())
def solve(s):
    s=s
    tmp = s[::-1]
    if math.gcd(int(s),int(tmp))==1:
        print("YES")
    else:
        print("NO")

while t >0:
    s=input()
    solve(s)
    t-=1
    

