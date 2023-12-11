class per:
    def __init__(self, name, ns, d1,d2,d3)-> None:
        self.name = name
        self.ns = ns
        self.tong = float(d1) + float(d2) + float(d3)

    def __str__(self)-> str:
        return self.name + ' '+ self.ns +" "+ f'{self.tong:.1f}'
    
a=[]
a.append(per(input(),input(),float(input()),float(input()),float(input())))
for i in a :
    print(i)