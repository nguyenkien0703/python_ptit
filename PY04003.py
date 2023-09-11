from math import * 

class P:
    def __init__(po,tu,mau):
        po.tu = tu
        po.mau = mau
    def rg(po):
        r = gcd(po.tu, po.mau)
        po.tu //=  r
        po.mau //=  r
        return "{}/{}".format(po.tu,po.mau)
tu,mau = map(int,input().split())
A= P(tu,mau)
print(A.rg())