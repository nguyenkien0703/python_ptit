# import math

# Prime=[1] * 10000000
# def init():
#     Prime[0]=Prime[1]=0;
#     for i in range(2,1000):
#         if Prime[i]==1:
#             for j in range(i*i, 10000000, i): Prime[j]=0


# def check1(a):
#     sum =0;
#     while a!=0 :
#         r = a%10;
#         sum += r 
#         if Prime[r]== 0:   
#             return False
#         # chia số nguyên trong python thì //, còn / thì nó ra số thực 
#         a//=10
#     if Prime[sum]!= 1:
#         return False
#     return True 

# init()
# t = int(input())
# for k in range(t):
#     n=int(input());
#     k=int(str(n)[::-1]);
#     if Prime[n]==1  and Prime[k]==1 and check1(n)== True :
#         print("Yes")
#     else:
#         print("No")

import math
def nto(n):
    for i in range(2,int(math.sqrt(n)) + 1):
        if n%i ==0:
            return False;
    return True
def check(n):
    sum =0
    x=n
    m =0;
    while n > 0:
        r = n%10
        m= m * 10 + r 
        if nto(r) == False: return False
        sum += r 
        n//=10
    if nto(sum) and nto(x) and nto(m): return True
    else:
        return False



t=int(input())

for k in range(t):
    n=int(input())
    if check(n):
        print("Yes")
    else:
        print("No")

