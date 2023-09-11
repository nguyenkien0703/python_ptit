from math import * 
def check(kien):
    
    for i in range(2, int(sqrt(kien)) + 1):
        if kien%i==0:
            return False
    return True




def solve(s):
    sum = 0
    for i in s:
        sum += int(i);
    
    if check(sum)== True:
        print("YES")
    else:
        print("NO")
t=int(input())
while t> 0:
    s=input()
    solve(s)
    t-=1