# from functools import reduce
from decimal import ROUND_HALF_UP, Decimal
class stu:
    def __init__(self, i, n, a) -> None:
        self.code = f'HS{str(i).zfill(2)}'
        self.name = n
        self.diem = 0
        for i in range(len(a)):
            if i== 0 or i == 1:
                self.diem += a[i] * 2
            else :
                self.diem += a[i]
        self.tbc = self.diem / 12        
        self.tbc = (self.tbc).quantize(Decimal('0.1'), ROUND_HALF_UP)
        if self.tbc >= 9: self.type = 'XUAT SAC'
        elif self.tbc >= 8: self.type = 'GIOI'
        elif self.tbc >= 7: self.type = 'KHA'
        elif self.tbc >= 5: self.type = 'TB'
        else: self.type = "YEU"
a = []
for i in range(int(input())):
    a.append(stu(i + 1, input(), [Decimal(x) for x in input().split()]))
a.sort(key = lambda x: (-x.tbc, x.code))
for i in a: print(i.code, i.name, i.tbc, i.type)