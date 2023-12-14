from math import * 
def nto(n):
    for i in range(2, int(sqrt(n)) + 1 ):
       if n% i==0:
           return False;    
    return True;

t=int(input())
def solve(s):
    # chuyeenr 1 chuỗi số thành 1 số nguyên thì dùng int(chuoi)
    if nto(int(s[:3])) == True and nto(int(s[len(s) -3:])) == True:
        print("YES")
        return
    print("NO")


while t > 0:
    s=input()
    solve(s)

    t-=1