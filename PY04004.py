from math import * 
#  tính tổng hai class phân số trong python
class P:
    def __init__(po,tu=None,mau=None):
        po.tu = tu
        po.mau = mau
    #  hàm __str__ là hàm có sẵn, xác định kiểu chuỗi trả vè dc hiển thị như thế nào 
    def __str__(po):
        return f'{po.tu}/{po.mau}'
    #  khi goi a+b thif nó sẽ chạy vào hầm add này 
    def __add__(po, other):
        c= P()
        c.mau = po.mau * other.mau
        c.tu = po.tu * other.mau + po.mau * other.tu
        c.rg()
        return c 
    
    def rg(po):
        r = gcd(po.tu, po.mau)
        po.tu //=r 
        po.mau //=r 




list = [int(i) for i in input().split()]
a = P(list[0], list[1])
b = P(list[2], list[3])
c = a + b
print(c)




