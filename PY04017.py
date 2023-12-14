def clearGIO(s: str):
    h, m= s.split(':')
    return int(h) * 60 + int(m)




class sv:
    def __init__ (self, name, dd, end)-> None:
        self.name = name 
        self.dd = dd 
        self.time  =( clearGIO(end) - clearGIO('06:00'))/60
        # print(self.time)
        self.v = 120/(self.time)
        self.ID = ''
        for i in dd.split(): self.ID += i[0].upper()
        for i in name.split(): self.ID += i[0].upper()


    def __str__ (self)-> str:
        return self.ID +" "+ self.name +" " +self.dd +" " + f'{round(self.v)}'+" " + "Km/h"





a=[]
n = int(input())
for i in range(n):
    a.append(sv(input(),input(), input()))
for i in sorted(a,  key = lambda x: -x.v): 
    print(i)





