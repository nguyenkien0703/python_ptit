class per:
    def __init__(self, code,name, sl, dg, ck)-> None:
        self.code = code 
        self.name = name 
        self.sl = sl 
        self.dg = dg 
        self.ck = ck 
        self.tt = self.sl * self.dg - self.ck

    def __str__(self)-> str:
        return str(self.code) + " "+ str(self.name) +" " + str(self.sl) +" " + str(self.dg)+" "+ str(self.ck) +" " + str(self.tt)
    
a=[]
for i in range(int(input())):
    a.append(per(input(), input(), int(input()), int(input()), int(input()) ))
a.sort(key=lambda x: (-x.tt))
for i in a:
    print(i)
