import math
a=[1]* 1000001

def init() :
    a[0]= a[1]=0
    for i in range(2,1000):
        if a[i]==1:
            for j in range(i*i , 1000001 ,i) : a[j] = 0
                

init()
t=int(input())
for k in range(0,t):
    n=int(input())
    for hoa in range(1,n):
        # chuyển 1 số thàn chuỗi là dùng str()
        #  đâỏ ngược chuỗi : sử dụng [::-1]
        #  eps laij thanhf kiểu int()
        k=int(str(hoa)[::-1])
        print(f"day la so {k}")
        if k >hoa and k< n  and a[k]==1 and a[hoa]==1:
            print(hoa,k,end=' ')
    print()
    