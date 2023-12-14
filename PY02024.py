import functools
t=int(input())
# so sánh tiêu chí có sử dụng cmp thì import functools
def tich(n):
    sum =1
    # chuyển 1 số nguyên sang 1 chuoix 
    kien =str(n)
    for i in kien:
        # kieemr tra xem 1 kí tự có là kí tự số không
        if i.isdigit():
            # chuyển 1 kí tự từ kí tự só sang số nguyên 
            sum *=int(i)
    return sum 


def cmp(a, b):
    if tich(a) == tich(b):
        # nếu a đang lớn hơn b, thì return 1 cho a nhỏ hơn b để sx. return 1 
        if a >  b : return 1
        else : return -1
        # return a < b
    elif tich(a) > tich(b): return 1
    else: return -1

while t > 0 :
    n=int(input())
    a=[int(x) for x in input().split()]
    a=sorted(a, key=functools.cmp_to_key(cmp))
    for i  in a : print(i,end=" ")
    print()
    t-=1
