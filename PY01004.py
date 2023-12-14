import math
def nto(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n%i ==0:
            return 0
    return n > 1 


t = int(input())
for k in range(0,t):
    
    x = int(input())
    s =0
    for i in range(1,x):
        if math.gcd(i,x) ==1:
            s+=1
    if nto(s):
        print("YES")
    else: print("NO")