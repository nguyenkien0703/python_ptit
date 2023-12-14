import functools
t=int(input())
# so sánh tiêu chí có sử dụng cmp thì import functools
def tong(n):
    sum =0
    while n>0:
        sum += n%10
        n//=10
    return sum 
    
def cmp(a, b):
    if tong(a) == tong(b):
        # nếu a đang lớn hơn b, thì return 1 cho a nhỏ hơn b để sx. return 1 
        if a >  b : return 1
        else : return -1
        # return a < b
    elif tong(a) > tong(b): return 1
    else: return -1

while t > 0 :
    n=int(input())
    a=[int(x) for x in input().split()]
    a=sorted(a, key=functools.cmp_to_key(cmp))
    for i  in a : print(i,end=" ")
    print()
    t-=1
